<?php
include("private/connect.php");
$title = "AArt - Your home for ASCII Art";
include("header.html");
include("sidebar.php");
?>
		<div class="flakes-content">
			<div class="view-wrap">
				<h1>Login</h1>
			</div>
<?php
if(isset($_POST['username'])){
	$username = mysqli_real_escape_string($conn, $_POST['username']);

	$sql = "SELECT * from users where username='$username';";
	$result = mysqli_query($conn, $sql);
	$row = $result->fetch_assoc();

	if($_POST['username'] === $row['username'] and $_POST['password'] === $row['password']){
		?>
		<h1>Logged in as <?php echo($username);?></h1>
		<?php

		$uid = $row['id'];
		$sql = "SELECT isRestricted from privs where userid='$uid' and isRestricted=1;";
		$result = mysqli_query($conn, $sql);
		$row = $result->fetch_assoc();
		if($row['isRestricted']){
			?>
			<h2>This is a restricted account</h2>

			<?php
		}else{
			?>
			<h2>Here is a flag you:</h2>
      <?php
        readfile("private/flag");
		}
	?>
	<h2>SUCCESS!</h2>
	<?php
	}
} else {
?>
			<div class="grid-1">
				<div class="span-1">
					<fieldset>
						<legend>Account</legend>
						<form action="login.php" method="post">
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
									<input type="submit" value="Login">
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
