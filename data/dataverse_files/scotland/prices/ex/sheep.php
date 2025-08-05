<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>The price of sheep, 1327 - 1599</title>
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
				<dd><a href="/hpw/scotland/demogtop.php">Demographic Data</a></dd>
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
<h4>The price of sheep, 1327 - 1599</h4>
<p>
<a href="exs.php">Notes on Exchequer Roll data</a><br>
<a href="../extop.php">Other Exchequer Roll price series</a><br><br>

Return to the <a href="../../pricetop.php">Price data directory</a></p>

<pre>INPUT 1 2 N 
 
 The price of sheep, 1327 - 1599
 
  From: Exchequer Rolls of Scotland (Rotuli Scaccarii Regum Scotorum),
        1264-1600 (23 vols., Edinburgh, 1878-1908)  [Average prices for
        1325-1465 taken from Grant, A., Independence and Nationhood:
        Scotland, 1306 - 1469 (Edward Arnold, London, 1984).]

 This file contains;
 
 1 - Average prices for sheep (each); 1327 - 1424 (big gaps!)
 2 - Sheep prices from Ross; 1479 - 1599 (gaps)

FORMAT
2 2 1 1 2 3 0 0 (I4,1X,I1,1X,I2)
2 2 1 1 2 3 0 0 (I4,6X,I2,1X,I1)
STOP
Crop Ave. Ross
Year      price
     s.d. s.d.
DATA
1327 1  6
1328 1  6
1329 1 10
1330 1  8
1367 1
1371 1  6
1372 1
1379 1  2
1383 1
1424 2  6
1479       1 8
1522       2 0
1524       2 0
1536       3 0
1538       3 0
1539       3 0
1541       3 0
1560       5 0
1565       6 8
1566       6 8
1568       6 8
1573       6 8
1578       6 8
1580       6 8
1587       6 8
1588       6 8
1590      13 4
1591      13 4
1592      13 4
1599      13 4
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
