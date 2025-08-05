<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>The Price of Poultry, 1491 - 1595</title>
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
<h4>The Price of Poultry, 1491 - 1595</h4>
<p>
<a href="exs.php">Notes on Exchequer Roll data</a><br>
<a href="../extop.php">Other Exchequer Roll price series</a><br><br>

Return to the <a href="../../pricetop.php">Price data directory</a></p>

<pre>INPUT 1 2 N  

 The Price of Poultry, 1491 - 1595 (big gaps!)

  From: Exchequer Rolls of Scotland (Rotuli Scaccarii Regum Scotorum),
        1264-1600 (23 vols., Edinburgh, 1878-1908)

 This file contains;

 1 - Prices at Tealing; 1491, 1494 & 1587
 2 - Prices in Kincardin; 1508
 3 - Prices in Fife; 1517-39,42,60-71,87-95 (gaps)
 4 - Prices in Perthshire; 1539-41
 5 - Prices in Ross; 1539 & 1562
 6 - Prices in Ballincrieff; 1555-73 & 1587 (gaps)

FORMAT
1 2 1 1 3 0 0 0 (I4,4X,I2)
1 2 1 1 3 0 0 0 (I4,13X,I2)
1 2 1 1 3 0 0 0 (I4,21X,I2)
1 2 1 1 3 0 0 0 (I4,27X,I2)
1 2 1 1 3 0 0 0 (I4,34X,I2)
1 2 1 1 3 0 0 0 (I4,40X,I2)
STOP
Crop  Tealing Kincardin Fife  Perth- Ross Ballin-
Year                          shire        creiff
        d.       d.      d.    d.     d.    d.
DATA
1491     3
1494     3
1508              2
1517                      4
1525                      4
1527                      4
1528                      4
1530                      6
1534                      8
1536                      6
1539                      8     4      3
1540                            4
1541                            4
1542                      6
1555                                        11
1556                                        10
1557                                        10
1558                                        10
1559                                        12
1560                     10                 12
1561                     10                 12
1562                     10          10
1563                                        12
1564                                        12
1565                     10	
1566                     10                 12
1568                     10                 12
1571                     10
1573                                        12
1587    24               30                 24
1591                     36
1592                     48
1595                     80
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
