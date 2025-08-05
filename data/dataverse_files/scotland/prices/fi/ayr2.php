<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Ayrshire fiars, 1667-1671, 1691-1697, & 1740-1780</title>
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
			<dd><a href="/hpw/">Index</a>
				<dl class="sub">
				<dd><a href="../../">Scottish Database</a></dd>
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
<h4>Ayrshire fiars, 1667-1671, 1691-1697, & 1740-1780</h4>
<p>
<a href="fiars.php">General discussion of the fiars</a><br><br>

<a href="../../geogdata/ayr.php">Other Ayrshire data</a><br>
<a href="ayr1.php">Ayrshire fiars, pt 1</a><br>
<a href="ayr3.php">Ayrshire fiars, pt 3</a><br><br>

Return to the <a href="../../pricetop.php">Price Data Directory</a></p>


<pre>INPUT 1 2 N  

 Ayrshire fiars, 1667 - 1671, 1691 - 1697, and 1740 - 1780.

 From: 1) 1667-1671, 1697 & 1740-1780; 
          Scottish Record Office, GD 25/9/box1
       2) 1691-1696;  Scottish Record Office, GD 109/3943

 This file contains;
 1 - Oatmeal prices; 1667-1780 (gaps)
 2 - Bere prices; 1667-1780 (gaps)
 3 - Wheat prices; 1740-1780
 4 - White corn prices; 1740-1780
 5 - Grey corn prices; 1740-1780

 Note: For the years 1740-1780 the different boll measures are defined
       in the source as;
         Boll of oatmeal     -  140 lbs  
         Boll of bere        -  8 Winchester bushels
         Boll of wheat       -  4 Winchester bushels
         Boll of white corn  -  8 Winchester bushels
         Boll of grey corn   -  8 Winchester bushels

FORMAT
3 2 2 1 1 2 3 0 (I4,1X,I2,1X,I2,1X,I1)
3 2 2 1 1 2 3 0 (I4,9X,I2,1X,I2,1X,I1)
3 2 2 1 1 2 3 0 (I4,17X,I2,1X,I2,1X,I1)
3 2 2 1 1 2 3 0 (I4,25X,I2,1X,I2,1X,I1)
3 2 2 1 1 2 3 0 (I4,33X,I2,1X,I2,1X,I1)
STOP
Crop Oatmeal   Bere   Wheat   White   Grey
Date                          corn    corn
DATA
1667  4 13 4  5
1668  4       5
1669  3 10    4 10
1670  5  6 8  5
1671  5 16 8  6
1691  4 16 8  4
1692  5       4 16 8 
1693  5 11 8  6
1694  6 13 4  6  6 8
1695  7 16 8  7
1696 12       9
1697  7       6
1740 10      11 04 0 13 04 0 09 12 0 06 08 0
1741  6       7 12    7 16    6  8    5
1742  4 10    5 12    6 10    4 16    4 16
1743  3 12    4  1 9  5  4    4       2 16
1744  6 13 4  7 12    8      10 13 4  4
1745  9      10 16    9 12    9 12    6
1746  6  8    7 16    7  4    6 13 4  5  6 8
1747  5  8    6       6 16    5  4    4
1748  5 12    7 16    8  8    5  6 8  4
1749  6       6 12    8       6       4
1750  6 13 4  7 16    9 12    6 13 4  4
1751  7 10    9 12    9 12    7 12    4 16
1752  7  4    8  8    9 12    7  4    4 16
1753  8      10       9       7  4    4 16
1754  6 12    8       8  8    6  8    4  5 4
1755  7 12    9 12    9 12    8       6
1756 10  8   12 12   14  8    9 12    7  4
1757  8  8   10 16   13  4    9 12    7  4
1758  5  4    6       9 12    5 12    4
1759  5  4    6       8  8    5  4    4
1760  6  6    6  8    9       6  8    4
1761  7  4    8 12    9 12    7 10    5  4
1762  9 12   10      12      10       6  8
1763  7  4    9  4   10 16    7 12    5  4
1764  7 12    9  8   12       7 12    5  4
1765 10 16   13  4   12 12   11  8    7 12
1766  9 12   12 12   12 12   10 16    7  4
1767  8 16   11  8   11  8   10 10    6  8
1768  7  4    7  4   12       8       4
1769  9      12      10 16    9 12    4 16
1770  9  4   11 12   10  4    9 12    4 16
1771  9 12   14      12 12    9  6    6
1772  8 16   11  8   13 16    8 16    5  8
1773  9  4   12 12   13  4    9 16    5  8
1774  8  8   11  8   12 12    9 12    6
1775  6 16   10      12       8       4 16
1776  7  4    9      11  8    8  8    5  8
1777  8      11  8   13 16    8  8    4 16
1778  8      10 16   11  8    9  4    6
1779  6 12    9  6    9 12    7  4    6
1780  8       9 12   11  8    8       6
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
