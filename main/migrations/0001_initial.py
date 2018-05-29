# Generated by Django 2.0.5 on 2018-05-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profbody', models.CharField(max_length=50, verbose_name='body')),
                ('grade', models.CharField(max_length=50, verbose_name='grade')),
                ('no_member', models.CharField(max_length=50, verbose_name='members')),
                ('year_selection', models.CharField(max_length=50, verbose_name='year selection')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Spec_awards_particulars', models.CharField(max_length=50, verbose_name='Particulars')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('national', models.CharField(max_length=50, verbose_name='National')),
                ('international', models.CharField(max_length=50, verbose_name='International')),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neft', models.CharField(max_length=50, verbose_name='NEFT')),
                ('uti', models.CharField(max_length=35, verbose_name='UTI')),
                ('Date', models.CharField(max_length=35, verbose_name='Date')),
                ('Amount', models.CharField(max_length=35, verbose_name='Amount')),
                ('Bank', models.CharField(max_length=35, verbose_name='Bank')),
                ('Branch', models.CharField(max_length=35, verbose_name='Branch')),
            ],
        ),
        migrations.CreateModel(
            name='BE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bsc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conf_conducted_org', models.CharField(max_length=50, verbose_name='organisation')),
                ('total_experience', models.CharField(max_length=50, verbose_name='experience')),
                ('university', models.CharField(max_length=50, verbose_name='university')),
                ('designation', models.CharField(max_length=50, verbose_name='designationsi')),
                ('from_date', models.CharField(max_length=50, verbose_name='from')),
                ('to_date', models.CharField(max_length=50, verbose_name='to')),
                ('total_duration', models.CharField(max_length=50, verbose_name='total duration')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('fathers_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('permanent_address', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('date_of_birth', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('reservation', models.CharField(max_length=50)),
                ('family_members', models.IntegerField()),
                ('Affiliation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Affiliation')),
                ('Awards', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Awards')),
                ('BE', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.BE')),
                ('BankDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.BankDetails')),
                ('Bsc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Bsc')),
                ('Conference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='IndustrialExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=50, verbose_name='organisation')),
                ('position_held', models.CharField(max_length=50, verbose_name='position held')),
                ('from_date', models.CharField(max_length=50, verbose_name='from date')),
                ('to_date', models.CharField(max_length=50, verbose_name='to date')),
                ('experience_years', models.CharField(max_length=50, verbose_name='experience years')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.CharField(max_length=50, verbose_name='proficiency')),
            ],
        ),
        migrations.CreateModel(
            name='MphilMca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PHD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=50)),
                ('Specialisation', models.CharField(max_length=50)),
                ('Institution_Name', models.CharField(max_length=50)),
                ('Passing_Year', models.CharField(max_length=50)),
                ('Percent_Marks', models.CharField(max_length=50)),
                ('Class_Awarded', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('contact_no', models.CharField(max_length=50, verbose_name='contact no')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_researchExp', models.CharField(max_length=50)),
                ('Name_university', models.CharField(max_length=50)),
                ('area_reasearch', models.CharField(max_length=50)),
                ('from_date', models.CharField(max_length=50)),
                ('to_date', models.CharField(max_length=50)),
                ('total_duration', models.CharField(max_length=50)),
                ('total_internationalConf', models.CharField(max_length=50)),
                ('title_paper', models.CharField(max_length=50)),
                ('conf_International', models.CharField(max_length=50)),
                ('year_month_pub', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='English',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='english', to='main.Languages'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Hindi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hindi', to='main.Languages'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='IndustrialExperience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.IndustrialExperience'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Kannada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kannada', to='main.Languages'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='MTech',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.MTech'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='MphilMca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.MphilMca'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='OtherCourse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.OtherCourse'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='PHD',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.PHD'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Referral',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Referral'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='Research',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Research'),
        ),
    ]
