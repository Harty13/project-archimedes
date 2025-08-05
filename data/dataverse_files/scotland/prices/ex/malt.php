<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>The price of malt, 1328 -1598</title>
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
<h4>The price of malt, 1328 -1598</h4>
<p>
<a href="exs.php">Notes on Exchequer Roll data</a><br>
<a href="../extop.php">Other Exchequer Roll price series</a><br><br>

Return to the <a href="../../pricetop.php">Price data directory</a></p>

<pre>INPUT 1 2 N  
 
 The price of malt, 1328 -1598
 
 From: Exchequer Rolls of Scotland (Rotuli Scaccarii Regum Scotorum),
       1264-1600 (23 vols., Edinburgh, 1878-1908)  [Average prices for
       1325-1465 taken from Grant, A., Independence and Nationhood:
       Scotland, 1306 - 1469 (Edward Arnold, London, 1984).]
 
 This file contains;
 1 - Average malt price; 1328-1465 (gaps)
 2 - Stirling malt price; 1474-1569 (gaps)
 3 - Fife malt price; 1476-1578 (gaps)
 4 - Dumbarton malt price; 1596-1598

FORMAT
2 2 2 1 2 3 0 0 (I4,1X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,7X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,13X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,19X,I3,1X,I2)
STOP
Crop Ave.  Stir- Fife  Dumbarton
Date price ling  price price
           price
     s. d. s. d. s. d.  s. d.
DATA 
1328  1  1
1329  2  2
1330  2  4
1364  2  8
1365  2  3
1366  2  1
1371  2  3
1372  2  7
1373  2  7
1379  2 11
1383  2  3
1443  3  4
1445  6  1
1446  5
1447  5
1448  5
1449  3 10
1450  4  3
1460  3  4
1461  6  8
1462  3  4
1463  4  8
1464  6  8
1465  4  2
1474        6  8
1475        8
1476        8     7  6
1477        8
1478       10     6  8
1480       10    10
1503             10
1507       10  7
1508        7
1509        7
1528             10  6
1529              8  4
1530              8  4
1551       24
1552       13  4
1554       13  4
1555       30 
1560             34
1561             42
1563             30
1566       20
1569       22  6
1578             30
1596                   133  4
1597                   160
1598                   120
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
