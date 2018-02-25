<?php
include("private/connect.php");
$title = "AArt - Your home for ASCII Art";
include("header.html");
include("sidebar.php");
?>
		<div class="flakes-content">
			<div class="view-wrap">
				<h1>Submit Art</h1>
			</div>
<?php
if(isset($_POST['username'])){
	$username = mysqli_real_escape_string($conn, $_POST['username']);
	$password = mysqli_real_escape_string($conn, $_POST['password']);
	
	$sql = "SELECT * from users where username='$username';";
	$result = mysqli_query($conn, $sql);

	$row = $result->fetch_assoc();

	if($username === $row['username'] and $password === $row['password']){
		$title = mysqli_real_escape_string($conn, $_POST['title']);
		$art = mysqli_real_escape_string($conn, $_POST['art']);
		?>
		<h1>Logged in as <?php echo($username);?></h1>
		<?php

		$uid = $row['id'];
		$sql = "INSERT INTO art (title, art, userid) values('$title', '$art', '$uid')";
		mysqli_query($conn, $sql);
	?>
	<h2>SUCCESS!</h2>
	<?php
	} else {
	?>
	<h2>Error</h2>
	<?php
	}
} else {
?>
			<div class="grid-1">
				<div class="span-1">
					<fieldset>
						<legend>Art</legend>
						<form action="submit.php" method="post">
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
									<label>Art Title</label>
									<input type="text" name="title">
								</li>
								<li>
									<label>Art</label>
									<textarea name="art"></textarea>
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
