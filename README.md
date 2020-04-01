# City of Lubbock

## Solid Waste Management

Welcome to The City of Lubbock Solid Waste Management site. At this new website you may submit reports and/or requests about how your trash is managed. You may also use this site to view if your trash has been picked for this week.
<html>
<script>
var peopleData = [
    { name: "John Dow", email: "john@company.com" },
    { name: "Don Dow", email: "don@company.com" }
];
 
function initDb() {
    var request = indexedDB.open("PeopleDB", 1);  
    request.onsuccess = function (evt) {
        db = request.result;                                                            
    };
 
    request.onerror = function (evt) {
        console.log("IndexedDB error: " + evt.target.errorCode);
    };
 
    request.onupgradeneeded = function (evt) {                   
        var objectStore = evt.currentTarget.result.createObjectStore("people", 
                                     { keyPath: "id", autoIncrement: true });
 
        objectStore.createIndex("name", "name", { unique: false });
        objectStore.createIndex("email", "email", { unique: true });
 
        for (i in peopleData) {
            objectStore.add(peopleData[i]);
        }
    };
}
</script>
</html>
To submit a service request, follow the instructions below:

<h2>(Optional): Upload Image of Trash Bin</h2>
<form>
<input type="file" accept="image/*" id="file" name="image1" onchange="loadFile(event)" style="display: none;">
</form> 
<p><label for="file" style="curser: pointer;">Upload Image</label></p>
<p><img id="output" width="200" /></p>

<script>
var loadFile = function(event)	{
	
	var image = document.getElementById('output');

	image.src = URL.createObjectURL(event.target.files[0]);

};

</script>

</body>
</html>

<!--
<html>
<head>
<script>
function gen_sql_table()					{
	
	var bin_num = document.forms["WasteForm"]["Bin Number"];

	var six_digits = document.forms["WasteForm"]["Six Digit Code"];

	var service_request = document.form["WasteForm"]["Service Request"];

	var db = openDatabase('bindb','1.0','Test DB',30000);

	db.transaction(function(tx)		{
		
		tx.executeSQL('CREATE TABLE IF NOT EXISTS WEBDB (id INTEGER, code INTEGER, request TEXT');

		tx.executeSQL('INSERT INTO WEBDB (id,code,request) (?,?,?)',[bin_num,six_digits,service_request]);
	
	});

	db.transaction(function (tx) { 

		    tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) { 

		       var len = results.rows.length, i; 

		       msg = "<p>Found rows: " + len + "</p>"; 

		       document.querySelector('#status').innerHTML +=  msg; 

	      

		       for (i = 0; i < len; i++) { 

			  msg = "<p><b>" + results.rows.item(i).log + "</b></p>"; 

			  document.querySelector('#status').innerHTML +=  msg; 

		       } 

		    }, null); 

		 }); 

      </script>


}
</script>
<body>
<form name="WasteForm" onsubmit="return gen_sql_table()" method="post">
<p>Enter Bin Number: <input type="text" name="Bin Number"></p><br>
<p>Enter Six Digit Code:<input type="password" name="Six Digit Code"></p><br>
<p>Enter Your Service Request:<input type="text" name="Service Request"></p><br>
<p><input type="submit" value="send" name="Submit" onClick="gen_sql_table()"></p>
</form>
</body>
</html>
-->

<!--
<html>
   <head>

      <script type = "text/javascript">
         var db = openDatabase('mydb', '1.0', 'Test DB', 2 * 1024 * 1024);
         var msg;

         db.transaction(function (tx) {
            tx.executeSql('CREATE TABLE IF NOT EXISTS LOGS (id unique, log)');
            tx.executeSql('INSERT INTO LOGS (id, log) VALUES (1, "foobar")');
            tx.executeSql('INSERT INTO LOGS (id, log) VALUES (2, "logmsg")');
            msg = '<p>Log message created and row inserted.</p>';
            document.querySelector('#status').innerHTML =  msg;
         })

         db.transaction(function (tx) {
            tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
               var len = results.rows.length, i;
               msg = "<p>Found rows: " + len + "</p>";
               document.querySelector('#status').innerHTML +=  msg;

               for (i = 0; i < len; i++) {
                  msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
                  document.querySelector('#status').innerHTML +=  msg;
               }
            }, null);
         });
	
	db.transaction(function (tx) { 

		    tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) { 

		       var len = results.rows.length, i; 

		       msg = "<p>Found rows: " + len + "</p>"; 

		       document.querySelector('#status').innerHTML +=  msg; 

	      

		       for (i = 0; i < len; i++) { 

			  msg = "<p><b>" + results.rows.item(i).log + "</b></p>"; 

			  document.querySelector('#status').innerHTML +=  msg; 

		       } 

		    }, null); 

		 }); 

      </script>
   </head>

   <body>
      <div id = "status" name = "status">Status Message</div>
   </body>
</html>

-->
<!--
<html>
<body>
<form action="welcome.php" method="post">
Enter Bin Number: <input type="text" name="bin_num"><br>
Enter Six Digits: <input type="text" name="six_digits"><br>
Enter Service Request: <input type="text" name="service_request"><br>
<input type="submit">
</form>

</body>
</html>
-->

<html>
<head>
<title>Service Request Form</title>
<script>
window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || 
window.msIndexedDB;
 
window.IDBTransaction = window.IDBTransaction || window.webkitIDBTransaction || 
window.msIDBTransaction;
window.IDBKeyRange = window.IDBKeyRange || 
window.webkitIDBKeyRange || window.msIDBKeyRange
 
if (!window.indexedDB) {
   window.alert("Your browser doesn't support a stable version of IndexedDB.")
}
function read_bin_number(binum)			{
	
	var binumber = binum.bin.value

	alert("You typed:" + binumber);

}

function read_six_digit_code(six_digit_code)	{
	
	var code = six_digit_code.code.value

	alert("You typed:" + code);

}

function read_service_request(service_request)	{
	
	var request = service_request.complaint.value

	alert("You typed:" + request);

}

function indexed_db_add() {
   var request = db.transaction(["employee"], "readwrite")
   .objectStore("employee")
   .add({ id: "01", name: "prasad", age: 24, email: "prasad@tutorialspoint.com" });
   
   request.onsuccess = function(event) {
      alert("Prasad has been added to your database.");
   };
   
   request.onerror = function(event) {
      alert("Unable to add data\r\nPrasad is already exist in your database! ");
   }
}
</script>
</head>
<body>
<button onclick="read()">Read </button>
<form name="BinForm" action="" method="post">Enter bin number:<br>
<input type="text" name="bin" value="">
<input type="button" name="button" value="Click" onClick="read_bin_number(this.form)">
</form>
<form name="CodeForm" action="" method="post">Enter six digit code:<br>
<input type="password" name="code" value="">
<input type="button" name="button" value="Click" onClick="read_six_digit_code(this.form)">
</form>
<form name="ServeForm" action="" method="post">Enter service request:<br>
<input type="text" name="complaint" value="">
<input type="button" name="button" value="Click" onClick="read_service_request(this.form)">
</form>
<form name="indexedb" action="" method="post">Testing IndexedDb:<br>
<input type="button" name="button" value="IndexedDB" onClick="indexed_db_add()">
</form>
<form name="sqlform"><br>
Enter bin number:<input type="text" name="bin" value=""><br>
Enter six digit code:<input type="password" name="code" value=""><br>
Enter Service Request:<input type="text" name="service_request" value=""><br>
<input type="button" name="button" value="Submit" onClick="add()"><br>
</body>
</html>

Read

<html>
   <head>
      <meta http-equiv = "Content-Type" content = "text/html; charset = utf-8" />
      <script type = "text/javascript">
         
         //prefixes of implementation that we want to test
         window.indexedDB = window.indexedDB || window.mozIndexedDB || 
         window.webkitIndexedDB || window.msIndexedDB;
         
         //prefixes of window.IDB objects
         window.IDBTransaction = window.IDBTransaction || 
         window.webkitIDBTransaction || window.msIDBTransaction;
         window.IDBKeyRange = window.IDBKeyRange || window.webkitIDBKeyRange || 
         window.msIDBKeyRange
         
         if (!window.indexedDB) {
            window.alert("Your browser doesn't support a stable version of IndexedDB.")
         }
         
         const employeeData = [
            { id: "00-01", name: "gopal", age: 35, email: "gopal@tutorialspoint.com" },
            { id: "00-02", name: "prasad", age: 32, email: "prasad@tutorialspoint.com" }
         ];
         var db;
         var request = window.indexedDB.open("newDatabase", 1);
         
         request.onerror = function(event) {
            console.log("error: ");
         };
         
         request.onsuccess = function(event) {
            db = request.result;
            console.log("success: "+ db);
         };
         
         request.onupgradeneeded = function(event) {
            var db = event.target.result;
            var objectStore = db.createObjectStore("employee", {keyPath: "id"});
            
            for (var i in employeeData) {
               objectStore.add(employeeData[i]);
            }
         }
         
         function read() {
            var transaction = db.transaction(["employee"]);
            var objectStore = transaction.objectStore("employee");
            var request = objectStore.get("00-03");
            
            request.onerror = function(event) {
               alert("Unable to retrieve daa from database!");
            };
            
            request.onsuccess = function(event) {
               // Do something with the request.result!
               if(request.result) {
                  alert("Name: " + request.result.name + ", 
                     Age: " + request.result.age + ", Email: " + request.result.email);
               } else {
                  alert("Kenny couldn't be found in your database!");
               }
            };
         }
         
         function readAll() {
            var objectStore = db.transaction("employee").objectStore("employee");
            
            objectStore.openCursor().onsuccess = function(event) {
               var cursor = event.target.result;
               
               if (cursor) {
                  alert("Name for id " + cursor.key + " is " + cursor.value.name + ", 
                     Age: " + cursor.value.age + ", Email: " + cursor.value.email);
                  cursor.continue();
               } else {
                  alert("No more entries!");
               }
            };
         }
         
         function add() {
            var request = db.transaction(["employee"], "readwrite")
            .objectStore("employee")
            .add({ id: "00-03", name: "Kenny", age: 19, email: "kenny@planet.org" });
            
            request.onsuccess = function(event) {
               alert("Kenny has been added to your database.");
            };
            
            request.onerror = function(event) {
               alert("Unable to add data\r\nKenny is aready exist in your database! ");
            }
         }
         
         function remove() {
            var request = db.transaction(["employee"], "readwrite")
            .objectStore("employee")
            .delete("00-03");
            
            request.onsuccess = function(event) {
               alert("Kenny's entry has been removed from your database.");
            };
         }
      </script>
      
   </head>
</html>

<html>
<script>
if (!('indexedDB' in window)) {
  console.log('This browser doesn\'t support IndexedDB');
  return;
}
</script>
</html>
<!--
#URL:https://www.javaworld.com/article/2077176/using-javascript-and-forms.html
#URL:https://stackoverflow.com/questions/21396279/display-image-and-validation-of-image-extension-before-uploading-file-using-java
#URL:https://stackoverflow.com/questions/8810927/showing-an-image-from-an-array-of-images-javascript
#URL:https://stackoverflow.com/questions/21396279/display-image-and-validation-of-image-extension-before-uploading-file-using-java
#URL:https://codewithlogic.wordpress.com/2013/09/01/creating-a-file-uploader-using-javascript-and-html-5/
#URL:https://www.webtrickshome.com/faq/how-to-display-uploaded-image-in-html-using-javascript
-->
