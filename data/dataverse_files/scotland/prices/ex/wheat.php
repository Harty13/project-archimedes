<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>The price of wheat, 1327 - 1598</title>
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
<h4>The price of wheat, 1327 - 1598</h4>
<p>
<a href="exs.php">Notes on Exchequer Roll data</a><br>
<a href="../extop.php">Other Exchequer Roll price series</a><br><br>

Return to the <a href="../../pricetop.php">Price data directory</a></p>

<pre>INPUT 1 2 N  
 
 The price of wheat, 1327 - 1598
 
  From: Exchequer Rolls of Scotland (Rotuli Scaccarii Regum Scotorum),
        1264-1600 (23 vols., Edinburgh, 1878-1908)  [Average prices for
        1325-1465 taken from Grant, A., Independence and Nationhood:
        Scotland, 1306 - 1469 (Edward Arnold, London, 1984).]

 1 - Average wheat prices; 1327-1466 (gaps)
 2 - Murray prices; 1472-1516 (gaps)
 3 - Fife prices; 1476-1592 (gaps)
 4 - Stirling prices; 1474-1596 (gaps)
 5 - Ballincreiff (W. Lothian) prices; 1488-1591 (gaps)
 6 - Colbrandspeth (N. Berwickshire) prices; 1506-1598 (gaps)
 7 - Carrick prices; 1480-1594 (gaps)

FORMAT
2 2 2 1 2 3 0 0 (I4,1X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,7X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,13X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,19X,I3,1X,I2)
2 2 2 1 2 3 0 0 (I4,26X,I2,1X,I2)
2 2 2 1 2 3 0 0 (I4,32X,I3,1X,I2)
2 2 2 1 2 3 0 0 (I4,39X,I3,1X,I2)
STOP
Crop Ave.  Mur-  Fife   Stir- Ball. Colbr. Carrick     Ball.=Ballincreiff
Year price ray          ling                            Colbr.=Colbrandspeth
     s. d. s. d. s. d.  s. d. s. d.  s. d.  s. d.
DATA
1327  1  8
1328  1  9
1329  2  6
1330  2  4
1357  1  8
1358  2  7
1361  2
1364  3  7
1365  2  7
1366  2  2
1368  2 10
1371  2  8
1372  2 11
1373  3  5
1379  3  6
1381  3  4
1383  2  5
1424  3  4
1434  6
1445 10
1446 12
1448  7  2
1449  9
1450  8
1451  6  8
1455  9  6
1456  8
1461  9
1464  7  4
1465  7  4
1466  8  4
1472        5
1473        5
1474        5            8  4
1475        6 10         9  3
1476        6  8  9      8
1477                    10
1478        6 11        12
1479        6  5         9
1480        8    14     16                  10
1483                                        13  4
1488                          13
1489             14
1491                          10
1497             13
1498             12  8
1503        9  4 
1504             10
1505       10
1506       10    14  4  12  6        12
1507             17  8
1508        8
1511        6  8
1515        8  4 10
1516        8  4 12  6
1521             12
1524             12  6
1525             13  4
1526             13  4
1527             17
1528             17
1529             12
1530             15  6
1534             16
1535             22
1541                    22
1542             24
1551                    30
1553                    12  6
1554                                 13  6
1555                          36     32
1556                                 30
1557                                 20
1558                                 22
1559                    38           34
1560             40                  30
1561                                 30
1562             50           50     53  4
1565             30     40
1566             25     40    20
1568             30     20    40
1572             50
1573             50           40
1578                          46  8
1587                                        73  4
1588             80           80     80     80
1590                                        73  4
1591             66  8        66  8         80
1592             75                         80
1593                                       173  4
1594                                       173  4
1596                   240   
1598                                100
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
