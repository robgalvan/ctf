<?php
include("private/connect.php");
$title = "AArt - Your home for ASCII Art";
include("header.html");
include("sidebar.php");
?>
		<div class="flakes-content">
			<div class="view-wrap">
				<h1>Voting!</h1>
			</div>
<?php
if(isset($_GET['id']) and isset($_GET['type'])){
	$id = mysqli_real_escape_string($conn, $_GET['id']);
	$type = mysqli_real_escape_string($conn, $_GET['type']);

	if($type === "up"){
		$sql = "UPDATE art SET karma=karma+1 where id='$id';";
	} elseif($type === "down"){
		$sql = "UPDATE art SET karma=karma-1 where id='$id';";
	}

	mysqli_query($conn, $sql);
	$sql = "SELECT karma, title from art where id='$id'";
	$result = mysqli_query($conn, $sql);
	$row = $result->fetch_assoc();
	?>
			<div class="grid-1">
				<div class="span-1">
					<h2><?php echo($row['title']);?> now has <?php echo($row['karma']);?> karma</h2>
				</div>
			</div>
	<?php
} else {
?>
			<div class="grid-1">
				<div class="span-1">
					<h2>What are you doing here?</h2>
				</div>
			</div>
<?php
}
?>
		</div>
<?php
include("footer.html");
?>
