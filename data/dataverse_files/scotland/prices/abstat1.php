<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Aberdeen Town Council Price Statutes; 1541 - 1701 (pt. 1)</title>
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
<h4>Aberdeen Town Council Price Statutes; 1541 - 1701 (pt. 1)</h4>

<ul>
<li><a href="stats.php">general notes on town council price statutes</a></li>
<li><a href="../geogdata/aber.php">Other 
Aberdeenshire (including Aberdeen town council) data</a></li>
<li><a href="abstat3.php">Aberdeen Town Council Price Statutes, part 3</a></li>
<li><a href="abstat4.php">Aberdeen Town Council Price Statutes, part 4</a></li>
<li>Return to the <a href="../pricetop.php">Price data directory</a>
</li>
</ul>

<pre>INPUT 3 2 N 

 Aberdeen Town Council Price Statutes; 1541 - 1701

 From; The minute books of the town council of aberdeen,
       volumes 17 - 58 (1541 - 1701), held at the Town House, 
       Aberdeen.  (Some price statutes were provided per. comm. by
       G. DesBrisay, who has since produced 'Authority and discipline 
       in Aberdeen, 1650-1700' (Unpublished University of Aberdeen 
       Ph.D. thesis, 1989).)

 This file contains;
 1 - Ale (per pint); 1543-1680
 2 - Beer (per pint); 1567-1680
 3 - Malt (per boll); 1581-1635 (gaps)
 4 - Wheat bread (per ounce); 1541- 1701
 5 - Wheat (per boll); 1581- 1630 (gaps)
 6 - Flour (per peck); 1597-1611 & 1665 

FORMAT
1 2 1 1 3 0 0 0 (I2,1X,I4,1X,I3)
1 2 1 1 3 0 0 0 (I2,1X,I4,5X,I3)
3 2 2 1 1 2 3 0 (I2,1X,I4,9X,I2,1X,I2,1X,I2)
1 2 4 2 3 0 0 0 (I2,1X,I4,18X,F5.3)
3 2 2 1 1 2 3 0 (I2,1X,I4,24X,I2,1X,I2,1X,I2)
2 2 3 1 2 3 0 0 (I2,1X,I4,33X,I2,1X,I2)
STOP
Mo Year Ale Beer  Malt  Cost of  Wheat  Flour
                 (boll) oz. of  (boll) (peck)
                         wheat              
                         bread               
        d.  d.  L. s. d.  d.   L. s. d. s. d.
DATA
10 1541                  0.111
 1 1542                  0.091
10 1543  16              0.100
10 1543                  0.111
 3 1544                  0.143
10 1544  16
 2 1545  16              0.182
 7 1546                  0.154
10 1546                  0.167
10 1547  16              0.100
 4 1549                  0.111
 8 1549                  0.143
10 1549  20
10 1550  20              0.154
10 1551  20              0.167
10 1552  16              0.143               
10 1553  12              0.100
10 1554  16              0.100
10 1555  16              0.125
10 1557                  0.143
10 1558  16              0.111
10 1559  16              0.125
10 1560  24              0.167
10 1561  24              0.200
11 1562  32              0.333
10 1563  32              0.222
10 1564  16              0.200
10 1566  20              0.167
10 1567  24  28          0.200
10 1568  24              0.200
10 1569  24  28          0.200
10 1570  24              0.200
10 1571  24  32          0.200
10 1572  24  32          0.250
10 1573  32  40          0.286
10 1574  32  40          0.286
10 1575  32  40          0.286
10 1576  32              0.222
10 1577  40  48          0.222
10 1578  40  60          0.222
10 1579  48  56          0.286
10 1580  48              0.286
10 1581  48  56  3  6  8 0.308  3  6  8
10 1582  40  48  2 10    0.308
10 1583  32  40          0.286
10 1583                  0.333
10 1584  48              0.333               
10 1585  68              0.429               
10 1586                  0.500
10 1587                  0.500
10 1588  48  56          0.429  4  
10 1589  48              0.429
10 1590  64  72          0.444               
10 1591                                      
10 1592  64  72          0.444               
10 1593  64  72  4  6  8 0.500  4  6  8      
10 1594  96      6 13  4 0.667  6 13  4 10
10 1595                  0.750  8
10 1597  96 112          1.000          13  4
10 1598  96 112  6 13  4 0.750  9
10 1599  96 112  6 13  4 1.000  8       10
11 1602 112
 6 1603                  1.000 10       13  4
10 1603  96 112  6       0.923          12   
 1 1604                  0.857
 3 1604                  0.800          12
10 1604  80      5       0.857          12
11 1605  96 112          0.857          12
10 1606  96 112          0.857 10       12   
10 1607  96 112  6       0.857
12 1608 160 192          0.857
10 1609  96      6       0.750  8
10 1610  96 112          0.667          10
11 1610                                      
10 1611 112 128  6       0.750  8       12
12 1612 128 144  8       0.615  6 13  4
10 1613 128 144          1.000  8            
 2 1614                                      
 5 1615                  1.091 10 13  4      
10 1615 128 144  8       1.091 10 13  4      
 1 1616                                      
10 1616 128 144  8       1.091 10 13  4
10 1617  96 112  6       0.857  8
10 1618 128              1.000 12
10 1619  96 128  6       1.000  8
10 1620  96 112  5  6  8 1.000  8
11 1621 128 144  8       1.000  8
 4 1622                  1.200 10
 8 1622 128      8
 6 1623                  1.500
 4 1624 144
 6 1624                  1.200
10 1624 128
12 1624  96      6       1.200
11 1625 128              1.000
11 1626  96      5       1.000  9
11 1627 128      6 13  4 1.000
12 1628 128 128          1.000
12 1629 128 128          1.500
10 1630 160 160          1.333 12 13  4
10 1631 128 128          1.333
11 1631  96  96          1.000
12 1632 128 128          1.333
 1 1634 160 160          1.333
10 1634 160 160          1.073
 1 1635                                      
 7 1635 192 192 10 13  4
12 1635 160 160          1.500
 4 1636 160 160          1.500               
11 1636 160 160          1.500
10 1637 128 128          1.200 
 3 1638                  1.091               
10 1638 128 128          1.091
11 1639 112 112          0.857
11 1640 128 128          1.000
12 1641 128 128 
 4 1642 160 160
 5 1642                                      
11 1642                                      
10 1643 128              0.965               
 2 1644 192
 3 1648 192 192          1.200
11 1648 192              1.500               
10 1649 192              1.600
10 1650 192              1.600
10 1651 192              0.857
10 1652 192              1.600               
 4 1653                  1.333               
10 1653 192              1.600               
10 1654                  0.857               
10 1656 192              0.857               
10 1657 192              0.923               
10 1658 192 192          1.091               
10 1659 192 192          1.200               
10 1660 192 192          1.200               
10 1661 192 192          1.091               
11 1664 192 192          1.091               
11 1665 192 192          1.000          16   
10 1666 192 192          0.857               
10 1667 192 192          0.857               
10 1668 192 192          0.857               
10 1669 192 192          0.857               
10 1670 192 192          0.857               
10 1671 192 192          0.857               
10 1672 192 192          1.000               
10 1673 192 192          1.000               
10 1674 192 192          0.800               
10 1675 192 192          0.960               
10 1676 192 192          1.333               
10 1677 192 192          0.923               
10 1678                  0.923               
10 1679 192 192          0.923               
10 1680 192 192          0.923               
10 1681                  0.857               
10 1682                  0.750               
10 1683                  0.750               
10 1684                  0.750               
10 1685                  0.857               
10 1686                  0.857               
10 1687                  0.857               
10 1688                  0.857               
10 1689                  0.857               
10 1697                  1.000               
10 1701                  1.000               
99 9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
