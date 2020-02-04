<!DOCTYPE html>
<html>
<head>
	<title>borrow</title>
	<link rel="stylesheet" type="text/css" href="css/styleborrow.css">
</head>
<body>
	<?php include "nav-template.php";?>
	<section id="admin/borrow-content" style="width:65%;float:left; background-color: white;">
		

		<form action="" method="post" style="height:600px; padding-left: 20%; width: %; border: solid 3px black;">

			<div style="width:100%; height:60Px; margin-top:40px;">
				<h3 style=" margin-top:0px; width:20%;float:left;">Student Name</h3>
					<select style="width:30%; float:left; border-radius: 3px;" >
				
					</select>
			</div>

			<div style="width:100%; height:70Px">
				<h3 style="margin-top:0px; width:20%;float:left;">Class Level</h3>
					<select style="width:30%; float:left; border-radius: 3px;">
						
					</select>
			</div >

			<div style="width:100%; height:70Px">
				<h3 style="margin-top:0px; width:20%;float:left;">Book Code</h3>
				<input type="" name="" size="35" style="border-radius: 3px; height: 23px; font-size: 17px;">
			</div>



			<div>
				<h3>Check Out Duration*</h3>
				<div style="padding-left:5%; font-size: 17px;">
					<input type="radio" name="duration" value="days7"> 1 Week<br>
  					<input type="radio" name="duration" value="days14"> 2 Weeks<br>
  					<input type="radio" name="duration" value="days30"> 1 Month<br>
  					<input type="radio" name="duration" value="days90">1 Term
				</div>
				
			</div>

			<div style="padding-top:20px;">
				<input type="submit" name="submit" value="Borrow" style="margin-left:%; height:30px; width:60%; font-size:20px; background-color:lightblue; border-radius: 10px;">
			</div>
			
			
			
			
			
			
			
		</form>
		
	</section>

	<script type="text/javascript"> document.getElementById("pageheading").innerHTML = "Check Out Books";</script>
</body>
</html>