<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
<title>Age at Death in Edinburgh; 1740 - 1792 (pt. 1)</title>
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
<h4>Age at Death in Edinburgh; 1740 - 1792 (pt. 1)</h4>

<p>
<a href="source1.php">Source notes</a><br><br>

<a href="../geogdata/edin.php">Other Edinburgh data</a><br>
<a href="age2.php">Part 2 (age at death over 50)</a><br><br>

Return to <a href="../demogtop.php">Demographic Data directory</a></p>

<pre>INPUT 1 2 N  
 
 Age at Death in Edinburgh; 1740 - 1792 (pt. 1)
    Being the number of individuals in the given age bands
    under 50, and the total number dying aged 50 or less, who
    were buried in Edinburgh churchyards.
 
 From: The Scots Magazine monthly Bills of Mortality tables
 
 This file contains;
 
 1 - No. dying aged less than two years
 2 - No. dying aged 2 - 5 years
 3 - No. dying aged 5 - 10 years
 4 - No. dying aged 10 - 20 years
 5 - No. dying aged 20 - 30
 6 - No. dying aged 30 - 40 years
 7 - No. dying aged 40 - 50 years
 8 - No. dying aged less than 50 years

FORMAT
1 2 1 1 3 0 0 0 (I4,2X,I3)
1 2 1 1 3 0 0 0 (I4,7X,I3)
1 2 1 1 3 0 0 0 (I4,12X,I3)
1 2 1 1 3 0 0 0 (I4,17X,I3)
1 2 1 1 3 0 0 0 (I4,22X,I3)
1 2 1 1 3 0 0 0 (I4,27X,I3)
1 2 1 1 3 0 0 0 (I4,32X,I3)
1 2 1 1 3 0 0 0 (I4,37X,I4)
STOP
Year  0-2  2-5  5-10 10-20 20-30 30-40 40-50  Total less than 50
DATA
1740  435  198   53   26   45   64  104   925

1741  562  269   93   51   60   96  128  1259
1743  450  204   59   55   62   83  103  1016
1744  410  200   63   43   74  103  102   995
1745  538  161   61   68  102  133  112  1175
1746  664  138   72   86  148  199  126  1433
1747  449   88   47   47   91  109  113   944
1748  458   99   55   70   99  153  120  1054
1749  443  115   41   55   72  102   92   920
1751  434   78   44   69  133  158  126  1042
1752  461  126   68   58   87  107   97  1004
1753  351   94   66   58   85  119  135   908
1754  355  129   69   63   97  131  157  1001
1755  359   90   62   78   97  142  139   967
1756  421  106   87   76   94  126  126  1036
1757  337  115   80   97  105  113  142   989
1758   85  118   79  104  100   88  120   694
1759  174  123   94   86  110   96  137   820
1760  156   85   33   44   40   74  180   612
1761  146   86   17   22   16   32  141   460
1762  172  129   69   47   48   58  129   652
1763  188   90   34   23   26   44  128   533
1764  183  119   51   49   26   65   89   582
1765  196  143   61   39   37   53  165   694
1766  244   60   50   38   48   59   57   556
1767  238  118   96   83   83   91   73   782
1768  132   98   76   91   94   88   81   660
1769  178  164  123  120  119   84   99   887
1770  433  125   78   68   79   69   85   937
1771  362  110   84   72   78   84  109   899
1772  408  148   92   58   64   65   59   894
1773  380  112   73   56   58   70   76   825
1774  500  154   89   58   64   74   70  1009
1775  337  113   68   55   60   71   80   784
1776  380  118   70   51   56   73   70   818
1777  310  121   64   45   44   54   69   707
1778  212   90   50   45   36   40   53   526
1779  206   77   49   40   42   49   51   514
1780  214   88   50   40   39   44   57   532
1781  214   86   44   30   34   31   42   481
1782  255  109   64   35   32   37   50   582
1783  198   87   46   32   34   31   43   471
1784  272  117   58   47   38   41   49   622
1785  201   90   44   42   34   37   51   499
1786  253   88   45   45   48   46   49   574
1787  638  175   93   82  111  126  142  1367
1788  749  205  110   93  131  157  135  1580
1789  722  247  105  113  136  143  140  1606
1790  653  216   99   93  128  143  157  1489
1791  927  380  133  116  114  156  161  1987
1792  664  253  116   75   94  133  150  1485
9999
</pre>
		<div class="top"><a href="#top">top</a></div>
	</div>
</div>
	
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
