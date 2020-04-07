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
      	function test()								{
         var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
         var msg;

         db.transaction(function (tx) {
            tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id,code,request)');
            tx.executeSql('INSERT INTO LOGS (id,code,request) VALUES (123456, 654321,"QR Code ripped off")');
            tx.executeSql('INSERT INTO LOGS (id,code,request) VALUES (789012, 210987,"Lid ripped off")');
            msg = '<p>Log message created and row inserted.</p>';
            document.querySelector('#status').innerHTML =  msg;
         })

         db.transaction(function (tx) {
            tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
               var len = results.rows.length, i;
               msg = "<p>Found rows: " + len + "</p>";
               document.querySelector('#status').innerHTML +=  msg;

               for (i = 0; i < len; i++) {
                  msg = "<p><b>" + results.rows.item(i).request + "</b></p>";
                  document.querySelector('#status').innerHTML +=  msg;
               }
            }, null);
         });

	}
	test();
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
</script>
</head>
<body>
<form NAME="myform" ACTION="" METHOD="GET">
Enter something in the box: <br>
<input TYPE="text" NAME="inputbox" VALUE=""><p>
<input TYPE="button" NAME="button1" Value="Read" onClick="readText(this.form)">
<input TYPE="button" NAME="button2" Value="Write" onClick="writeText(this.form)">
<input TYPE="button" NAME="button3" Value="SQL" onClick="test()">
</form>
</body>
</html>

test2()
#URL:https://www.javaworld.com/article/2077176/using-javascript-and-forms.html
#URL:https://www.geeksforgeeks.org/form-validation-using-html-javascript/
