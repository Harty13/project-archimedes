<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Stirling Town Council Price Statutes, 1520 - 1664</title>
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
<h4>Stirling Town Council Price Statutes, 1520 - 1664</h4>
<p>
<a href="stats.php">Note on town council price statutes</a><br>
<a href="../geogdata/stir.php">Other 
Stirlingshire (including Stirling Town Council) data</a><br>
Return to the <a href="../pricetop.php">Price data directory</a>
</p>
 
<pre>INPUT 3 2 N  
 
 Stirling Town Council Price Statutes, 1520 - 1664

 From; Robert Renwick, 'Extracts from the records of the Royal
       Burgh of Stirling, 1519 - 1666' (Glasgow, 1887)

 This file contains;
 1 - Malt (per boll); 1520-1664
 2 - Ale (per gallon); 1520-1664
 3 - Wheat (per boll); 1520-1664
 4 - Fine wheat oats (per peck); 1602-1664
 5 - Carse oats or corn (per peck); 1525-1664
 6 - Dry-field oats or corn (per peck); 1545-1664
 7 - Tallow (per stone); 1522-1664
 8 - Candle (per pound); 1522-1664
 9 - Wheat bread (per ounce); 1526-1664

FORMAT
3 2 2 1 1 2 3 0 (I2,1X,I4,1X,I2,1X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I2,1X,I4,9X,I2,1X,I1)
3 2 2 1 1 2 3 0 (I2,1X,I4,14X,I2,1X,I2,1X,I1)
2 2 3 1 2 3 0 0 (I2,1X,I4,22X,I2,1X,I1)
2 2 3 1 2 3 0 0 (I2,1X,I4,27X,I2,1X,I1)
2 2 3 1 2 3 0 0 (I2,1X,I4,32X,I2,1X,I1)
3 2 6 1 1 2 3 0 (I2,1X,I4,37X,I2,1X,I2,1X,I1)
1 2 5 2 3 0 0 0 (I2,1X,I4,48X,F4.1)
1 2 4 2 3 0 0 0 (I2,1X,I4,53X,F6.4)
STOP
                                        Dry-
                                  Carse field
                             Fine oats  oats
Court    Malt   Ale   Wheat  wheat or   or   Tallow Candle  Bread
Date                         oats corn corn                 (per 
         boll   gall  boll   peck peck peck   stone   lb.    oz.)

Mo Year  L.s.d. s.d.  L.s.d. s.d. s.d. s.d.  L.s.d.   s.d.    d.
DATA
01 1520  1 00 0         18 0
 4 1520                 17
 7 1520    16    1 4    17
10 1520    13 4         13 4
 1 1521    13 4         18 6
 4 1521    13 4         16
 9 1521    12           13 4
10 1522    12    1      16                  00  4       4.5 
10 1523          1 4    18                  00  4
10 1524               1 00
 1 1525    16         1
10 1525          1      14           5
10 1526    16           16                  00          4.5 0.1000
 9 1527    16    1 8  1
10 1528          1    1
10 1529    14 4         18
10 1545  1 10    2    1 18           8    6 00              0.1818
 1 1546  1 14         2  6
10 1546  1 10         1 12
10 1548  1  4    2    1  6                  00              0.1250
 1 1550  2  4         2 10
10 1554    16    1 4    18           5    4 00  9
 1 1555    19    1 4  1  3           4    3 00         10.0 
10 1555  1  8 8  2    1 12           7    5 00         11.0
10 1556  1 16    2 8  1 16           8    6 00          7.0
 1 1562  2       2 8               1 0    9
 1 1566  1 13         2  6 8       1      8 00         12.0
 4 1567  1 17         1 17 0    
10 1599  7  6 8  9 4  8            4    2 8  2  4      34.0
10 1600  6       8    8            3 4  2    2         32.0
11 1601  6  3 4  8    7            3    2    1 13 4    30.0 0.8000
11 1602  7 13 4  9 4  9  6 8  6 8  4    2 6  1 16      32.0 0.9231
10 1603  6 13 4  8    8       5    3    2    1 13 4    30.0 0.7500
12 1604                       5         2 6  1 15      32.0
11 1605  6  6 8  8    8 13 4       5    3    2         36.0 0.8000
 2 1607  6       8    8       6    4    3 4  2  4      40.0 0.8000
10 1607  5  6 8  8    8       5    4    2 8  2         40.0 0.8000
11 1608  5  6 8  8   10       5 6  4    3    2         40.0 0.9231
10 1609  5 13 4  8    7       5    3 4  2 6  1 16 0    36.0 0.7500
11 1610  6  6 8  8    7       5    3 4  2 6  2         40.0 0.7500
10 1611  5 16 8  8    8 13 4  5    3 4  2 6  2         40.0 0.8571
10 1613  7       9 4  8       6    4 6  3 4  2         36.0 0.7500
10 1614  6       8    8       6    4 6  2 6  2         36.0 0.8000
10 1615  7       9 4  9  6 8  6 8  4    3 4  2         40.0 0.9231
10 1616  6       8    9  6 8  6    4 6  3    2         36.0 0.9600
10 1617  6       8    8       6    5    3 4  2  6 8    40.0 0.8571
11 1618  6 10    9 4  8 10    6    5    3 4  2  2 0    40.0 0.9231
10 1619  5 13 4  8    8  6 8  5    4    2    2         40.0 0.9231
10 1620  4 10    6    6       4    2 8  2    2         40.0 0.7500
11 1621  7  6 8 10 8  9       6    4    2 8  2         40.0 0.9231
10 1622  8      10 8 10       6 8  6    3    2         40.0 1.0000
12 1623 12      16   12       8    5    3 4  1 16      36.0 1.2000
10 1624  6  6 8  8   11       6    4    2 6  2         36.0 1.0000
10 1625  6       8    8       5    3 4  2 6  2         36.0 0.8571
11 1626  5 13 4  8    7       4 2  3 4  2    2  5 0    36.0 0.8000
11 1628  6       9 4  8 10    5    3 4  2    2  6 8    42.0 0.9231
10 1629  8      10 8 10       6 8  5    2 6  2  6 8    42.0 1.0000
11 1630  9      10 8 10 13 4  8    6    3    2         40.0 1.0909
10 1631  6       8    9  6 8  6    4    2 8  2         40.0 1.0000
11 1632  6 13 4  9 4 10       6    4    2 8  2  6 8    44.0 1.0726
11 1633  7       9 4  9  6 8  6 8  4 2  2 8  2  6 8    44.0 1.0000
11 1634.07 13 4 10 8  8 13 4  6 8  5 0  3 4  2  8      42.0 0.9600
11 1636  8 13 4 12   12      10    8    2 8  2  6 8    40.0 1.3333
11 1637  8      10 8 10 13 4  6 8  5    4    2  5      40.0 1.1429
11 1638  6  6 8  8    8 13 4  6    5    3 4  2  6 8    40.0 0.9143
11 1639  5 13 4  8    8       5 4  4    2 8  2  3 4    40.0 0.8571
11 1640  5 13 4  8    7       5    4    2 8  2  5      40.0 0.7500
11 1641  8 10   10 8  9  6 8  8    6    3 4  2 14      48.0 1.0000
11 1642  9 16 8 13 4 12       6 8  5    3 4  2 14      48.0 1.2632
11 1643  6  7 8  9 4  9  6 8  6 8  5    3 4  2  6 8    40.0 1.0213
11 1644  6  6 8  8    8 13 4  6 8  5    3 4  2  3 4    40.0 0.9796
11 1647  7 13 4 10 8 10       7 6  6 3  4    4         66.0 1.0726 
11 1649 11  6 8 13 4 13  6 8 10    8 4  6 8  3  6 8    60.0 1.4545
11 1653 12 13 4 16   14      10    8 4  6 8  2 16 8    52.0 1.5000
12 1663  5 13 4 10 8  9       4 7  3    1 9  2  3      52.0 0.9697
12 1664  4 13 4  8    8       4 2  3 4  1 9  3         54.0 0.8571
99 9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
