<?php
header("Location: https://iisg.amsterdam/en/research/projects/hpw/calculate.php",TRUE,301);
exit('go to <a href="https://iisg.amsterdam/en/research/projects/hpw/calculate.php">new website</a>');
?>




<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
	<title>Prices and Wages - Conferences</title>
	<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
	<style type="text/css" media="all">@import url(/styles/sochist.css);</style>
</head>

<body>
<center>
<a name="top"></a>
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/top-home-sochist.inc.php"; ?>

<div class="bulk">
	<div class="navsecond">
		<dl id="menu">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/menu-hpw.inc.php"; ?>
		</dl>
		<dl id="email">
			<dd>Email: <?php require_once "_email_hpw.inc.php"; ?></dd>
		</dl>
	</div>
	<div class="navthird">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/search-ghome-sochist.inc.php"; ?>
		<dl id="also">
			<dt>See also</dt>
			<dd><a href="/research/">Research</a></dd>
			<dd><a href="/indonesianeconomy/">Indonesian Economic Development</a></dd>
			<dd><a href="https://www.neha.nl/">Netherlands Economic History Archive</a></dd>
		</dl>
	</div>
	<div class="content">

<h2>Conferences</h2>

<p>
<strong>Law and Economic Development</strong><br>
Conference of the <a href="http://www.lse.ac.uk/collections/economicHistory/GEHN/">Global Economic History Network</a><br>
<a href="law-economic-development.php">Programme</a><br>
<a href="law-economic-development.pdf">Call for papers</a> - <span class="small">deadline expired</span><br>
Utrecht, 20-22 September 2007</p>

<p><strong>The Return of the Guilds</strong><br>
Conference of the <a href="http://www.lse.ac.uk/collections/economicHistory/GEHN/">Global Economic History Network</a><br>
<a href="return-guilds.php">Programme</a><br>
Utrecht, 5-7 October 2006
</p>

<p>
<strong>The Rise, Organization, and Institutional Framework of Factor Markets</strong><br>
Conference of the <a href="http://www.lse.ac.uk/collections/economicHistory/GEHN/">Global Economic History Network</a><br>
<a href="factormarkets-intro.php">Introduction</a><br>
<a href="factormarkets.php">Conference Programme and papers</a><br>
Utrecht, 23-25 June 2005<br>
</p>

<p>
<strong>Towards a Global History of Prices and Wages</strong><br>
<a href="globalhistory.php">Conference programme and papers</a><br>
Utrecht, 19-21 August 2004
</p>

<p>
<strong>Economic Growth and Institutional Change in Indonesia in the 19th and 20th Centuries</strong><br>
<a href="/research/ecgrowthprogr.php">Conference programme and papers</a><br>
Amsterdam, 25-26 February 2002
</p>

		<div class="top"><a href="#top">top</a></div>
	</div>
</div>

<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
