<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>The price of cattle (marts), 1326 -1598</title>
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
<h4>The price of cattle (marts), 1326 -1598</h4>
<p>
<a href="exs.php">Notes on Exchequer Roll data</a><br>
<a href="../extop.php">Other Exchequer Roll price series</a><br><br>

Return to the <a href="../../pricetop.php">Price data directory</a></p>

<pre>INPUT 1 2 N 
 
 The price of cattle (marts), 1326 -1598
 
  From: Exchequer Rolls of Scotland (Rotuli Scaccarii Regum Scotorum),
        1264-1600 (23 vols., Edinburgh, 1878-1908)  [Average prices for
        1325-1465 taken from Grant, A., Independence and Nationhood:
        Scotland, 1306 - 1469 (Edward Arnold, London, 1984).]
 
 This file contains;
 
 1 - Average Price per Mart; 1326 - 1467 (big gaps!)
 2 - Mart Prices in Ross; 1479, 1506,11,24,30,35-41,60-68
 3 - Mart Prices of Galloway; 1470 - 1488 (big gaps!)
 4 - Mart Prices of Strathern; 1479, 1497-1513, 1525-42, 1560-84, 1594 (gaps)
 5 - Mart Prices of Bute; 1505-54, 1563, 1575-84 (gaps)
 6 - Mart Prices of Discheor and Toyer (Breadalbane); 1555-60, 1583-98 (gaps)

FORMAT
2 2 1 1 2 3 0 0 (I4,1X,I2,1X,I2)
2 2 1 1 2 3 0 0 (I4,7X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I4,12X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I4,17X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I4,22X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I4,27X,I3,1X,I1)
STOP
Crop Ave.   Ross Gall Stra Bute Discheor
Year price       oway earn      & Toyer
      s. d.  s.d. s.d. s.d. s.d. s.d.
DATA
1326  7 10
1327  9  3
1328  8
1329  9  1
1330  7
1358  5
1366  6  8
1367  5 10
1371  5
1372  5
1379  5
1384  5
1424 13 4
1433 11
1437 11 11
1449 16
1450 18
1452 17  3
1453 13  4
1455 20
1456 17  6
1457 14 10
1458 13
1460 14  5
1461 15
1462 15  2
1463 18
1464 18  6
1466 16  2
1467 19
1470 00 00 00 0 17 5
1474            20
1479       12   20   21
1488            20
1497                 20
1500                 20
1501                 20
1503                 20
1505                 20   20
1506       18        20
1507                      20
1508                 20
1509                 20
1511       16
1513                 20   20
1521                      13 4
1522                      13 4
1524       20             13 4
1525                 13 4 
1526                 15   13 4
1527                 15   20
1528                 15   20
1529                 15   20
1530 00 00 30 0 00 0 30   20
1531                 20   20
1532                 20   20
1533                      20
1534                 20   30
1535       20
1536       24        20   24
1538       26 8      20
1539       30        20   24
1540                 20   24
1541       30        20   24
1542                 20  
1551                      24
1552                      24
1553                      24
1554                      24
1555                      00 0  40
1556                            40
1559                            40
1560       46 8      20         40
1561                 20
1563                 20   24
1564       66 8      20
1566       66 8      20
1568       66 8
1571                 20
1572                 20
1573                 20
1575                 20   24
1576                 20
1577                 20
1578                      24
1581                 20   24
1583                 20   24   100
1584                 20   24
1587                           100
1591                           133 4
1593                           133 4
1596                 20
1597                           200
1598                           200
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
