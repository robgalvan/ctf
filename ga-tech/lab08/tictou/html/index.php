<?php
include("private/connect.php");
$title = "AArt - Your home for ASCII Art";
include("header.html");
include("sidebar.php");
?>
		<div class="flakes-content">
			<div class="view-wrap">
				<h1>AArt</h1>

				<h3>Welcome to AArt, your home for ASCII Art</h3>
				<p>Need new ASCII art for you login banner? New images to dump in IRC? We've got you covered here.</p>

<?php

$sql = "SELECT * from art ORDER BY karma DESC;";
$result = mysqli_query($conn, $sql);

while($row = $result->fetch_assoc()){
	$name = $row['title'];
	$userid=$row['userid'];
	$art = $row['art'];
	$aid = $row['id'];

	$sql = "SELECT username FROM users WHERE id=$userid;";
	$res= mysqli_query($conn, $sql)->fetch_assoc();
	$username = $res['username'];
	
	$karma = $row['karma'];
?>
			<div class="grid-1">
				<div class="span-1">
					<fieldset class="flakes-information-box">
							<legend><?php echo($name);?></legend>
							<dl>
								<dt>Submitted By</dt>
								<dd><?php echo($username);?></dd>
							</dl>
							<dl>
								<dt>Art</dt>
								<dd><pre><code><?php echo($art);?></code></pre></dd>
							</dl>
							<dl>
								<dt>Karma</dt>
								<dd><?php echo($karma);?></dd>
							</dl>
							<div class="grid-2">
								<div class="span-1">
									<a class="button-darkblue" href="vote.php?id=<?php echo($aid);?>&type=up">Upvote</a>
								</div>
								<div class="span-1">
									<a class="button-darkblue" href="vote.php?id=<?php echo($aid);?>&type=down">Downvote</a>
								</div>
							</div>
					</fieldset>
				</div>
			</div>
<?php

} //end select loop
?>
<?
include("footer.html");
?>
