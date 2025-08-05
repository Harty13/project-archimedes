<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Edinburgh accounts of the Master of Works, 1529 - 1640</title>
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
<h4>Edinburgh accounts of the Master of Works, 1529 - 1640</h4>

<p>
<a href="accounts.php">General notes on wages drawn from work accounts</a><br><br>
<a href="../geogdata/edin.php">Other Edinburgh data</a><br>
<a href="edin1.php">Wages from Edinburgh town council accounts, 1502 - 1780</a><br><br>
Return to the <a href="../wagetop.php">Wage Data Directory</a></p>

<pre>INPUT 2 2 Y  

 Accounts of the Master of Works; Edinburgh, 1529 - 1640

 From: Paton, H.M., Accounts of the Master of Works, vol. 1, 
       1529-1615 (Edinburgh, 1957), and Imrie, J. & Dunbar, J.G.,
       Accounts of the Master of Works, vol. 2, 1616-1649 
       (Edinburgh, 1982)

 This file contains;
 1 - Workmens' daily wages, 1529 - 1639
 2 - Masons' daily wages, 1529 - 1640
 3 - Quariours' daily wages, 1529 - 1640
 4 - Sawers' daily wages, 1538 - 1640
 5 - Slaters' daily wages, 1540 - 1633
 6 - Smyths' daily wages, 1559 - 1640
 7 - Wrights' daily wages, 1529 - 1640

 Note: As discussed in the references given above, these wages are
       from actual accounts.  For further discussion of this type
       of wage data see Gibson & Smout, Prices, food and wages in 
       Scotland, 1550 - 1780 (CUP, 1994), Ch. 8.

 See also <a href="edin1.php">Edinburgh wage rates from Town Council accounts</a>.

FORMAT
1 1 1 1 3 0 0 0 (I4,1X,A1,2X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,8X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,14X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,20X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,26X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,32X,A1,I3)
1 1 1 1 3 0 0 0 (I4,1X,A1,38X,A1,I3)
STOP
Year s  Work- Mason Quar- Saw-  Slat- Smyth Wrights
     /  mens  wage  riour ers   ers   wage  wage
     w  wage        wage  wage  wage
DATA
1529 W
1529 S    12    28    20                    * 26
1530 W
1530 S    10    26    22                      28
1531 W                                        28
1531 S
1532 W
1532 S    12    36                            22
1535 W 
1535 S    10    28    16                      30
1536 W     9                                  30
1536 S    10    28                            30
1538 3
1538 S    20                18                28
1539 W    12    24          18                28
1539 S
1540 W
1540 S    10                      28
1559 W
1559 S    18    36                      36    36
1576 W
1576 S    26
1579 W
1579 S    26    60                            60
1580 W    26    60
1580 S
1599 W
1599 S    60                                 120
1611 W
1611 S                                       120
1613 W
1613 S    72   160
1614 W
1614 S    72   120                            96
1616 W    
1616 S    80   144   160   160         107   144
1617 W
1617 S    80   144         160   160   107   120
1618 W
1618 S    80   144                     107   107
1619 W
1619 S    80
1620 W
1620 S    80
1621 W
1621 S    80
1622 W
1622 S    80   144               160         107
1623 W
1623 S    80
1624 W
1624 S    80
1625 W
1625 S    80   160                    *107   107
1626 W    
1626 S    80   144   144              *107   107
1627 W
1627 S    80
1628 W  
1628 S    80   160         144         107   160
1629 W
1629 S    80   160                     120   120
1630 W
1630 S    80
1631 W
1631 S    80
1632 W
1632 S    80
1633 W
1633 S    80  *168   120        *160  *144  *144
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
1639 S    80   160   144   160         160   160
1640 W         160   144               160   160
1640 S
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
