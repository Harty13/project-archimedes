<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Age at Death in Edinburgh; 1740 - 1792 (pt. 2)</title>
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
<h4>Age at Death in Edinburgh; 1740 - 1792 (pt. 2)</h4>

<p>
<a href="source1.php">Source notes</a><br><br>

<a href="../geogdata/edin.php">Other Edinburgh data</a><br>
<a href="age1.php">Part 1 (age at death less than 50)</a><br><br>

Return to <a href="../demogtop.php">Demographic Data directory</a></p>

<pre>INPUT 1 2 N 

 Age at Death in Edinburgh; 1740 - 1792 (pt. 2)
    Being the number of individuals in the given age bands
    over 50, and the total number dying aged 50 or more, who
    were buried in Edinburgh churchyards.
 
 From: The Scots Magazine monthly Bills of Mortality tables
 
 This file contains;
 
 1 - No. dying aged 50 to 60 years
 2 - No. dying aged 60 to 70 years
 3 - No. dying aged 70 to 80 years
 4 - No. dying aged 80 or more
 5 - No. dying aged 50 or more

FORMAT
1 2 1 1 3 0 0 0 (I4,2X,I3)
1 2 1 1 3 0 0 0 (I4,7X,I3)
1 2 1 1 3 0 0 0 (I4,12X,I3)
1 2 1 1 3 0 0 0 (I4,17X,I3)
1 2 1 1 3 0 0 0 (I4,22X,I4)
STOP
Year  50-  60-  70-  80+  Total
       60   70   80        >50
DATA
1740   96   98   98   23   315
1741  107  122   88   43   360
1743   92  132   98   41   363
1744   93   97   84   40   314
1745  110   97   58   23   288
1746  122   93   48   36   299
1747   97   79   40   40   256
1748   93   66   44   29   232
1749   85   61   42   24   212
1751   89   52   31   27   199
1752   74   56   30   23   183
1753   89   52   33   23   197
1754  101   58   34   21   214
1755  112   54   34   20   220
1756  121   78   49   32   280
1757  114   76   55   33   278
1758   97   82   83   45   307
1759  122   97   62   35   316
1760  178  179  117   37   511
1761  155  159   89   40   443
1762  214  232  175   32   653
1763  202  205  203   17   627
1764  190  166   98    1   455
1765  200  183  155   18   556
1766   82  145  153  115   495
1767   98   89   68   28   283
1768  101   71   54   39   265
1769  113   46   35   24   218
1770   93   90   65   68   316
1771  109  101   85   56   351
1772   78   95   68   46   287
1773   99   80   60   43   282
1774   87  105   79   71   342
1775   92   98   91   46   327
1776   73   95   74   51   293
1777   66   77   74   64   281
1778   59   61   46   28   194
1779   55   82   73   34   244
1780   56   70   61   34   221
1781   43   60   38   20   161
1782   59   73   60   29   221
1783   51   55   40   25   171
1784   60   56   50   17   183
1785   55   58   46   25   184
1786   56   64   38   20   178
1787  135  135  133   57   460
1788  156  190  140   58   544
1789  157  137  126   49   469
1790  149  186  127   53   515
1791  176  226  134   69   605
1792  189  167  117   65   538
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
