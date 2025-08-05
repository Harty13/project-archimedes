<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Demographic Data</title>
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
		<dt>Prices and Wages</dt>
			<dd><a href="/hpw/">Index</a></dd>
			<dd><a href="/hpw/scotland/">Scottish Database</a>
			<dl class="sub">
				<dd><a href="/hpw/scotland/croptop.php">Crop Yields</a></dd>
				<dd>Demographic Data</dd>
				<dd><a href="/hpw/scotland/pricetop.php">Price Series</a></dd>
				<dd><a href="/hpw/scotland/wagetop.php">Wage Series</a></dd>
				<dd><a href="/hpw/scotland/weathtop.php">Weather Statistics</a></dd>
				<dd><a href="/hpw/scotland/geogdata/scotlist.php">Counties and Places</a></dd>
				<dd><a href="/hpw/scotland/notes.php">User Notes</a></dd>
				</dl></dd>		
		</dl>
		<dl id="email">
			<dd>Email: 
<script language="javascript" type="text/javascript">
  <!--
  var wie = "hpw"
  var host2 = "g.nl"
  var host1 = "iis"
  document.write("<a href=" + "mail" + "to:" + wie + "@" + host1 + host2 + ">" + wie + "@" + host1 + host2 + "</a>")
  //-->
</script></dd>
		</dl>
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/print.inc.php"; ?>
	</div>
	<div class="navthird">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/search-ghome-sochist.inc.php"; ?>
	</div>
	<div class="content">

<h2>Scottish Economic History Database</h2>	
<h4>Demographic Data</h4>

<p>
Edinburgh mortality tables, 1740-1792<br>
<a href="demog/source1.php">For information on source</a></p>

<ul>
<li><a href="demog/age1.php">Age at death (0-50)</a></li>
<li><a href="demog/age2.php">Age at death (50+)</a></li>
<li><a href="demog/monthly.php">Burials per month, 1740-1792</a></li>
<li><a href="demog/burials.php">Burials, Children, 1740-1748</a></li>
<li><a href="demog/burials.php">Burials, Female adults, 1740-1748</a></li>
<li><a href="demog/burials.php">Burials, Male adults, 1740-1748</a></li>
<li><a href="demog/burials.php">Burials, Female, 1749-1780</a></li>
<li><a href="demog/burials.php">Burials, Male, 1749-1780</a></li>
<li><a href="demog/burials.php">Burials, total per annum , 1740-1780</a></li>
</ul>

<p>
Mortality indicies from Flinn et al., 1615 - 1820<br>
<a href="demog/source2.php">For information on source</a></p>

<ul>
<li><a href="demog/index1.php">Far North</a></li>
<li><a href="demog/index1.php">Highlands and Islands</a></li>
<li><a href="demog/index1.php">North-east Scotland</a></li>
<li><a href="demog/index1.php">Western Lowlands</a></li>
<li><a href="demog/index1.php">Western Lowlands excluding Glasgow</a></li>
<li><a href="demog/index1.php">Eastern Lowlands</a></li>
<li><a href="demog/index2.php">Eastern Lowlands excluding urban areas</a></li>
<li><a href="demog/index2.php">Western Borders</a></li>
<li><a href="demog/index2.php">Eastern Borders</a></li>
<li><a href="demog/index2.php">Urban Area</a></li>
<li><a href="demog/index2.php">Rural Area</a></li>
<li><a href="demog/index2.php">Scotland (Average)</a></li>
</ul>

		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
