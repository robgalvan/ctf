<?php
include("private/connect.php");
$title = "AArt - Your home for ASCII Art";
include("header.html");
include("sidebar.php");
?>
		<div class="flakes-content">
			<div class="view-wrap">
				<h1>Register</h1>
			</div>
<?php
if(isset($_POST['username'])){
	$username = mysqli_real_escape_string($conn, $_POST['username']);
	$password = mysqli_real_escape_string($conn, $_POST['password']);

	$sql = "INSERT into users (username, password) values ('$username', '$password');";
	mysqli_query($conn, $sql);
  
	$sql = "INSERT into privs (userid, isRestricted) values ((select users.id from users where username='$username'), 1);";
	mysqli_query($conn, $sql);
	?>
	<h2>SUCCESS!</h2>
	<?php
} else {
?>
			<div class="grid-1">
				<div class="span-1">
					<fieldset>
						<legend>Account</legend>
						<form action="register.php" method="post">
							<ul>
								<li>
									<label>Username</label>
									<input type="text" name="username">
								</li>
								<li>
									<label>Password</label>
									<input type="text" name="password">
								</li>
								<li>
									<input type="submit">
									</li>
							</ul>
						</form>
					</fieldset>
				</div>
			</div>
<?php
}
?>
		</div>
<?php
include("footer.html");
?>
