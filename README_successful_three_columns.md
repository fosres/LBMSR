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
<form>
<p><input type="file"  accept="image/*" name="image" id="file1"  onchange="loadFile1(event)" style="display: none;"></p>
<p><label for="file1" style="cursor: pointer;">Upload Image</label></p>
<p><img id="output1" width="200" /></p>
</form>

<form>
<p><input type="file"  accept="image/*" name="image" id="file2"  onchange="loadFile2(event)" style="display: none;"></p>
<p><label for="file2" style="cursor: pointer;">Upload Image</label></p>
<p><img id="output2" width="200" /></p>
</form>

<script>
var loadFile1 = function(event) {
	var image = document.getElementById('output1');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var loadFile2 = function(event) {
	var image = document.getElementById('output2');
	image.src = URL.createObjectURL(event.target.files[0]);
};
</script>
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
 var msg;

 var bins = document.testform.bin_number.value;

 var code =document.testform.six_digit_code.value;

 var service = document.testform.service_request.value;

 db.transaction(function (tx) {
    tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique,code,request TEXT)');
    tx.executeSql('INSERT INTO LOGS (id,code,request) VALUES (?,?,?)',[bins,code,service]);
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
<form NAME="testform" ACTION="" METHOD="GET">
Enter bin number in the box below: <br>
<input TYPE="number" NAME="bin_number" VALUE=""><p>
Enter six digit code in the box below: <br>
<input TYPE="number" NAME="six_digit_code" VALUE=""><p>
Enter service request in the box below: <br>
<input TYPE="text" NAME="service_request" VALUE=""><p>
<input TYPE="button" NAME="button1" Value="SQL" onClick="test()">
</form>
</body>
</html>

test4()
#URL:https://www.javaworld.com/article/2077176/using-javascript-and-forms.html
#URL:https://www.geeksforgeeks.org/form-validation-using-html-javascript/



