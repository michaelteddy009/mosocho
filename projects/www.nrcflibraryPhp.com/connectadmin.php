<!DOCTYPE html>
<html>
<head>
	<title>connectadmin</title>
	<link rel="stylesheet" type="text/css" href="styleLogIn.css">
</head>
<body>


<?php
 
//find out why include wount work in this instance

$servername = "localhost";
$username = "root";
$password = "";


// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else{
	//echo "Connected successfully<br>";
}



$sql = "SELECT * FROM nrcalibrary.accounts";
$result = $conn->query($sql);

//confirm that the query succeeded


$row = $result->fetch_assoc();
	

//conditional statement whether the user exists which leads to page rendering

if ($row['idno'] == $_POST["id"] && $row["password"] == $_POST["password"]) {

	 //display the navigation bar
	include "fist-page.php";


	//display changing pictures of factuals about the website
} else {
	include "index.php";
	echo '<script >document.getElementById("p2").innerHTML = "* Invalid Id or Password";</script>';

}


?>
</body>
</html>



