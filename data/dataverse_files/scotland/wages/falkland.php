<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Falkland accounts of the Master of Works, 1532-1540, 1616-1640</title>
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
<h4>Falkland accounts of the Master of Works, 1532-1540, 1616-1640</h4>

<p>
<a href="accounts.php">General notes on wages drawn from work accounts</a><br><br>
<a href="../geogdata/fife.php">Other Fife data</a><br><br>
Return to the <a href="../wagetop.php">Wage Data Directory</a></p>

<pre>INPUT 2 2 Y  

 Falkland Wages; 1532-1540 (gaps), 1616-1640

 From: Paton, H.M., Accounts of the Master of Works, vol. 1, 
       1529-1615 (Edinburgh, 1957), and Imrie, J. & Dunbar, J.G.,
       Accounts of the Master of Works, vol. 2, 1616-1649 
       (Edinburgh, 1982)

 This file contains;

 1 - Workmens' daily wages; 1532,37-40 & 1616-40
 2 - Masons' daily wages; 1537-40 & 1629
 3 - Quarriours' daily wages; 1537-40 & 1628-29
 4 - Sawers' daily wages; 1538-39 & 1628-29
 5 - Slaters' daily wages; 1538 & 1628-29
 6 - Wrights' daily wages; 1538-39 & 1628-29

Note: There is great variation in the rates given for
      all but workmen throughout these accounts.

FORMAT
1 1 1 1 3 0 0 0 (I4,1X,A1,2X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,8X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,14X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,20X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,26X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,32X,A1,I3)
STOP
Year s  Work- Mason Quar- Saw-  Slat- Wrights
     /  mens  wage  riour ers   ers   wage
     w  wage        wage  wage  wage
DATA
1532 W
1532 S    12
1537 W          24
1537 S    10        * 16
1538 W    10    24  * 16
1538 S    10    28          36    36    28
1539 W     8    20  * 16
1539 S    10    24  * 28    26          28
1540 W    10  * 24  * 22                20
1540 S    10  * 28  * 22                20
1616 W
1616 S    80
1617 W
1617 S    80
1618 W
1618 S    80
1619 W    
1619 S    80
1620 W
1620 S    80
1621 W
1621 S    80
1622 W
1622 S    80
1623 W
1623 S    80
1624 W   
1624 S    80
1625 W
1625 S    80
1626 W
1626 S    80
1627 W
1627 S    80
1628 W
1628 S    80         133   107   133  *160
1629 W
1629 S    80   160   133   107   160   160
1630 W
1630 S    80
1631 W
1631 S    80
1632 W
1632 S    80
1633 W
1633 S    80
1634 W
1634 S    80
1635 W
1635 S    80
1636 W  
1636 S    80
1637 W
1637 S    80
1638 W    
1638 S    80
1639 W
1639 S    80
1640 W
1640 S    80
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
