<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Scottish Economic History Database; File structure and codes</title>
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
<h4>File structure and codes</h4>

<p>
The Scottish Economic History Database comprises over 550 price, wage and other time-series held in about 130 separtate files.</p>

<p>
In most cases there is a separate file for each source, although as their was an initial constraint of only 9 data-series per file, in some cases a particular source may extend over a number of separate files. Pointers to such files are always provided. Conversely, for reasons of convenience in a few cases individual files may contain data drawn from a number of separate, but always related, sources. This is also always made clear in the files concerned.</p>

<p>
The layout of all files as they appear on screen follows a standard format and comprises the following nine sections;</p>

<ol>
<li>HTML-specific header comprising;

	<ul>
<li>Title</li>
<li>Links to associated files and directories (including, if appropriate, source descriptions)</li>
	</ul></li>

<li>Coded line describing general data chracteristics</li>
<li>File title</li>
<li>Data source(s)</li>
<li>Text description of the file's contents (optional)</li>
<li>Format statements and coded descriptions for each series held on the file</li>
<li>Column headers (optional)</li>
<li>Data series</li>
<li>File terminator (9999 in date column)</li>
</ol>

<p>
The particular structure of the files reflects the fact that they were created for use with a suite of data management, analysis and presentation programs written in FORTRAN. To these original data files has been added the first section of HTML-specific information.</p>

<p>
With the exception of the coded information, the nine sections are self-explanatory.  The two coded sections provide the following information;</p>

<ol>
<li>A coded line containing general data chracteristics; this always starts with the word INPUT.
<p>
The word INPUT is then followed by three integers;</p>

<ul>
<li>a: how the data is represented, where;

	<ul>
<li>1  -  Just year, as an integer (ie 1701)</li>
<li>2  -  Year and season, with S = summer and W = winter  (ie 1701 S)</li>
<li>3  -  Month and year (ie 10 1701)</li>
<li>4  -  Just year, as a real number (ie 1700.00)</li>
	</ul></li>

<li>b: the currency (if appropriate) in which the data is provided
	<ul>
<li>1  -  Sterling</li>
<li>2  -  Scots  (Note: 1 shilling Scots = 1 penny Sterling)</li>
	</ul></li>
<li>c: whether a 'small sample' symbol is used to highlight an average price/wage derivied from a limited number of quotations
	<ul>
<li>Y  -  Yes</li>
<li>N  -  No</li>
	</ul></li>
</ul></li>
<li>A coded line for each data-series in the file<br><br>

There is one line for each data-series, with the first line corresponding to the first series as read from left to right in the actual data section of the file.  Each line of code contains eight integers followed by a FORTRAN format statement describing the position of the column or columns which make up the data series.  The coded entries are as follows;

<ol>
<li>a:  The number of columns used by the data-series (maximum = 4)</li>
<li>b:  The type of data, where;
	<ul>
<li>1  -  Wages</li>
<li>2  -  Prices (or other)</li>
	</ul></li>
<li>c:  The data unit, where;
	<ul>
<li>1  -  If prices or other (b=2), price per unspecified unit;  if wages (b=1), wage per day</li>
<li>2  -  If prices or other (b=2), price per boll; if wages (b=1), wage per week</li>
<li>3  -  If prices or other (b=2), price per peck; undefined for use with wages (b=1)</li>
<li>4  -  If prices or other (b=2), price per ounce; undefined for use with wages (b=1)</li>
<li>5  -  If prices or other (b=2), price per pound; undefined for use with wages (b=1)</li>
<li>6  -  If prices or other (b=2), price per stone; undefined for use with wages (b=1)</li>
	</ul></li>
<li>d:  The data format, where;
	<ul>
<li>1  -  Integer</li>
<li>2  -  Floating point</li>
	</ul></li>
<li>e: Column one is?
	<ul>
<li>1  -  Pounds</li>
<li>2  -  Shillings</li>
<li>3  -  Pence</li>
<li>4  -  Twelfths of pence (sometimes used when Sterling is the currency of account)</li>
	</ul></li>
<li>f  to h:  Column 2 to 4 are?
	<ul>
<li>0  -  Not applicable</li>
<li>1  -  Pounds</li>
<li>2  -  Shillings</li>
<li>3  -  Pence</li>
<li>4  -  Twelfths of pence (sometimes used when Sterling is the currency of account)</li>
	</ul></li>
<li>i:  FORTRAN format statement identifying location of column(s) used</li>
</ol>

</ol>
<p>
Return to <a href="notes.php">User Notes.</a></p>

		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
