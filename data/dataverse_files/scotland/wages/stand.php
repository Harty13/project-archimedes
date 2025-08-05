<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>St. Andrews daily wage-rates, 1693-1724</title>
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
<h4>St. Andrews daily wage-rates, 1693-1724</h4>

<p>
<a href="accounts.php">General notes on wages drawn from work accounts</a><br><br>

<a href="../geogdata/fife.php">Other Fife data</a><br><br>
Return to the <a href="../wagetop.php">Wage Data Directory</a></p>

<pre>INPUT 1 2 N  

 St. Andrews Daily Wage-Rates, 1693 - 1724

 From: Building accounts of St.&yuml;20Leonard's college, St. Andrews,
       held in St Andrews University Library

 This file contains;
 1 - Wrights' wages
 2 - Wrights' mens' (aka servant wrights') wages 
 3 - Masons' wages
 4 - Barrowmens' wages

FORMAT
1 1 1 1 3 0 0 0 (I4,4X,I3)
1 1 1 1 3 0 0 0 (I4,13X,I3)
1 1 1 1 3 0 0 0 (I4,22X,I3)
1 1 1 1 3 0 0 0 (I4,31X,I3)
STOP
Year  Wrights  Wrights  Masons   Barrowmen
                 Men
         d.       d.       d.       d.
DATA
1693    120               160       60
1694    120
1695                      160       60
1696                      160       48
1697    144               160       48
1699    120       96      120       60
1700    120               120       60
1701    120         
1702    120       96      120       60
1703    120
1704    120
1705    120
1706    144       96
1714    120       79      160
1717    160
1719    160      120      144       72
1723    160      120                79
1724                                72
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
