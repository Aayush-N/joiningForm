

<!DOCTYPE html>
<html>
   <head>
      <meta charset="utf-8"/>
      <style type="text/css">
         *{-moz-box-sizing:border-box;box-sizing:border-box}body,div,form,h1,h2,h4,html,label,p,span,table{margin:1;margin-left:60;padding:0;border:0;font:inherit;vertical-align:baseline}header{margin-bottom:30px}header .gnb{height:90px;width:990px;margin:auto;color:#707070 ;padding-top:34px}header .gnb .nLogo{width:237px;float:left}header .gnb p{float:right;width:auto;max-width:400px;word-break:break-all}header .gnb .primary-link.skip{float:right;font-weight:400;font-size:18px}header .gnb .underline{text-decoration:underline}header .banner{background: no-repeat #000;height:60px;color:#fff;text-align:center}header .banner .title{font-size:16px;padding-top:10px}header .banner .msg{font-size:19px;padding-top:2px;font-weight:400}footer{text-align:center;font-size:12px;margin-bottom:30px;margin-top:65px}footer a{color:#27a7d4 ;display:inline-block;font-size:12px;line-height:1;padding:0 10px;border-left:solid 1px #a7a7a7 }footer a:hover{color:#0f89b2 }footer a:first-child{border-left:none}footer p{color:#a7a7a7 ;margin-top:5px}body{font-family:Roboto,sans-serif;font-size:15px;font-weight:100;background-color:white; }.wrap{width:990px;margin:0 auto}main{text-align:center;display:block}.view-container{position:relative;min-height:500px}.view-container>.view.ng-animate{position:absolute;top:0;left:0;width:100%;min-height:500px}
      </style>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
      <title>Teaching</title>
   </head>
   <body class="col-md-12">
      <p style="text-align: center;"><strong></strong><img src="https://bmsit.ac.in/assets/logo-167a1e45069e8f279b09630a9bff0d35e6cba7f016a24651e39a40dc422e9dc1.png"width="70" height="70"></strong></p>
      <a style=" margin-left: 950px;" href="http://localhost/faculty/AdminLogin.php">Admin Login</a> 
      <!--
         <button style=" margin-left: 1000px;" class="button" onClick="window.open('http://www.site.com');"><span class="icon" ><center>  Login </center> </span></button>
         -->
      <p style="text-align: center;"><strong>BMS INSTITUTE OF TECHNOLOGY & MANAGEMENT</strong></p>
      <p style="text-align: center;">Yelahanka, Bangaluru-560064 / Approved by AICTE / Accredited by NBA</p>
      <h2 style="text-align: center;">APPLICATION FOR FACULTY POSITION</h2>
      <form name="teaching" action="DB_values.php" onsubmit="window.alert("submit"); method=POST>

         <p><strong>&nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;</strong></p>
         <p style="text-align: center;">
            Application for the Position   &nbsp;&nbsp;
            <select name="position" id="position" type="text" >
               <option value="Professor">Professor</option>
               <option value="Assoc. Professor">Assoc. Professor</option>
               <option value="Asst. Professor">Asst. Professor</option>
            </select>
         </p>
         <p style="text-align: center;">
            Department:
            <select name="department" id="department"  type="text" >
               <option value="ece">ECE</option>
               <option value="cse">CSE</option>
               <option value="ise">ISE</option>
               <option value="me">EEE</option>
               <option value="civ">TCE</option>
               <option value="mca">CVIL</option>
               <option value="eee">MCA</option>
               <option value="mtech">MTECH</option>
            </select>
         </p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
<table style="margin-left: auto; margin-right: auto; border-collapse: collapse;" border="1">
         <div class="form-group">
            <label for="name">1. Name in Full (In capital Letters only)</label>
            <input class="form-control" type="text" name="name" id="name"  type="text" style="width:245px;padding: 3px;" maxlength="200" />
         </div>
         <div class="form-group">
            <label for="father">2. Father&rsquo;s Name &amp; Occupation</label>
            <input class="form-control" type="text" name="father" id="father"  type="text" style="width:245px;;padding: 3px;" maxlength="200" />
         </div>
         <div class="form-group">
            <label>3. Address for Correspondence</label>
            <input class="form-control" type="text" name="address" id="address" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>4. Permanent Address</label>
            <input class="form-control" type="text" name="permanent" id="permanent" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>5. Contact Numbers</label>
            <input class="form-control" type="number" name="phone" id="phone" required="" type="number" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>6. Email ID</label>
            <input class="form-control" type="email" name="email" id="email" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>7. Date of Birth</label>
            <input class="form-control" type="date" name="dateofbirth" id="dateofbirth" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>8. Age as on the last date of submission of application</label>
            <input class="form-control" type="number" name="age" id="age" required="" type="number" style="width:145px;" maxlength="2" />
         </div>
         <div class="form-group">
            <label>9. Place of Birth</label>
            <input class="form-control" type="text" name="place" id="place" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
            <label>10. Religion</label>
            <input class="form-control" type="text" name="religion" id="religion" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
         <label>11. Reservation Category (Enclose copies of Certificate issued by competent authority)</label>
         <input class="form-control" type="text" name="reservation" id="reservation" required="" type="text" style="width:245px;" maxlength="50" /> </div>
         <div class="form-group">
            <label>12. Any Member of the family Presently an employee of BMSIT (If yes, provide details)</label>
	<input class="form-control" type="text" name="familyMember" id="familyMember" required="" type="text" style="width:245px;" maxlength="50" />
         </div>
         <div class="form-group">
         <label>Read</label>
         <p style="text-align: left;"><strong>Write</strong></p>
         <p style="text-align: left;"><strong>Speak</strong></p>
         <td width="210">
            <select name="languages_known">
            <option value="Kannada">Kannada</option>
            <option value="English">English</option>
            <option value="Hindi">Hindi</option>
         </td>
         <td width="137">
            <select name="to_read">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
         </td>
         <td width="184">
            <select name="to_speak">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
         </td>
         <td width="191">
            <select name="to_write">
            <option value="Yes">Yes</option>
            <option value="No">No</option>
         </td>
         </tr>
         <tr>
            <td width="210">
               <select name="languages_known1">
               <option value="Kannada">Kannada</option>
               <option value="English">English</option>
               <option value="Hindi">Hindi</option>
            </td>
            <td width="137">
               <select name="to_read1">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
            <td width="184">
               <select name="to_speak1">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
            <td width="191">
               <select name="to_write1">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
         </tr>
         <tr>
            <td width="210">
               <select name="languages_known2">
               <option value="Kannada">Kannada</option>
               <option value="English">English</option>
               <option value="Hindi">Hindi</option>
            </td>
            <td width="137">
               <select name="to_read2">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
            <td width="184">
               <select name="to_speak2">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
            <td width="191">
               <select name="to_write2">
               <option value="Yes">Yes</option>
               <option value="No">No</option>
            </td>
         </tr>
         </tbody>
         </table>
         <p>&nbsp;</p>
         <table style="margin-left: auto; margin-right: auto; border-collapse: collapse;" border="1">
            <tbody>
               <tr>
                  <td colspan="7" width="150">
                     <p style="margin-left: 5px;"><strong>14. Highest Educational Qualification</strong></p>
                  </td>
                  <td colspan="12" width="242"><input type="text"  name="qualification" id="qualification" required="" type="text" style="width:140px;" maxlength="50">
                  </td>
               </tr>
               <tr>
                  <td colspan="18" width="150">
                     <p style="text-align: center;"><strong>Details of Educational Qualification</strong></p>
                  </td>
               </tr>
               <tr>
                  <td colspan="0" width="10">
                     <p style="margin-left: 5px;">Degree</p>
                  </td>
                  <td colspan="3" width="66">
                     <p style="text-align: left;">Course</p>
                  </td>
                  <td colspan="3" width="66">
                     <p style="margin-left: 5px;">Specialization</p>
                  </td>
                  <td colspan="3" width="66">
                     <p style="margin-left: 3px;">Name of the Institution</p>
                  </td>
                  <td colspan="3" width="66">
                     <p style="margin-left: 3px;">Year of Passing</p>
                  </td>
                  <td colspan="4" width="66">
                     <p style="margin-left: 5px;">Percentage of Marks</p>
                  </td>
                  <td colspan="1" width="66">
                     <p style="margin-left: 3px;">Class</p>
                     <p style="margin-left: 3px;">Awarded</p>
                  </td>
               </tr>
               <tr>
                  <td colspan="0" width="16">
                     <p style="margin-left: 5px;">PhD</p>
                  <td colspan="3" width="25"><input type="text"  name="PhD_Course" id="PhD_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="25"><input type="text"  name="PhD_Specialisation" id="PhD_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="25"><input type="text"  name="PhD_Institution_Name" id="PhD_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="25"><input type="text"  name="PhD_Passing_Year" id="PhD_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="25"><input type="text"  name="PhD_Percent_Marks" id="PhD_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="76"><input type="text"  name="PhD_Class_Awarded" id="PhD_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               </tr>
               <tr>
                  <td colspan="18" width="275">
                     <p style="text-align: center;"><strong>POST GRADUATION (PG)</strong></p>
                  </td>
               </tr>
               <tr>
                  <td width="">
                     <p style="margin-left: 5px;">ME / M Tech</p>
                  <td colspan="3" width="66"><input type="text"  name="ME_Mtech_Course" id="ME_Mtech_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="ME_Mtech_Specialisation" id="ME_Mtech_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="ME_Mtech_Institution_Name" id="ME_Mtech_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="ME_Mtech_Passing_Year" id="ME_Mtech_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="66"><input type="text"  name="ME_Mtech_Percent_Marks" id="ME_Mtech_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="76"><input type="text" name="ME_Mtech_Class_Awarded" id="ME_Mtech_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               </tr>
               <tr>
                  <td width="167">
                     <p style="margin-left: 5px;">M.Phil/M.Sc./MCA</p>
                  <td colspan="3" width="66"><input type="text"  name="Mphil_mca_Course" id="Mphil_mca_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="Mphil_mca_Specialisation" id="Mphil_mca_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="Mphil_mca_Institution_Name" id="Mphil_mca_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text" name="Mphil_mca_Passing_Year" id="Mphil_mca_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="66"><input type="text" name="Mphil_mca_Percent_Marks" id="Mphil_mca_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="76"><input type="text" name="Mphil_mca_Class_Awarded" id="Mphil_mca_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               <tr>
                  <td colspan="18" width="375">
                     <p style="text-align: center;"><strong>UNDER GRADUATION (UG)</strong></p>
                  </td>
               </tr>
               <tr>
                  <td width="167">
                     <p style="margin-left: 5px;">BE/B.Tech</p>
                  <td colspan="3" width="66"><input type="text"  name="BE_Btech_Course" id="BE_Btech_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="BE_Btech_Specialisation" id="BE_Btech_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="BE_Btech_Institution_Name" id="BE_Btech_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text" name="BE_Btech_Passing_Year" id="BE_Btech_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="66"><input type="text"  name="BE_Btech_Percent_Marks" id="BE_Btech_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="76"><input type="text" name="BE_Btech_Class_Awarded" id="BE_Btech_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               </tr>
               <tr>
                  <td width="167">
                     <p style="margin-left: 5px;">B. Sc</p>
                  </td>
                  <td colspan="3" width="66"><input type="text"  name="Bsc_Course" id="Bsc_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="Bsc_Specialisation" id="Bsc_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="Bsc_Institution_Name" id="Bsc_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="Bsc_Passing_Year" id="Bsc_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="66"><input type="text"  name="Bsc_Percent_Marks" id="Bsc_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="66"><input type="text"  name="Bsc_Class_Awarded" id="Bsc_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               <tr>
                  <td width="167">
                     <p style="margin-left: 5px;">Other</p>
                  </td>
                  <td colspan="3" width="66"><input type="text"  name="others_Course" id="others_Course" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="others_Specialisation" id="others_Specialisation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="others_Institution_Name" id="others_Institution_Name" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="3" width="66"><input type="text"  name="others_Passing_Year" id="others_Passing_Year" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="4" width="66"><input type="text"  name="others_Percent_Marks" id="others_Percent_Marks" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  <td colspan="1" width="76"><input type="text"   name="others_Class_Awarded" id="others_Class_Awarded" required="" type="text" style="width:140px;" maxlength="50" /></td>
               </tr>
               </tr>
               </td>
               </tr>
               </td>
               </tr>
               </td>
               </tr>
               </td>
               </tr>
            </tbody>
         </table>
         <p style="margin-left: 5px;"><strong>15. Total No. of years of Research Experience</strong></p>
         <input type="text"  name="total_researchExp" id="total_researchExp" required="" type="text" style="width:140px;" maxlength="50" /></td>
         <p style="margin-left: 5px;">Details ( Use separate if required)</p>
         <table class="table table-bordered" id="myTable">
            <tr>
               <th>Name of the University / Institution</th>
               <th>Area of Research</th>
               <th>From</th>
               <th>To</th>
               <th>Total</th>
               <th></th>
            </tr>
            <tr>
               <td><input type="text"  name="Name_university" id="Name_university" required="" type="text" style="width:140px;" maxlength="50" /></td>
               <td>
                  <input type="3ext"  name="area_reasearch" id="area_reasearch" required="" type="text" style="width:140px;" maxlength="50" />
               </td>
               <td>
                  <input type="text"  name="research_from" id="research_from" required="" type="text" style="width:140px;" maxlength="50" />
               </td>
               <td>
                  <input type="text"  name="research_to" id="research_to" required="" type="text" style="width:140px;" maxlength="50" />
               </td>
               <td>
                  <input type="text"  name="research_total" id="research_total" required="" type="text" style="width:140px;" maxlength="50" />
               </td>
               <td><input type="button"  name="add_row" id="add_row" required="" type="text" style="width:140px;" maxlength="50" type="button" value="Add row"  onclick="addField();"/></td>
            </tr>
         </table>
         <tr>
            <td colspan="18" width="275">
               <p style="text-align: center;"><strong>
            </td>
         </tr>
         <tr>
            <td colspan="18" width="475">
               <p style="margin-left: 5px;"><strong>16. Total No. of Publications ( National &amp; International Journals, Conferences and Books with ISBN Number&nbsp; if any) </strong></p6>
                  <input type="text" name="total_internationalConf" id="total_internationalConf" required="" type="text" style="width:140px;" maxlength="50" />
               <p style="margin-left: 5px;">For details of Publications (Please attach separate sheet giving details of journal/ impact factors and citations from Google scholar, Scopus and web of science)</p>
               <table id="myTable1" class="table table-bordered">
                  <tr>
                     <th>Title of the Paper</th>
                     <th>International Conference</th>
                     <th>Year and Month of Publication</th>
                     <th>Organization which conducted it</th>
                     <th></th>
                  </tr>
                  <tr>
                     <td><input type="text"  name="title_paper" id="title_paper" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="conf_International" id="conf_International" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="year_month_pub" id="year_month_pub" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="conf_conducted_org" id="conf_conducted_org" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="button"  name="add_row" id="add_row" required="" type="text" style="width:140px;" maxlength="50" type="button" value="Add row"  onclick="addField1();"/></td>
                  </tr>
               </table>
               <p style="margin-left: 5px;"><strong>17. Total No. of Teaching Experience</strong></p>
               <input type="text"  name="teaching_totalExp" id="teaching_totalExp" required="" type="text" style="width:140px;" maxlength="50" />
               <p style="margin-left: 5px;">Details Teaching Experience</p>
               <table class="table table-bordered">
                  <tr>
                     <th>Name of the University / Institution</th>
                     <th>Designation</th>
                     <th>From</th>
                     <th>To</th>
                     <th>Total</th>
                  </tr>
                  <tr>
                     <td><input type="text"  name="teaching_university" id="teaching_university" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="teaching_designation" id="teaching_designation" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="teaching_from" id="teaching_from" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="teaching_to" id="teaching_to" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td><input type="text"  name="teaching_total" id="teaching_total" required="" type="text" style="width:140px;" maxlength="50" /></td>
                  </tr>
                  <tr>
                     <td><input type="text"  name="teaching_university" id="teaching_university" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="teaching_designation" id="teaching_designation" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_from" id="teaching_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_total" id="teaching_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_total" id="teaching_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td><input type="text"  name="teaching_university" id="teaching_university" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="teaching_designation" id="teaching_designation" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_from" id="teaching_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_to" id="teaching_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_total" id="teaching_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td><input type="text"  name="teaching_university" id="teaching_university" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="teaching_designation" id="teaching_designation" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_from" id="teaching_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_to" id="teaching_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="teaching_total" id="teaching_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
               </table>
               <p style="margin-left: 5px;"><strong>18. Total No. of Industrial Experience</strong></p>
               <input type="text"  name="total_industrialExp" id="total_industrialExp" required="" type="text" style="width:140px;" maxlength="50" />
               <p style="margin-left: 5px;">Details Industrial Experience</p>
               <table class="table table-bordered">
                  <tr>
                     <th>Name of the Organization</th>
                     <th>Position Held</th>
                     <th>From</th>
                     <th>To</th>
                     <th>Total</th>
                  </tr>
                  <tr>
                     <td><input type="text"  name="industrial_org" id="industrial_org" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="industrial_positionheld" id="industrial_positionheld" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_from" id="industrial_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_to" id="industrial_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_total" id="industrial_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td><input type="text"  name="industrial_org" id="industrial_org" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="industrial_positionheld" id="industrial_positionheld" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_from" id="industrial_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_to" id="industrial_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_total" id="industrial_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td><input type="text"  name="industrial_org" id="industrial_org" required="" type="text" style="width:140px;" maxlength="50" /></td>
                     <td>
                        <input type="text"  name="industrial_positionheld" id="industrial_positionheld" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_from" id="industrial_from" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_to" id="industrial_to" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="industrial_total" id="industrial_total" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
               </table>
               <p style="margin-left: 5px;"><strong>19. Affiliation to Professional Organisation </strong></p6>
               <table class="table table-bordered">
                  <tr>
                     <th>Name of the Professional Body</th>
                     <th>Grade of the Membership</th>
                     <th>Number of Membership</th>
                     <th>Year of Selection</th>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Affiliation_profbody" id="Affiliation_profbody" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_grade" id="Affiliation_grade" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_no_member" id="Affiliation_no_member" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_year_selection" id="Affiliation_year_selection" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Affiliation_profbody" id="Affiliation_profbody" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_grade" id="Affiliation_grade" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_no_member" id="Affiliation_no_member" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_year_selection" id="Affiliation_year_selection" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Affiliation_profbody" id="Affiliation_profbody" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_grade" id="Affiliation_grade" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_no_member" id="Affiliation_no_member" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Affiliation_year_selection" id="Affiliation_year_selection" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  </tr>
               </table>
               <p>
                  <strong>
               <p style="margin-left: 5px;">20. Special Award / Achievements or any other information :</strong></p>
               <table class="table table-bordered">
                  <tr>
                     <th>Name of the Professional Body</th>
                     <th>Grade of the Membership</th>
                     <th>Number of Membership</th>
                     <th>Year of Selection</th>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Spec_awards_particulars" id="Spec_awards_particulars" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_state" id="awards_state" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_national" id="awards_national" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_intnational" id="awards_intnational" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Spec_awards_particulars" id="Spec_awards_particulars" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_state" id="awards_state" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_national" id="awards_national" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_intnational" id="awards_intnational" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="Spec_awards_particulars" id="Spec_awards_particulars" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_state" id="awards_state" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_national" id="awards_national" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="awards_intnational" id="awards_intnational" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
               </table>
               <p>
                  <strong>
               <p style="margin-left: 5px;">21.&nbsp; Details of the References</strong></p>
               <table class="table table-bordered">
                  <tr>
                     <th>Name</th>
                     <th>Occupation or Position</th>
                     <th>Address for Communication with Contact Number</th>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="ref_name" id="ref_name" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="ref_position" id="ref_position" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="ref_add_contactNo" id="ref_add_contactNo" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
                  <tr>
                     <td>
                        <input type="text"  name="ref_name" id="ref_name" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="ref_position" id="ref_position" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="ref_add_contactNo" id="ref_add_contactNo" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
               </table>
              <p style="margin-left: 5px;">21.&nbsp;<strong>Details of Fee Paid</strong></p>
               <table class="table table-bordered">
                  <tr>
                     <th>NEFT</th>
                     <th>UTR No.</th>
                     <th>Date</th>
                     <th>Amount</th>
                     <th>Bank</th>
                     <th>Branch Name</th>
                  </tr>
                  <tr>
                     <td>
                        <input type="number"  name="neft" id="neft" required="" type="number" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="number"  name="uti" id="uti" required="" type="number" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="date"  name="Date" id="Date" required="" type="date" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Amount" id="Amount" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Bank" id="Bank" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                     <td>
                        <input type="text"  name="Branch" id="Branch" required="" type="text" style="width:140px;" maxlength="50" />
                     </td>
                  </tr>
               </table>
               <p>&nbsp;</p>
               <p>&nbsp;</p>
         <tr>
    <td colspan="18" width="775">
       <p style="margin-left: 5px;"><strong>22. List of documents to be attached with the application</strong></p>
    </td>
 </tr>
 <tr>
    <td colspan="10" rowspan="2" width="339">
       <p style="text-align: center;">Title of the document</p>
    </td>
 <tr>
    <td colspan="8" width="153">
       <p style="margin-left: 5px;;">Upload</p>
    </td>
 <tr>
<td colspan="10" width="339">
	<p style="text-align: center;">SSLC Marks Card or age proof document</p>
</td>
            <!--form name="fileupload" action="file_upload.php" method="post" enctype="multipart/form-data"-->
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Bachelors Degree Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Bachelors Degree Marks cards</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Masters Degree Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Masters Degree Marks cards</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Ph.D. Degree Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Other Certificates ( Please Specify)</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Research Experience Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Teaching Experience Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Industrial Experience Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Research Publications/ Papers</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Professional Membership Certificate</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Copy of Aadhar card</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="10" width="339">
               <p style="text-align: center;">Copy of PAN card</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         <tr>
            <td colspan="4" width="339">
               <p style="text-align: center;">Reference Letters</p>
            </td>
            <td colspan="8" width="339"><label style="  font: bold 11px Arial;  text-decoration: none;  background-color: #EEEEEE;  color: #333333;
               padding: 2px 6px 2px 6px; border-top: 1px solid #CCCCCC;  border-right: 1px solid #333333;  border-bottom: 1px solid #333333;
               border-left: 1px solid #CCCCCC;" for="myImage">Upload</label>
               <input style="display:none;" type="file" value="upload" name="myImage" id="myImage" required="" type="text" accept="image/jpg,image/jpeg,image/png,image/gif," />
            </td>
         </tr>
         </tr>
         <tr>
            <td colspan="20" align="center" valign="top"><input type="reset" name="reset" id="reset" value="Reset" class="button gray" />
               <input type="submit" name="submit" id="sends" value="Submit" class="button rosy"/>
            </td>
         </tr>
         </table>
         </tbody>
         </table>
      </form>
   </body>
</html>
<script>
   function addField (argument) {
       var myTable = document.getElementById("myTable");
       var currentIndex = myTable.rows.length;
       var currentRow = myTable.insertRow(-1);
   
       var university = document.createElement("input");
       university.setAttribute("name", "Name_university" + currentIndex);
     university.setAttribute("style", "width:140px");
   
       var area = document.createElement("input");
       area.setAttribute("name", "area_research" + currentIndex);
   area.setAttribute("style", "width:140px");
   
       var research_to = document.createElement("input");
       research_to.setAttribute("name", "research_to" + currentIndex);
   research_to.setAttribute("style", "width:140px");
     
     var research_from = document.createElement("input");
       research_from.setAttribute("name", "research_from" + currentIndex);
   research_from.setAttribute("style", "width:140px");
   
     var research_total = document.createElement("input");
       research_total.setAttribute("name", "research_total" + currentIndex);
   research_total.setAttribute("style", "width:140px");
   
       var addRowBox = document.createElement("input");
       addRowBox.setAttribute("type", "button");
       addRowBox.setAttribute("value", "Add another line");
       addRowBox.setAttribute("onclick", "addField();");
       addRowBox.setAttribute("class", "button");
   
       var currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(university);
   
       currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(area);
   
       currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(research_to);
   
     currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(research_from);
   
     currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(research_total);
   
     currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(add_row);
     }
   
   function addField1() {
   	var myTable = document.getElementById("myTable1");
       var currentIndex = myTable.rows.length;
       var currentRow = myTable.insertRow(-1);
   
       var title_paper = document.createElement("input");
       title_paper.setAttribute("name", "title_paper" + currentIndex);
     title_paper.setAttribute("style", "width:140px");
   
       var conf_International = document.createElement("input");
       conf_International.setAttribute("name", "conf_International" + currentIndex);
   conf_International.setAttribute("style", "width:140px");
   
       var year = document.createElement("input");
       year.setAttribute("name", "year_month_pub" + currentIndex);
   year.setAttribute("style", "width:140px");
     
     var conf = document.createElement("input");
       conf.setAttribute("name", "conf_conducted_org" + currentIndex);
   conf.setAttribute("style", "width:140px");
   
       var addRowBox = document.createElement("input");
       addRowBox.setAttribute("type", "button");
       addRowBox.setAttribute("value", "Add another line");
       addRowBox.setAttribute("onclick", "addField1();");
       addRowBox.setAttribute("class", "button");
   
       var currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(title_paper);
   
       currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(conf_International);
   
       currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(year);
   
     currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(conf);
   currentCell = currentRow.insertCell(-1);
       currentCell.appendChild(add_row);
   }
</script>
