<!DOCTYPE html>
<html>
<head>
	<title>nrca_library</title>
	<link rel="stylesheet" type="text/css" href="css/styleLogIn.css">
</head>
<body>
	 	<section style="background-color: green;height: 80px; padding:0px;border-bottom: solid 3px black;margin-bottom: 30px;">
	 		<action style="width:10%;float:left;padding-left: 3%;padding-top:28.5px;"><a href="index.php"><BUTTON>Main Page</BUTTON></a></action>
	 		<action style="width:80%;height:50px;padding-top:15px;padding-bottom:15px;float:left;">
	 			<p style="height:50px; margin:0px;font-size: 40px;padding-left: 35%">Admin Log In</p>
	 		</action>
	 		
	 	</section>

	
	<div id="loginform">
	<form action='connectadmin.php' method="post">
		<p id="p2"  style="width:50%;margin:auto;color:red;"></p>
		<div id="loginfield">
			<label style="font-size: 17px"><b>Admin ID:</b></label><br>
			<input type="number" name="id" required="true" placeholder="example 1234">
		</div>

		<div id="loginfield">
			<label style="font-size: 17px"><b>Password:</b></label><br>
			<input type="password" name="password" required="true" size="" placeholder="";>
		</div>

		<div id='loginfield'>
			<input  type="submit" value="Log In" style="background-color: black; color:white; width:30%; height: 28px; font-family: aerial">
		</div>
		
	</div>
	</form>



</body>
</html>