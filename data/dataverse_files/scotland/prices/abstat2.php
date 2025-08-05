<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Aberdeen Town Council Price Statutes; 1541 - 1701 (pt. 2)</title>
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
<h4>Aberdeen Town Council Price Statutes; 1541 - 1701 (pt. 2)</h4>

<ul>
<li><a href="stats.php">General notes on town council price statutes</a></li>
<li><a href="../geogdata/aber.php">Other 
Aberdeenshire (including Aberdeen town council) data</a></li>
<li><a href="abstat1.php">Aberdeen Town Council Price Statutes, part 1</a></li>
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
 1 - Men's double shoes (per pair); 1541-1616
 2 - Men's double shoes (per inch); 1611-1701
 3 - Men's boots (per pair); 1549-1616
 4 - Mutton (per bowk); 1647-1701
 5 - Flesher's mutton (per bowk);1582-1595
 6 - Butcher's mutton (per bowk);1582-1595
 7 - Moltin tallow (per stone); 1589-1701
 8 - Sheep tallow (per stone); 1547-1701
 9 - Nolt tallow (per stone); 1547-1701

FORMAT
1 2 1 1 3 0 0 0 (I2,1X,I4,1X,I3)
1 2 1 1 3 0 0 0 (I2,1X,I4,9X,I2)
2 2 1 1 2 3 0 0 (I2,1X,I4,14X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I2,1X,I4,20X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I2,1X,I4,26X,I2,1X,I1)
2 2 1 1 2 3 0 0 (I2,1X,I4,32X,I2,1X,I1)
2 2 6 1 2 3 0 0 (I2,1X,I4,39X,I3,1X,I1)
2 2 6 1 2 3 0 0 (I2,1X,I4,46X,I2,1X,I1)
2 2 6 1 2 3 0 0 (I2,1X,I4,52X,I2,1X,I1)
STOP
Date    Mens'  Mens'  Mens      Mutton             Tallow       
        double double boots ++++++++++++++++  +++++++++++++++++
        soled  soled            flesh- butch- moltin sheep nolt
        shoes  shoes            ers    ers
        (per   (per  (per  bowk bowk   bowk   st.    st.   st.  
        pair)  inch) pair)
Mo Year d.      d.   s.d.  s.d.  s.d.  s.d.   s. d.  s. d. s.d. 
DATA
10 1541  28
10 1547  30                 6 8                      10     8   
10 1549  30           8     6 8                      10     8
10 1550                     7 
10 1551  30                 7                        12    10
10 1552  30          12     6 8                      10     8   
10 1553                     5                 
10 1554  30                 5                        10     8   
10 1555  32                 6                        10     8   
10 1558  30                 5                        10     8   
10 1559  36                 6
10 1560  40          16     8                        14    12
10 1561  40                 8                        14    12
11 1562  40                14
10 1563  40                10                        14    12
10 1564  36          16    10                        14    12
10 1565                                              16    14
10 1566                     8
10 1567  36          16    12                        18    16
10 1568  36          16                              18    16
10 1569  36          16                              18    16
10 1570  36          16    10                        12    10
10 1571  48          20    10                        12    10
10 1572  48          20    10                        16    12
10 1573  48          20    10                        18    14
10 1574  48          20    12                        16    14
10 1575  48          16    10                        14    11   
10 1576  48          20    14                        14    11   
10 1577  48          20    14                        20    16   
10 1578  48          20    10                        18    13 4 
10 1579  66          24    13 4                      20    16
10 1580  60                13                        24    20
10 1581  60          24    13 4                      20    16
10 1582  60          24          15    12            20    16   
10 1583  80          32          15    12            24    18   
10 1584  80          32          15    10            24    18   
10 1585              33 4        15                  28    24   
 7 1586                    20
10 1586              30          16                  24    20
10 1587              30    16                        24    20
10 1588                          20
10 1589 108          33 4        20    18      26 8  26 8  20
10 1590 120          40          18    16      28    28    20   
10 1591                                        28    28    20   
10 1592 120          40          20            28    28    20   
10 1593                          24    20      33 4  33 4  24   
10 1595 144          46 8        20    20      36    36    26 8
10 1597 144          46 8  24                  33 6  33 6  26 8 
10 1598                    24                  33 4  33 4  26 8 
 6 1600                    30
11 1602 144                26 8                42    36 8  30   
10 1603                    33 4                42    36 8  30   
10 1604 144                26 8                42    36 8  30   
10 1605                    33 4                53 4  53 4  40   
11 1605 192          70
10 1606 192          70    26 8                50    50    36   
10 1607                    26 8                46 8  46 8  33 4 
10 1607 216          78
10 1609 192          70    33 4                46 8  46 8
10 1610                    33 4                46 8  46 8
10 1611                    33 4                53 4  53 4  40
12 1611         18
10 1613 192          66 8
10 1616 216          66 8
11 1626         18
11 1627         16
12 1628         18
10 1638         18
11 1639         24
11 1640                                              60    53 4
12 1641                                              60    53 4
 8 1642                                                         
10 1642                                              60    53 4 
10 1643                                                         
 5 1644                    48
 3 1648                    53 4   
11 1648                                              66 8  66 8 
10 1649         24         46                        73 4  66 8 
10 1650         24         46                        73 4  66 8 
10 1651         24         46                        66 8  60   
10 1652         24         46                        66 8  60   
10 1653         24         46                        66 8  60   
10 1654         24                                   66 8  60   
10 1656                    36                  80          66 8 
10 1657         30         36                  60    55    50   
10 1658         30         36                  80    60    53 4 
10 1659         30         32                  73 4  55    50
10 1660                    36                 106 8  58    53 4 
10 1661         24         34                  66 8  66 8  60   
10 1662         30         30                  66 8  58    53 4 
10 1663         30         30                  66 8  58    53 4 
10 1664         30         33 4                80    73 4  66 8 
10 1665         30         30                  66    58    53 4 
10 1666         30         26 8                73 4  66 8  60   
10 1667         30         24                  73 4  58    53 4 
10 1668         24         24                  73 4  58    53 4 
10 1669         24         24                  73 4  58    53 4 
10 1670         24         24                  73 4  58    53 4 
10 1671         24         24                  73 4  58    53 4 
10 1672         24         24                  73 4  58    53 4 
10 1673         24         24                  73 4  58    53 4 
10 1674         24         24                  73 4  53 4  50   
10 1675         24         24                  73 4  63 4  56   
10 1676         24         24                  73 4  63 4  56   
10 1677         24         26 8                73 4  60    53 4 
10 1678         24         26 8                93 4  80    93 4 
10 1679         26         29                  80    66 8  60   
10 1680         26         29                  80    66 8  60   
10 1681         24         26 8                80    66 8  60   
10 1682         16         26 8                80    66 8  60   
10 1683         16         26 8                80    66 8  60   
10 1684         16         26 8                66 8  60    53 4 
10 1685         16         26 8                73 4  60    53 4 
10 1686         16         26 8                73 4  60    53 4 
10 1687         16         26 8                73 4  60    53 4 
10 1688         16         26 8                73 4  60    53 4 
10 1689         16         26 8                73 4  60    53 4 
10 1697         24         26 8                      60    53 4 
10 1701         24         40                 100    66 8  66 8 
99 9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
