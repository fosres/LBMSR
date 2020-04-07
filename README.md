# City of Lubbock

## Solid Waste Management

Welcome to The City of Lubbock Solid Waste Management site. At this new website you may submit reports and/or requests about how your trash is managed. You may also use this site to view if your trash has been picked for this week.

To submit a service request, follow the instructions below:

<html>
<body>

<h2>Enter Your First and Last Name</h2>

<form>
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
</form>

<h2>Enter Your Six Digit Code</h2>
<form>
  <label for="six digit code">Six Digit Code:</label><br>
  <input type="password" id="six digit code" name="six digit code" value="123456"><br><br>
</form>

<h2>Enter Your Service Request</h2>
<form>
  <label for="lname">Type your issue with your trash bin below:</label><br>
  <input type="text" id="lname" name="lname" value="QR Code ripped off."><br><br>
  <input type="submit" value="Submit">
</form> 

<h2>(Optional): Upload Images of Trash Bin</h2>
<form action="/action_page.php">
	<input type="file" id="myFile" name="filename">
	<input type="submit">
</form> 


<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

</body>
</html>

<html>
<body>
<script src="best.js">
</script>
</body>
</html>

<html>
   <head>

      <script type = "text/javascript">
      	
      </script>
   </head>

   <body>
      <div id = "status" name = "status">Status Message</div>
   </body>
</html>

<html>
<head>
<title>Test Input </title>
<script LANGUAGE="JavaScript">
function readText (form) {
    TestVar =form.inputbox.value;
    alert ("You typed: " + TestVar);
}
function writeText (form) {
    form.inputbox.value = "Have a nice day!"
}
function test(form)								{
         var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
         
	 var bins = document.testform.bin_number.value;

	 var crypto = document.testform.six_digit_code.value;

         var service = document.testform.service_request.value;

         db.transaction(function (tx) {
           
            tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique,code,request TEXT)');
            tx.executeSql('INSERT INTO LOGS (id,code,request) VALUES (?,?,?)',[bins,crypto,service]);
            tx.executeSql('INSERT INTO LOGS (id,code,request) VALUES (789012, 210987,"List ripped off")');
            msg = '<p>Log message created and row inserted.</p>';
            document.querySelector('#status').innerHTML =  msg;
         })

         db.transaction(function (tx) {
            tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
               var len = results.rows.length, i;
               msg = "<p>Found rows: " + len + "</p>";
               document.querySelector('#status').innerHTML +=  msg;

               for (i = 0; i < len; i++) {
                  msg = "<p><b>" + results.rows.item(i).id + "</b></p>";
                  document.querySelector('#status').innerHTML +=  msg;
                  
		  msg = "<p><b>" + results.rows.item(i).code + "</b></p>";
                  document.querySelector('#status').innerHTML +=  msg;
		  
		  msg = "<p><b>" + results.rows.item(i).request + "</b></p>";
                  document.querySelector('#status').innerHTML +=  msg;
               }
            }, null);
         });

	}
</script>
</head>
<body>
<form NAME="myform" ACTION="" METHOD="POST">
Enter bin number in the box: <br>
<input TYPE="text" NAME="inputbox" VALUE=""><p>
<input TYPE="button" NAME="button1" Value="Read" onClick="readText(this.form)">
<input TYPE="button" NAME="button2" Value="SQL" onClick="test()">
</form>
<form NAME="myform2" ACTION="" METHOD="POST">
Enter six-digit code in the box: <br>
<input TYPE="text" NAME="inputbox" VALUE=""><p>
<input TYPE="button" NAME="button1" Value="Read" onClick="readText(this.form)">
<input TYPE="button" NAME="button2" Value="SQL" onClick="test()">
</form>
<form NAME="testform" ACTION="" METHOD="POST">
<input TYPE="number" NAME="bin_number" VALUE="Enter bin number (Ex: 123456)"><p>
<input TYPE="number" NAME="six_digit_code" VALUE="Enter six digit code (Ex: 654321)"><p>
<input TYPE="text" NAME="service_request" VALUE="Enter service request here."><p>
<input TYPE="button" VALUE="Upload Request" onClick="test()">
</form>
</body>
</html>

<!--
#URL:https://www.javaworld.com/article/2077176/using-javascript-and-forms.html
#URL:https://www.geeksforgeeks.org/form-validation-using-html-javascript/
-->


