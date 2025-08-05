<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Linlithgow accounts of the Master of Works, 1302, 1534 & 1616-40</title>
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
<h4>Linlithgow accounts of the Master of Works, 1302, 1534 & 1616-04</h4>

<p>
<a href="accounts.php">General notes on wages drawn from work accounts</a><br><br>
<a href="../geogdata/wloth.php">Other West Lothian (including Linlithgow) data</a><br><br>
Return to the <a href="../wagetop.php">Wage Data Directory</a></p>

<pre>INPUT 2 2 Y  

 Accounts of the Master of Works; Linlithgow, 1302, 1534 & 1616-40

 From: Paton, H.M., Accounts of the Master of Works, vol. 1, 
       1529-1615 (Edinburgh, 1957), and Imrie, J. & Dunbar, J.G.,
       Accounts of the Master of Works, vol. 2, 1616-1649 
       (Edinburgh, 1982)

 This file contains;

 1 - Workmens' Daily Wages; 1302, 1534 & 1616-40
 2 - Masons' Daily Wages; 1302, 1534, 1618-19,28,33
 3 - Slaters' Daily Wages; 1302, 1534 & 1616
 4 - Wrights' Daily Wages; 1534, 1618-19 & 1628-33

 Note: As discussed in the references given above, these wages are
       from actual accounts.  For further discussion of this type
       of wage data see Gibson & Smout, Prices, food and wages in 
       Scotland, 1550 - 1780 (CUP, 1994), Ch. 8.

FORMAT
1 1 1 1 3 0 0 0 (I4,1X,A1,3X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,10X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,17X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,24X,A1,I3)
STOP
Year w   Work-  Masons Slat-  Wrights
     /   mens   wages  ers    wages
     s   wage          wage  
DATA
1302 W
1302 S      3      4      4
1534 W
1534 S      8     24     28     27
1616 W
1616 S     80
1617 W
1617 S     80    
1618 W
1618 S     80    144     72    120
1619 W           96           144
1619 S     80
1620 W
1620 S     80
1621 W
1621 S     80
1622 W
1622 S     80
1623 W
1623 S     80
1624 W    
1624 S     80
1625 W
1625 S     80
1626 W
1626 S     80
1627 W
1627 S     80
1628 W
1628 S     80     96           160
1629 W
1629 S     80
1630 W
1630 S     80
1631 W
1631 S     80
1632 W
1632 S     80
1633 W  
1633 S     80   *180           144
1634 W
1634 S     80
1635 W
1635 S     80
1636 W
1636 S     80
1637 W
1637 S     80
1638 W    
1638 S     80
1639 W
1639 S     80
1640 W
1640 S     80
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
