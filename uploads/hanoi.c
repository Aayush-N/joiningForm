#include <stdlib.h>
#include <stdio.h>
#include <GL/glut.h>

#define BREITE 0.1f
#define STANGENBREITE 0.025f
#define SLICES 32
#define INNERSLICES 16
#define LOOPS 1
#define FPS 64   /* more looks nicer, uses more cpu power */
#define FEM 1000.0/FPS
#define FSEM 0.001f   /* speed (bigger is faster)*/

struct config {
	GLfloat gap;
	GLfloat pinradius;
	GLfloat pinheight;
};

struct action {
	char fromstack;
	char tostack;
	struct action *next;
};
typedef struct action action;

struct actions {
	action *head;
	action *tail;
};
typedef struct actions actions;
struct disk {
	char color;
	GLfloat radius;
	struct disk *next;
	struct disk *prev;
};
typedef struct disk disk;

struct stack {
	disk *bottom;
	disk *top;
};
typedef struct stack stack;

int disks=3;  //initial number of disks
GLfloat rotX, rotY, zoom, offsetY = 1.5, speed;
GLUquadricObj *quadric;
GLfloat pos;
GLboolean fullscreen;
stack pin[3];
float pinheight[3];
struct config config;
actions actqueue;
action *curaction;
disk *curdisk;
int duration;
char seconds[24] = "Time: 0s";
int draw, maxdraws;

//function prototypes
void moveDisk(int param);
void hanoiinit(void);
void reset();
void Display(void);
void hanoi(actions *queue, const int n, const char pin1, const char pin2, const char pin3);
void push(stack *pin, disk *item);
disk *pop(stack *pin);
void drawDisk(GLUquadricObj **quadric, const GLfloat outer, const GLfloat inner);
void drawPin(GLUquadricObj **quadric, const GLfloat radius, const GLfloat height);
void drawAllPins(GLUquadricObj **quadric, const GLfloat radius, const GLfloat height, const GLfloat gap);
void drawBitmapString(const GLfloat x, const GLfloat y, const GLfloat z, void *font, char *string);
void drawBitmapInt(const GLfloat x, const GLfloat y, const GLfloat z, void *font, const int number);




void hanoi(actions *queue, const int n, const char pin1, const char pin2, const char pin3)
{
	action *curaction;
	if(n > 0)
	{	hanoi(queue, n-1, pin1, pin3, pin2);
		/* push action into action queue */
		curaction = (action *)malloc(sizeof(action));
		curaction->next = NULL;
		curaction->fromstack = pin1;
		curaction->tostack = pin3;
		if(queue->head == NULL)
			queue->head = curaction;
		if(queue->tail != NULL)
			queue->tail->next = curaction;
		queue->tail = curaction;
		hanoi(queue, n-1, pin2, pin1, pin3);
	}
}

/** push item to pin */
void push(stack *pin, disk *item) {
	item->next = NULL;
	if(pin->bottom == NULL) {
		pin->bottom = item;
		pin->top = item;
		item->prev = NULL;
	} else {
		pin->top->next = item;
		item->prev = pin->top;
		pin->top = item;
	}
}

/** pop item from pin */
disk *pop(stack *pin) {
	disk *tmp;
	if(pin->top != NULL) {
		tmp = pin->top;
		if(pin->top->prev != NULL) {
			pin->top->prev->next = NULL;
			pin->top = tmp->prev;
		} else {
			pin->bottom = NULL;
			pin->top = NULL;
		}
		return tmp;
	}
	return NULL;
}

void drawDisk(GLUquadricObj **quadric, const GLfloat outer, const GLfloat inner)
 {
	glPushMatrix();
		glRotatef(-90.0, 1.0, 0.0, 0.0);
		gluCylinder(*quadric, outer, outer, BREITE, SLICES, LOOPS);
		gluQuadricOrientation(*quadric, GLU_INSIDE);
		if(inner > 0)
gluCylinder(*quadric, inner, inner, BREITE, INNERSLICES, LOOPS);
		gluDisk(*quadric, inner, outer, SLICES, LOOPS);
		gluQuadricOrientation(*quadric, GLU_OUTSIDE);
		glTranslatef(0.0, 0.0, BREITE);
		gluDisk(*quadric, inner, outer, SLICES, LOOPS);
		gluQuadricOrientation(*quadric, GLU_OUTSIDE);
	glPopMatrix();
}

void drawPin(GLUquadricObj **quadric, const GLfloat radius, const GLfloat height)
{
	glPushMatrix();
		glRotatef(-90.0, 1.0, 0.0, 0.0);
		gluCylinder(*quadric, radius, radius, BREITE/2, SLICES, LOOPS);
		gluQuadricOrientation(*quadric, GLU_INSIDE);
		gluDisk(*quadric, 0.0, radius, SLICES, LOOPS);
		gluQuadricOrientation(*quadric, GLU_OUTSIDE);
		glTranslatef(0.0, 0.0, BREITE/2);
		gluDisk(*quadric, 0.0, radius, SLICES, LOOPS);
gluCylinder(*quadric, STANGENBREITE, STANGENBREITE, height, INNERSLICES, LOOPS);
		glTranslatef(0.0, 0.0, height);
		gluDisk(*quadric, 0.0, STANGENBREITE, INNERSLICES, LOOPS);
	glPopMatrix();
}

void drawAllPins(GLUquadricObj **quadric, const GLfloat radius, const GLfloat height, const GLfloat gap)
{
	glPushMatrix();
		drawPin(quadric, radius, height);
		glTranslatef(-gap, 0.0, 0.0);
		drawPin(quadric, radius, height);
		glTranslatef(gap*2, 0.0, 0.0);
		drawPin(quadric, radius, height);
	glPopMatrix();
}

void drawBitmapString(const GLfloat x, const GLfloat y, const GLfloat z, void *font, char *string)
{
	char *c;
	glRasterPos3f(x, y, z);
	for (c = string; *c != '\0'; c++)
		glutBitmapCharacter(font, *c);
}

void drawBitmapInt(const GLfloat x, const GLfloat y, const GLfloat z, void *font, const int number)
{
	char string[17];
	sprintf(string, "%d", number);
	drawBitmapString(x, y, z, font, string);
}

void populatePin(void)
{
	int i;
	disk *cur;
	GLfloat radius = 0.1f*disks;
	for(i = 0;i < disks;i++)
	{
		cur = (disk *)malloc(sizeof(disk));
		cur->color = (char)i%6;
		cur->radius = radius;
		push(&pin[0], cur);
		radius -= 0.1;
	}
	duration = 0;
	draw = 0;
}

void clearPins(void)
{
	int i;
	disk *cur, *tmp;
	free(curdisk);
	curdisk = NULL;
	for(i = 0;i < 3;i++)
	{
		cur = pin[i].top;
		while(cur != NULL)
		{
			tmp = cur->prev;
			free(cur);
			cur = tmp;
		}
		pin[i].top = NULL;
		pin[i].bottom = NULL;
	}
}

void hanoiinit(void)
{
	GLfloat radius;
	speed = FSEM*FEM;
	radius = 0.1f*disks;
	config.pinradius = radius+0.1f;
	config.gap = radius*2+0.5f;
	config.pinheight = disks*BREITE+0.2f;
	maxdraws = (2 << (disks-1))-1;   //calculate minimum number of moves
	populatePin();
	/* calculate actions; initialize action list */
	actqueue.head = NULL;
	hanoi(&actqueue, disks, 0, 1, 2);
	curaction = actqueue.head;
	curdisk = pop(&pin[(int)curaction->fromstack]);
	pos = 0.001;
}

void reset(void)
{
	clearPins();
	populatePin();
	/* reset actions */
	curaction = actqueue.head;
	curdisk = pop(&pin[(int)curaction->fromstack]);
	pos = 0.001;

}

void hanoicleanup(void)
{
	action *acur, *atmp;
	clearPins();
	acur = actqueue.head;
	do {
		atmp = acur->next;
		free(acur);
		acur = atmp;
	} while(acur != NULL);
	gluDeleteQuadric(quadric);
}
void setColor(const int color)
{
	switch(color) {
		case 0:
			glColor3f(1.0, 0.0, 0.0);
			break;
		case 1:
			glColor3f(0.0, 1.0, 0.0);
			break;
		case 2:
			glColor3f(0.0, 0.0, 1.0);
			break;
		case 3:
			glColor3f(0.0, 1.0, 1.0);
			break;
		case 4:
			glColor3f(1.0, 0.0, 1.0);
			break;
		case 5:
			glColor3f(0.0, 0.0, 0.0);
			break;
	}
}

void Init(void)
{
	const GLfloat mat_specular[] = { 1.0, 1.0, 1.0, 1.0 };
	const GLfloat mat_shininess[] = { 50.0 };
	const GLfloat light_position[] = { 0.0, 1.0, 1.0, 0.0 };
	glShadeModel(GL_SMOOTH);
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);  /* draw polygons filled */
	glClearColor(1.0, 1.0, 1.0, 1.0);   /* set screen clear color */
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);  /* blending settings */
	glCullFace(GL_BACK);		/* remove backsides */
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
	glLightfv(GL_LIGHT0, GL_POSITION, light_position);
	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);
	glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_DEPTH_TEST);
	quadric = gluNewQuadric();
	gluQuadricNormals(quadric, GLU_SMOOTH);
}

/*Is called if the window size is changed */
void Reshape(int width, int height)
{
	glViewport(0, 0, (GLint) width, (GLint) height);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0, 1.0, 1.0, 75.0);
	glMatrixMode(GL_MODELVIEW);
}

/* react to key presses */
void Key(unsigned char key, int x, int y)
{
	switch(key)
	{
		case 27:
		case 'q':
			exit(EXIT_SUCCESS);
			break;
		case ' ':
			rotX = 0.0;
			rotY = 0.0;
			zoom = 0.0;
			offsetY = 1.5;
			speed = FSEM*FEM;
			break;
		case 'r':
			reset();
			break;
		case 'f':
			if (fullscreen == 0)
			{
				glutFullScreen();
				fullscreen = 1;
			}
			else
			{
				glutReshapeWindow(800, 600);
				glutPositionWindow(50, 50);
				fullscreen = 0;
			}
			break;
	}
	glutPostRedisplay();
}

void SpecialKey(int key, int x, int y)
{
	switch(key)
	{
		case GLUT_KEY_UP:
			rotX -= 5;
			break;
		case GLUT_KEY_DOWN:
			rotX += 5;
			break;
		case GLUT_KEY_LEFT:
			rotY -= 5;
			break;
		case GLUT_KEY_RIGHT:
			rotY += 5;
			break;
	}
	glutPostRedisplay();
}

void
mouse(int button, int state, int x, int y)
{

  if (button==GLUT_LEFT_BUTTON && state == GLUT_DOWN)
  {
			zoom += 0.1;
  }
  if (button==GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
		zoom -= 0.1;
  if (button==GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
		reset();


  }

void Display(void)
{
	disk *cur;
	int i;
	GLfloat movY;
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); /* clear scren */
	glLoadIdentity();
	glColor3f(0.0, 0.0, 0.0);
	drawBitmapString(25.0, 32.0, -60.0, GLUT_BITMAP_9_BY_15, seconds);
	drawBitmapInt(25.0, 30.0, -60.0, GLUT_BITMAP_9_BY_15, draw);
	drawBitmapInt(28.0, 30.0, -60.0, GLUT_BITMAP_9_BY_15, maxdraws);
	drawBitmapString(-32.0, 30.0, -60.0, GLUT_BITMAP_9_BY_15, "Controls:");
	drawBitmapString(-32.0, 28.0, -60.0, GLUT_BITMAP_9_BY_15, "f : fullscreen");
drawBitmapString(-32.0, 26.0, -60.0, GLUT_BITMAP_9_BY_15, "r : restart animation");
	drawBitmapString(-32.0, 24.0, -60.0, GLUT_BITMAP_9_BY_15, "q/Esc : quit");
drawBitmapString(-32.0, 22.0, -60.0, GLUT_BITMAP_9_BY_15, "Use the arrow keys to rotate the view");
	gluLookAt(0.0, 0.9, 3.6+zoom, 0.0, offsetY, 0.0, 0.0, 1.0, 0.0); // calculate view point
	glRotatef(rotY, 0.0, 1.0, 0.0);	 /* rotate Y axis */
	glRotatef(rotX, 1.0, 0.0, 0.0);	 /* rotate X axis */
	glColor3f(0.0, 0.0, 0.0);
	drawAllPins(&quadric, config.pinradius, config.pinheight, config.gap); // draw pins
	glTranslatef(-config.gap, BREITE/2, 0.0);
	glPushMatrix();
	for(i = 0; i < 3; i++)
	{ /* fill pins with disks */
		glPushMatrix();
		pinheight[i] = 0;
		if((cur = pin[i].bottom) != NULL)
		{
			do {
				setColor(cur->color);
				drawDisk(&quadric, cur->radius, STANGENBREITE);
				glTranslatef(0.0, BREITE, 0.0);
				pinheight[i] += BREITE;
				cur = cur->next;
			} while(cur != NULL);
		}
		glPopMatrix();
		glTranslatef(config.gap, 0.0, 0.0);
	}
	glPopMatrix();
	if(curaction != NULL && curaction->fromstack != -1 && curdisk != NULL) {
		if(pos <= 1.0)
		{
			movY = pos*(config.pinheight-pinheight[(int)curaction->fromstack]);
glTranslatef(config.gap*curaction->fromstack, pinheight[(int)curaction->fromstack]+movY, 0.0);
		}
		else
		{
			if(pos < 2.0 && curaction->fromstack != curaction->tostack)
			{
				if(curaction->fromstack != 1 && curaction->tostack != 1)
				{ /* jump 2 pins */
					glTranslatef(config.gap, config.pinheight+0.05f, 0.0);
					if(curaction->fromstack == 0)
						glRotatef(-(pos-2.0f)*180-90, 0.0, 0.0, 1.0);
					else
						glRotatef((pos-2.0f)*180+90, 0.0, 0.0, 1.0);
					glTranslatef(0.0, config.gap, 0.0);
				}
				else
				{
				         if(curaction->fromstack == 0&&curaction->tostack == 1)
					{
glTranslatef(config.gap/2, config.pinheight+0.05f, 0.0);
						glRotatef(-(pos-2.0f)*180-90, 0.0, 0.0, 1.0);
					}
					else
					{
if(curaction->fromstack == 2 && curaction-> tostack == 1)
						{
glTranslatef(config.gap/2*3, config.pinheight+0.05f, 0.0);
glRotatef((pos-2.0f)*180+90, 0.0, 0.0, 1.0);
						}
						else
						{
if(curaction->fromstack == 1 && curaction->tostack == 2)
							{
glTranslatef(config.gap/2*3, config.pinheight+0.05f, 0.0);
glRotatef(-(pos-2.0f)*180-90, 0.0, 0.0, 1.0);
							}
							else
							{
glTranslatef(config.gap/2, config.pinheight+0.05f, 0.0);
glRotatef((pos-2.0f)*180+90, 0.0, 0.0, 1.0);
							}
						}
					}
					glTranslatef(0.0, config.gap/2, 0.0);
				}
				glRotatef(-90, 0.0, 0.0, 1.0);
			}
			else
				if(pos >= 2.0)
				{ /* drop disk down */
movY = config.pinheight-(pos-2.0f+speed)* (config.pinheight-pinheight[(int)curaction->tostack]);
glTranslatef(config.gap*curaction->tostack, movY, 0.0);
				}
		}
		setColor(curdisk->color);
		drawDisk(&quadric, curdisk->radius, STANGENBREITE);
	}
	glutSwapBuffers(); /* swap buffers (double buffering) */
}
void moveDisk(int param)
{
	if(param == 1)
		reset();
	if(curaction != NULL)
	{
		if(pos == 0.0 || pos >= 3.0-speed)
		{ /* 0--1 -> disk goes upwards, 1--2 "disk in air", 2--3 disk goes downwards*/
			pos = 0.0;
			draw++;
			push(&pin[(int)curaction->tostack], curdisk);
			curaction = curaction->next;
			if(curaction != NULL)
				curdisk = pop(&pin[(int)curaction->fromstack]);
		}
		pos += speed;
		if(pos > 3.0-FSEM)
			pos = 3.0-FSEM;
      glutTimerFunc((unsigned)FEM, moveDisk, 0);
	}
	else
	{
		curdisk = NULL;
		glutTimerFunc(5000, moveDisk, 1);
	}
	glutPostRedisplay();
}

void timer(int param)
{
	if(curaction != NULL)
	{
		printf(seconds, "Time: %ds", ++duration);
	}
	glutTimerFunc(1000, timer, 0);
}

int main(int argc, char *argv[])
{
	hanoiinit();
	atexit(hanoicleanup);
	glutInit(&argc, argv);
	//command line arguments for setting the number of disks
	if(argc>1)
		disks=(int)argv[1];
	glutInitWindowPosition(0, 0);
	glutInitWindowSize(800, 600);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE);
	if(glutCreateWindow("Towers of Hanoi Puzzle Simulation") == GL_FALSE)
		exit(EXIT_FAILURE);
	Init();
	glutReshapeFunc(Reshape);
	glutKeyboardFunc(Key);
	glutSpecialFunc(SpecialKey);
	glutMouseFunc(mouse);
	glutDisplayFunc(Display);
	glutTimerFunc((unsigned)FEM, moveDisk, 0);
	glutTimerFunc(1000, timer, 0);
	glutMainLoop();
	return EXIT_SUCCESS;
}
