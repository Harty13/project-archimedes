<?php
header("Location: https://iisg.amsterdam/en/research/projects/hpw/calculate.php",TRUE,301);
exit('go to <a href="https://iisg.amsterdam/en/research/projects/hpw/calculate.php">new website</a>');
?>








<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
	<title>Datafiles of Historical Prices and Wages</title>
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
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/menu-hpw.inc.php"; ?>
		</dl>
		<dl id="email">
			<dd>Email: <?php require_once "_email_hpw.inc.php"; ?></dd>
		</dl>
	</div>
	<div class="navthird">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/search-ghome-sochist.inc.php"; ?>
		<dl id="also">
			<dt>See also</dt>
			<dd><a href="/research/">Research</a></dd>
			<dd><a href="/indonesianeconomy/">Indonesian Economic Development</a></dd>
			<dd><a href="https://www.neha.nl/">Netherlands Economic History Archive</a></dd>
		</dl>
	</div>
	<div class="content">

<h2>List of Datafiles</h2>

<p>See also: <a href="link.php">Index to websites</a></p>

<p>
<a href="#world">World</a><br><br>

<a href="#africa">Africa</a> | <a href="#egypt">Egypt</a> | <a href="#southafrica">South Africa</a><br><br>

<a href="#asia">Asia</a> | <a href="#babylon">Babylon</a> | <a href="#china">China</a> | <a href="#india">India</a> | <a href="#indonesia">Indonesia</a> | <a href="#japan">Japan</a> | <a href="#korea">Korea</a> | <a href="#singapore">Singapore</a> | <a href="#srilanka">Sri Lanka</a> | <a href="#thailand">Thailand</a><br><br>

<a href="#europe">Europe</a> | <a href="#austria">Austria</a> | <a href="#belgium">Belgium</a> | <a href="#denmark">Denmark</a> | <a href="#france">France</a> | <a href="#germany">Germany</a> | <a href="#hungary">Hungary</a> | <a href="#ireland">Ireland</a> | <a href="#italy">Italy</a> | <a href="#netherlands">The Netherlands</a> | <a href="#ottoman">Ottoman Empire</a> | <a href="#poland">Poland</a> | <a href="#portugal">Portugal</a> | <a href="#russia">Russia</a> | <a href="#scotland">Scotland</a> | <a href="#spain">Spain</a> | <a href="#sweden">Sweden</a> | <a href="#switzerland">Switzerland</a> | <a href="#united">United Kingdom</a><br><br>

<a href="#northamerica">North America</a> | <a href="#canada">Canada</a> | <a href="#unitedstates">United States</a><br>
<a href="#southamerica">South America</a> | <a href="#brazil">Brazil</a> | <a href="#chile">Chile</a> | <a href="#colombia">Colombia</a> | <a href="#peru">Peru</a><br><br>

<a href="#oceania">Oceania</a> | <a href="#australia">Australia</a></p>

<hr width="300" size="1" noshade>

<h5><a name="world"><em>World</em></a></h5>
<p>
<em>Allen-Unger Global Commodity Prices Dataset</em><br>
-&nbsp; Authors: Robert C. Allen & Richard W. Unger<br>
-&nbsp; About this dataset: <a href="allen-unger_about.pdf">About</a><br>
-&nbsp; The datafiles: <br>
&nbsp;&nbsp;&nbsp;Commodities <a href="allen-unger-commodities.php">csv files by commodity</a><br>
&nbsp;&nbsp;&nbsp;Markets <a href="allen-unger-markets.php">csv files by market</a><br>
&nbsp;&nbsp;&nbsp;Currencies <a href="currency.xlsx">xlsx file</a><br>
&nbsp;&nbsp;&nbsp;Measures <a href="measures.xls">xls file</a><br>
&nbsp;&nbsp;&nbsp;Beer Excise <a href="beer_excise.zip">zip file</a>
</p>

<p>
<em>Just before the metre, the gram, the litre. Building a Rosetta Stone of Weights and Measures in the Early Modern World</em><br>
-&nbsp; Bob Allen and Tommy E. Murphy<br>
-&nbsp; <a href="http://www.nuff.ox.ac.uk/users/murphy/measures/before_metre.htm">The datafile</a> - available at website of Department of Economics and Nuffield College</p>

<p>
<em>Inflation 1800-2000</em><br>
-&nbsp; Author: Coos Santing<br>
-&nbsp; The datafile: <a href="inflation-1800-2000.xls">spreadsheet</a> <span class="small">(.xls, 660 Kb)</span></p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="africa"><em>Africa</em></a></h5>
<p>
<em>Wages, prices and welfare ratios in colonial Africa, 1880-1965</em><br>
-&nbsp; Authors: Ewout Frankema and Marlous van Waijenburg<br>
-&nbsp; About this datafile: The data are explained and applied in Frankema, Ewout and Marlous Van Waijenburg. "Structural Impediments to African Growth? New Evidence from Real Wages in British Africa, 1880-1965", forthcoming in the <em>Journal of Economic History</em>. An earlier extended version appeared under this title as a Center for Global Economic History Working Paper (2011).
<!-- further reading is provided in E. Frankema and M. van Waijenburg, <a href="http://www.cgeh.nl/sites/default/files/WorkingPapers/CGEH.WP_.No2_.FrankemavanWaijenburg.jan2011.pdf">African Real Wages in Asian Perspective, 1880-1940</a>, CGEH Working Paper 2 --><br>
-&nbsp; The datafiles: <br>
&nbsp;&nbsp;&nbsp;Gambia - <a href="gambia-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 104 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Gold Coast - <a href="goldcoast-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 112 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Kenya - <a href="kenya-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 93 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Mauritius - <a href="mauritius-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 98 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Nigeria - <a href="nigeria-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 115 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Nyasaland - <a href="nyasaland-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 93 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Sierra Leone - <a href="sierraleone-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 112 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Tanganyika - <a href="tanganyika-wages-prices-welfare-ratio.xlsx">spreadsheet</a> <span class="small">(.xls, 33 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Uganda - <a href="uganda-wages-prices-welfare-ratio.xls">spreadsheet</a> <span class="small">(.xls, 88 Kb)</span><br></p>


<h5><a name="egypt">Egypt</a></h5>
<p>
<em>Cairo wages and grain prices, 1400-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Cairo_wages_wheat_1400-1800.xls">spreadsheet</a>, available at GPIH-website</p>

<h5 id="southafrica">South Africa</h5>
<p>
<em>Wages and Prices in South Africa</em><br>
-&nbsp; Author: Pim de Zwart<br>
-&nbsp; About these datafiles: further reading is provided in Pim de Zwart, <a href="southafrica-wages-prices.pdf">Appendix to the data on Wages and Prices in South Africa, 1835-1910</a> - <span class="small">pdf, 46 Kb.</span><br>
-&nbsp; The datafiles: <br>
&nbsp;&nbsp;&nbsp;South African Wages, 1835-1910 - <a href="southafrica-wages_1835-1910.xlsx">spreadsheet</a> <span class="small">(.xlsx, 282 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Cape Colony Price Index, 1835-1910 - <a href="cape-colony-price-index_1835-1910.xls">spreadsheet</a> <span class="small">(.xls, 790 Kb)</span><br>
&nbsp;&nbsp;&nbsp;Natal Price Index, 1835-1910 - <a href="natal-price-index_1850-1910.xls">spreadsheet</a> <span class="small">(.xls, 560 Kb)</span>.</p>

<h5><a name="asia"><em>Asia</em></a></h5>
<p>
<em>General level of wages in Asia</em><br>
-&nbsp; Source: International Labour Office, Year book of Labour Statistics 1935-1955<br>
-&nbsp; The datafile: <a href="ilowagesasia.xls">spreadsheet</a> <span class="small">(.xls, 27.5 Kb)</span></p>

<h5><a name="babylon">Babylon</a></h5>
<p>
<em>Commodity prices in Babylon 385-61 BC</em><br>
-&nbsp; Author: R.J. van der Spek<br>
-&nbsp; <a href="babylon.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="babylonia.xls">spreadsheet</a> <span class="small">(.xls, 1.15 Mb)</span></p>

<h5><a name="china">China</a></h5>
<p>
<em>Regulated wages paid by the state in public construction. Data from</em> Wuliao jiazhi zeli <em>(Regulations and precedents on the prices of materials) for 15 Chinese provinces from 1769 to 1795</em><br>
-&nbsp;Compilers: Chen Chaoyong (Gansu, Shanxi, Jiangsu, Yunnan), Chen Jing (Shandong, Manchuria, Guangdong), Juliane Kiefner (Zhili, Hunan), Christine Moll-Murata (Fujian, Rehe, Zhili, Hunan, Henan), Zhang Wenliang and Ma Debin (Sichuan, Zhejiang, Henan)<br>
-&nbsp;<a href="wuliao.php">About these datafiles</a><br>
-&nbsp; The datafiles are divided in 2 separate files:<br>
&nbsp;&nbsp;Wuliao jiazhi zeli - <a href="wuliao.xls">spreadsheet</a> <span class="small">(.xls, 878 Kb)</span><br>
&nbsp;&nbsp;Rehe - <a href="rehe.xls">spreadsheet</a> <span class="small">(.xls, 20 Kb)</span></p>

<p>
<em>Regulated wages paid by the state in public construction at the capital, 1659-1736, according to the</em> Huidian shili <em>(Collected statutes and factual precedents), 1899, and the</em> Jiuqing yiding wuliao jiazhi <em>(Prices of materials decided by the nine ministers)</em><br>
-&nbsp;Compiler: Christine Moll-Murata<br>
-&nbsp;<a href="huidian-jiuqing.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="huidian-jiuqing.xls">spreadsheet</a> <span class="small">(.xls, 25 Kb)</span></p>

<p>
<em>Wages for construction workers in public service (c. 1766) paid for construction in the imperial villa Yuanming yuan Garden of Perfect Brightness outside Peking</em><br>
-&nbsp;Compiler: Christine Moll-Murata<br>
-&nbsp;<a href="yuanmingyuan.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="yuanmingyuan.xls">spreadsheet</a> <span class="small">(.xls, 17 Kb)</span></p>

<p>
<em>Wages for armament, military equipment, and shipbuilding workers, 1769 and 1816</em><br>
-&nbsp;Compiler: Christine Moll-Murata<br>
-&nbsp;<a href="wages-armament.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="wages-armament.xls">spreadsheet</a> <span class="small">(.xls, 21 Kb)</span></p>

<p>
<em>Wages for silk weaving in Suzhou and Peking, 1686 and 1752</em><br>
-&nbsp;Compiler: Christine Moll-Murata<br>
-&nbsp;<a href="suzhou-peking.php">About this datafile</a><br>
-&nbsp; The datafiles:<br>
&nbsp;&nbsp;Suzhou - <a href="suzhou.xls">spreadsheet</a> <span class="small">(.xls, 18 Kb)</span><br>
&nbsp;&nbsp;Peking - <a href="peking.xls">spreadsheet</a> <span class="small">(.xls, 16 Kb)</span></p>

<p>
<em>Wages for printing and bookbinding in the Peking Imperial Printery Wuying dian (Hall
of Military Fame), 1694 to 1851</em><br>
-&nbsp;Compiler: Christine Moll-Murata<br>
-&nbsp;<a href="wages-printing.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="wages-printing.xls">spreadsheet</a> <span class="small">(.xls, 33 Kb)</span></p>

<p>
<em>Wages paid on the free market: various industries, China-wide, between 1735 and 1820</em><br>
-&nbsp;Compilers: Ma Debin and Zhang Wenliang, revised by Christine Moll-Murata<br>
-&nbsp;<a href="wages-various.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="wages-various.xls">spreadsheet</a> <span class="small">(.xls, 70 Kb)</span></p>

<p>
<em>Rice prices, 961-1910</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/China_rice_prices_%20961-1910.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Canton and Macao, 1704-1833</em><br>
-&nbsp;Compiler: Paul A. Van Dyke<br>
-&nbsp; About this datafile: further reading is provided in Paul A. Van Dyke, <a href="canton.pdf"><em>Description of Price and Wage Data from Canton and Macao 1704-1833</em></a> - pdf, 111 Kb.<br>
-&nbsp; The datafiles:<br>
&nbsp;&nbsp;Prices - <a href="canton-prices.xls">spreadsheet</a> <span class="small">(.xls, 1.4 Mb)</span><br>
&nbsp;&nbsp;Wages - <a href="canton-wages.xls">spreadsheet</a> <span class="small">(.xls, 121 Kb)</span></p>

<h5><a name="india">India</a></h5>
<p>
<em>Monthly cost of living product prices and index in Bombay, 1921-1940</em><br>
-&nbsp;Source: <em>Labour gazette</em>, Government of Maharastra: Office of the Commissioner of Labour Bombay, vol I (1921)-Vol XX (1940, Feb)<br>
-&nbsp;<a href="india.php">About this datafile</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li>India cost of living 1921-1937 <a href="india1921-1937.xls">spreadsheet</a> <span class="small">(.xls, 167 Kb)</span></li>
<li>India cost of living 1937-1940 <a href="india1937-1940.xls">spreadsheet</a> <span class="small">(.xls, 286 Kb)</span></li></ul>

<p>
<em>Prices, wages, crop yields and land revenues in the Mughal Empire, from c. 1595 onwards</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Mughal_Empire_c1595_later.xls">spreadsheet</a>, available at GPIH-website </p>

<p>
<em>Pune prices, wages and transportation costs, 1796-1831</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Pune_1796-1831.xls">spreadsheet</a>, available at GPIH-website </p>

<p>
<em>Commodity prices in Sri Lanka and Southern India, 1677-1790</em><br>
-&nbsp; Author: Christiaan van Bochove<br>
-&nbsp; About this datafile: further reading is provided in Christiaan van Bochove, <a href="voc-srilanka-southernindia.pdf">Prices in Sri Lanka and Southern India during the pre-industrial period</a> <span class="small">(.pdf,  479Kb)</span><br>
-&nbsp; The datafile: <a href="voc-srilanka-southernindia.xls">spreadsheet</a> <span class="small">(.xls, 1.7Mb)</span></p>

<h5><a name="indonesia">Indonesia</a></h5>
<p>
<em>Monthly rice prices on Java (Batavia, Semarang, and Surabaya) 1824-1855</em><br>
-&nbsp; Author: Jan Luiten van Zanden<br>
-&nbsp;<a href="javarijstprijs.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="javarijstprijskort.xls">spreadsheet</a> <span class="small">(.xls, 56 kb)</span></p>

<h5><a name="japan">Japan</a></h5>
<p>
<em>Rice prices in 14 regions, 1620-1867</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Japan_rice_P_1620-1867.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Kyoto, Edo and Osaka, 1710-1871</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Japan_1710-1871.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices, wages and exchange rates, 1885-1926</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Japan_1885-1926.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Osaka prices, 1600-1650</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Osaka_1600-1650.xls">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="korea">Korea</a></h5>
<p>
<em>Labour cost, land prices, land rent, and interest rates in the southern region of Korea (1690-1909)</em><br>
-&nbsp; Authors: S.H Jun, J.B Lewis<br>
-&nbsp;<a href="korea.php">About this datafile</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li>all data in one <a href="korea.xls">spreadsheet</a> <span class="small">(.xls, 510 Kb)</span></li> 
<li>in two different spreadsheets:<br>
<a href="korearice-4.xls">The Price of Paddy and Polished Rice</a> <span class="small">632 Kb)</span><br>
<a href="koreawages-4.xls">Wages</a> <span class="small">397 Kb)</span></li></ul>
-&nbsp;Further reading: <a href="korea2.pdf">On Double-entry Bookkeeping in eighteenth-century Korea</a> <span class="small">(.pdf, 67 pp., 948 Kb)</span><br>

<h5><a name="singapore">Singapore</a></h5>
<p>
<em>Commodity price data Singapore</em><br>
-&nbsp; Author: Maurits van Os<br>
-&nbsp;<a href="singapore/">About this datafile</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li>Exchange rates 
<a href="singapore/exchange.xls">spreadsheet</a> <span class="small">(.xls, 174 Kb)</span></li>
<li>Products from the East traded in Singapore 
<a href="singapore/prijs-east.xls">spreadsheet</a> <span class="small">(.xls, 460 Kb)</span></li>
<li>Products from the East traded in Singapore 
<a href="singapore/prijs-east2.xls">spreadsheet</a> <span class="small">(.xls, 356 Kb)</span></li>
<li>Products from the West traded in Singapore 
<a href="singapore/prijs-west.xls">spreadsheet</a> <span class="small">(.xls, 469 Kb)</span></li></ul>

<h5><a name="srilanka">Sri Lanka</a></h5>
<p>
<em>Commodity prices in Sri Lanka and Southern India, 1677-1790</em><br>
-&nbsp; Author: Christiaan van Bochove<br>
-&nbsp; About this datafile: further reading is provided in Christiaan van Bochove, <a href="voc-srilanka-southernindia.pdf">Prices in Sri Lanka and Southern India during the pre-industrial period</a> <span class="small">(.pdf,  479Kb)</span><br>
-&nbsp; The datafile: <a href="voc-srilanka-southernindia.xls">spreadsheet</a> <span class="small">(.xls,  1.7Mb)</span></p>

<h5><a name="thailand">Thailand</a></h5>
<p>
<em>Prices, wages and rents, 1820-1959</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Thai_prices_and_wages_1820-1959.xls">spreadsheet</a> available at GPIH-website</p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="europe"><em>Europe</em></a></h5>
<p>
<em>General level of wages in Europe</em><br>
-&nbsp;Source: International Labour Office, Year book of Labour Statistics 1935-1955<br>
-&nbsp; The datafile: <a href="ilowageseurope.xls">spreadsheet</a> <span class="small">(.xls, 62 Kb)</span></p>

<p>
<em>Consumer price indices, nominal / real wages and welfare ratios of building craftsmen and labourers, 1260-1913</em><br>
-&nbsp; Author: Robert C. Allen<br>
-&nbsp; Spreadsheets available at website of University of Oxford's Department of Economics<br>
-&nbsp; The datafiles: all files listed below can be downloaded as one <a href="allen.rar">file</a> <span class="small">(.rar, 4 Mb)</span></p>
<ul class="square">
<li>Craftsmen</li>
<li>Labourers</li>
<li>Prices and Wages in Amsterdam & Holland, 1500-1914 Amsterdam</li>
<li>Prices and Wages in Antwerp & Belgium, 1366-1913</li>
<li>Prices and Wages in Augsburg, 1417-1830</li>
<li>Prices and Wages in Gdansk, 1501-1914</li>
<li>Prices and Wages in Krakow, 1369-1914</li>
<li>Prices and Wages in Leipzig, 1547-1914</li>
<li>Prices and Wages in London & Southern England, 1259-1914</li>
<li>Prices and Wages in Lwow, 1519-1914</li>
<li>Prices and Wages in Madrid and New Castile, 1501-1913</li>
<li>Prices and Wages in Munich, 1400-1913</li>
<li>Prices and Wages in Naples, 1474-1806</li>
<li>Prices and Wages in Northern Italy, 1286-1914</li>
<li>Prices and Wages in Paris, 1400-1914</li>
<li>Prices and Wages in Strasbourg, 1313-1875</li>
<li>Prices and Wages in Vienna, 1439-1913</li>
<li>Prices and Wages in Warsaw, 1526-1914</li>
</ul>

<h5><a name="austria">Austria</a></h5>
<p>
<em>Prices of various goods in Austrian towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Vienna, 1439-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; Datafile 1: <a href="http://gpih.ucdavis.edu/files/Vienna_prices_1439-1800.xls">prices</a>, spreadsheet available at GPIH-website<br>
-&nbsp; Datafile 2: <a href="http://gpih.ucdavis.edu/files/Vienna_wages_1444-1779.xls">wages</a>, spreadsheet available at GPIH-website</p>

<p>
<em>Austro-Hungarian prices and wages, 1827-1914</em><br>
-&nbsp; Author: Tomas Cvrcek<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Cvrcek_P_&_w,_A-H_1827-1914.xlsx">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Austro-Hungarian housing rents, 1827-1914 </em><br>
-&nbsp; Author: Tomas Cvrcek<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Aus-Hung_housing_rents_(Cvrcek).xlsx">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="belgium">Belgium</a></h5>
<p>
<em>Prices of the Sint-Donatiaanskapittel in Brugge, 1348-1800</em><br>
-&nbsp; Author: A. E. Verhulst<br>
-&nbsp;<a href="donat.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="donat.xls">spreadsheet</a> <span class="small">(.xls, 140 Kb)</span></p>

<p>
<em>Prices of various goods in Belgian towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Belgium, 1366-1603</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Belgium_1366-1603.xls">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="denmark">Denmark</a></h5>
<p>
<em>Prices of various goods in Danish towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Copenhagen prices, 1712-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Copenhagen_p_1712-1800.xls">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="france">France</a></h5>
<p>
<em>Monthly grain prices at Les Halles, Paris. 1549-1698</em><br>
-&nbsp; This file contains monthly prices of wheat, barley and oats in Tournois pounds per setier (156 litre). The data are used in a paper by Nicholas Poynder, <a href="poynder.pdf">Grain storage in theory and history</a>, <span class="small">(.pdf, 40 Kb)</span>. Paper presented at the Third Conference of the European Historical Economics Society, Lisbon, October 29-30, 1999.<br>
-&nbsp;<a href="poynder-france.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="poynder-france.xls">spreadsheet</a> <span class="small">(.xls, 64 Kb)</span></p>

<p>
<em>Monthly prices in Angoul&ecirc;me, 1819-1880</em><br>
-&nbsp; Author: Fr&eacute;d&eacute;ric Michaud<br>
-&nbsp;<a href="angouleme.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="angouleme.xls">spreadsheet</a> <span class="small">(.xls, 66 Kb)</span></p>

<p>
<em>Prices of various goods in French towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices, wages and rents in Paris, 1450-1789</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Paris_1450-1789.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in various French towns (non Paris), 1450-1789</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/France_1450-1789_non-Paris.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Wheat Prices in France, 1825-1913</em><br>
-&nbsp; Author: Bertrand Roehner<br>
-&nbsp; The datafile: <a href="http://eh.net/database/wheat-prices-in-france-1825-1913/">spreadsheet</a>, available at EH.net-website</p>

<h5><a name="germany">Germany</a></h5>
<p>
<em>Monthly wheat prices in Cologne, 1550-1700</em><br>
This datafile was used in: Nicholas Poynder, <a href="poynder.pdf">Grain storage in theory and history</a>, <span class="small">(pdf-file, 40 Kb)</span>. Paper presented at the Third Conference of the European Historical Economics Society, Lisbon, October 29-30 (1999).<br>
-&nbsp;<a href="poynder-germany.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="poynder-germany.xls">spreadsheet</a> <span class="small">(.xls, 36 Kb)</span></p>

<p>
<em>Prices of various goods in German towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Augsburg prices and wages, 1500-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Augsburg_1500-1800.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Frankfurt prices and wages, 1500-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Frankfurt_1500-1800.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices in Mark of L&uuml;beck (14th to 16th century)</em><br>
-&nbsp; Author: Oliver Volckart<br>
-&nbsp;<a href="mark_of_lubeck.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="mark_of_lubeck.xls">spreadsheet</a> <span class="small">(.xls, 2 Mb)</span></p>

<h5><a name="hungary">Hungary</a></h5>
<p>
<em>Prices and wages in Sopron, 1404-1750</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Sopron_(Hungary)_1404-1750.xls">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="ireland">Ireland</a></h5>
<p>
<em>Prices of various goods in Irish towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a>, available at GPIH-website</p>

<h5><a name="italy">Italy</a></h5>
<p>
<em>Wheat prices in Tuscany, 1260-1860 (annual averages)</em><br>
-&nbsp; Author: Paolo Malanima<br>
-&nbsp;<a href="malanima.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="malanima.xls">spreadsheet</a> <span class="small">(.xls, 52 Kb)</span></p>

<p>
<em>Grain prices and prices of olive oil in Pisa, 1548-1818 (monthly averages)</em><br>
-&nbsp; Author: Paolo Malanima<br>
-&nbsp;<a href="malanima.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="grainprices.xls">spreadsheet</a> <span class="small">(.xls, 1.60 Mb)</span></p>

<p>
<em>Monthly wheat prices in Siena, 1546-1765</em><br>
-&nbsp; This datafile was used in: Nicholas Poynder, <a href="poynder.pdf">Grain storage in theory and history</a>, <span class="small">(pdf-file, 40 Kb)</span>. Paper presented at the Third Conference of the European Historical Economics Society, Lisbon, October 29-30 (1999).<br>
-&nbsp;<a href="poynder-italy.php">About this file</a><br>
-&nbsp; The datafile: <a href="poynder-italy.xls">spreadsheet</a> <span class="small">(.xls, 40 Kb)</span></p>

<p>
<em>Prices of various goods in Italian towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Florence, 1286-1381</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_Florence_14thc.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Florence, 1520-1621</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy%20_Florence_1520-1621.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Florence during the Renaissance</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_Florence_Renaissance.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Milan, 1601-1710</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_Milan_1601-1710.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices, wages and rents in Milan, 1701-1860</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_Milan_1701-1860.xls">spreadsheet</a>, available at GPIH-website </p>

<p>
<em>Prices and wages in northern Italian towns, 1285-1850</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_north_1285-1850.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Prices and wages in Modena, 1458-1704</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italy_Modena_to_1705.xls">spreadsheet</a>, available at GPIH-website</p>

<p>
<em>Silver content of the lira in four Italian towns, 1252-1860</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Italian_silver.xls">spreadsheet</a>, available at GPIH-website</p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="netherlands">The Netherlands</a></h5>
<p>
<em>Freight rates between Amsterdam and various port cities 1500-1800, and factors costs of shipping industry 1450-1800</em><br>
-&nbsp; Authors: Milja van Tielhof and Jan Luiten van Zanden<br>
-&nbsp; <a href="freight-rates.pdf">About this datafile</a> <span class="small">(.pdf, 732 Kb)</span><br>
-&nbsp; The datafile: <a href="freight-rates.xls">spreadsheet</a> <span class="small">(.xls, 125 Kb)</span> </p>

<p>
<em>Wages and prices from the convent Leeuwenhorst, 1410-1570</em><br>
-&nbsp; Author: Dr Geertruida de Moor<br>
-&nbsp; <a href="leeuwenhorst/leeuwenhorst.php">About this datafile</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li>Wages in agriculture:
<a href="leeuwenhorst/wagesagriculture.xls">spreadsheet</a> <span class="small">(.xls, 57.5 Kb)</span></li>
<li>Wages in textile:
<a href="leeuwenhorst/wagestextile.xls">spreadsheet</a> <span class="small">(.xls, 71.5 Kb)</span></li>
<li>Wages for digging peat:
<a href="leeuwenhorst/wagespeat.xls">spreadsheet</a> <span class="small">(.xls, 35 Kb)</span></li>
<li>Wages artisans:
<a href="leeuwenhorst/wagesartisans.xls">spreadsheet</a> <span class="small">(.xls, 47.5 Kb)</span></li>
<li>Prices grain and grain products:
<a href="leeuwenhorst/grainproducts.xls">spreadsheet</a> <span class="small">(.xls, 33 Kb)</span></li>
<li>Prices other agricultural produce:
<a href="leeuwenhorst/agriproduce.xls">spreadsheet</a> <span class="small">(.xls, 91 Kb)</span></li>
<li>Prices fruit:
<a href="leeuwenhorst/fruit.xls">spreadsheet</a> <span class="small">(.xls, 31 Kb)</span></li>
<li>Prices animals:
<a href="leeuwenhorst/animals.xls">spreadsheet</a> <span class="small">(.xls, 168 Kb)</span></li>
<li>Prices herbs:
<a href="leeuwenhorst/herbs.xls">spreadsheet</a> <span class="small">(.xls, 48 Kb)</span></li>
<li>Prices beverages:
<a href="leeuwenhorst/beverages.xls">spreadsheet</a> <span class="small">(.xls, 42 Kb)</span></li>
<li>Prices raw textile:
<a href="leeuwenhorst/rawtextile.xls">spreadsheet</a> <span class="small">(.xls, 30.5 Kb)</span></li>
<li>Prices textile (semi-manufactured):
<a href="leeuwenhorst/semitextile.xls">spreadsheet</a> <span class="small">(.xls, 35 Kb)</span></li>
<li>Prices gloves:
<a href="leeuwenhorst/gloves.xls">spreadsheet</a> <span class="small">(.xls, 30 Kb)</span></li>
<li>Prices building materials:
<a href="leeuwenhorst/buildingmaterials.xls">spreadsheet</a> <span class="small">(.xls, 38.5 Kb)</span></li>
<li>Prices metal:
<a href="leeuwenhorst/metalobjects.xls">spreadsheet</a> <span class="small">(.xls, 74.5 Kb)</span></li>
<li>Prices wood:
<a href="leeuwenhorst/wood.xls">spreadsheet</a> <span class="small">(.xls, 231 Kb)</span></li>
<li>Prices peat:
<a href="leeuwenhorst/peat.xls">spreadsheet</a> <span class="small">(.xls, 29.5 Kb)</span></li></ul>

<p>
<em>The prices of the most important consumer goods, and indices of wages and the cost of living in the western part of the Netherlands, 1450-1800</em><br>
-&nbsp; Author: Jan Luiten van Zanden; data supplied by Jan de Vries, Jan Pieter Smits and Arthur van Riel<br>
-&nbsp;<a href="brenv.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="brenv.xls">spreadsheet</a> <span class="small">(.xls, 125 Kb)</span></p>
 
<p>
<em>Prices of consumer and producer goods, 1800-1913</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp;<a href="brannex.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="prijzen19earthur.xls">spreadsheet</a> <span class="small">(.xls, 104 Kb)</span></p>

<p>
<em>Indices of the cost of living, 1800-1913</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp;<a href="brannex.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="col.xls">spreadsheet</a> <span class="small">(.xls, 136 Kb)</span></p>

<p>
<em>Weekly prices in Amsterdam in the 18th century (grains, colonial goods, bills, agio)</em><br>
-&nbsp; Author:  Miko&#322;aj Malinowski<br>
-&nbsp;<a href="weekly-prices-amsterdam-18thcentury.pdf">About this datafile</a> <span class="small">(.pdf, 402 Kb)</span><br>
-&nbsp; The datafile: <a href="weekly-prices-amsterdam-18thcentury.xls">spreadsheet</a> <span class="small">(.xls, 2 Mb)</span></p>

<div class="top"><a href="#top">top</a></div>

<p>
<em>Indices of the prices of private consumer expenditure, 1815-1913</em><br>
-&nbsp; Authors: Jan Pieter Smits and Edwin Horlings<br>
-&nbsp; About this datafile: see Horlings and Smits, &quot;Private consumer expenditure in the Netherlands, 1800-1913&quot;, in: Economic and Social History in the Netherlands, 7 (1996) 15-40<br>
-&nbsp; The datafile: <a href="prijzen19ejanp.xls">spreadsheet</a> <span class="small">(.xls, 62 Kb)</span><br>
<em>These price series are part of the results of the project &quot;reconstruction of the national accounts of the Netherlands 1800-1913&quot; organized by Jan Luiten van Zanden. For full details about this project see: <a href="http://nationalaccounts.niwi.knaw.nl">nationalaccounts.niwi.knaw.nl</a></em></p>

<p>
<em>Agricultural prices in Groningen, 1546-1990</em><br>
-&nbsp; Author: W. Tijms<br>
-&nbsp;<a href="groningen.xls">A list of the data</a><br>
-&nbsp; About the data: see W. Tijms, &quot;Groninger graanprijzen&quot;, in: Historia Agriculturae 31 (2000)<br>
-&nbsp; These data can be downloaded from <a href="http://www.rug.nl/let/onderzoek/onderzoekcentra/nahi/download">www.rug.nl/let/onderzoek/onderzoekcentra/nahi/download</a></p>

<p>
<em>Monthly prices of agricultural goods on Zeeland and Brabant markets, 1816-1855</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp;<a href="vanriel.php">About this datafile</a><br>
-&nbsp; The datafiles:<br>
Monthly prices of agricultural goods on Brabant markets, <a href="brabant-market-prices.xls">spreadsheet</a> <span class="small">(.xls, 243 Kb)</span><br>
Monthly prices of agricultural goods on Zeeland markets, <a href="zeeland-market-prices.xls">spreadsheet</a> <span class="small">(.xls, 226 Kb)</span></p>

<p>
<em>Monthly rye prices in Brabant 1824-1849</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp; The datafile: <a href="monthly-rye-brabant.xls">spreadsheet</a> <span class="small">(.xls, 140 Kb)</span></p>

<p>
<em>Monthly rye prices in Zeeland 1822-1855</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp; The datafile: <a href="monthly-rye-zeeland.xls">spreadsheet</a> <span class="small">(.xls, 144 Kb)</span></p>

<p>
<em>Monthly grain prices in Groningen 1641-1913</em><br>
-&nbsp; Author: Arthur van Riel<br>
-&nbsp; About the data: This file contains monthly prices of grain (1641-1784), of Wheat (1823-1913), of Rye (1785-1913), and of Buckwheat (1786-1829) for Groningen obtained from, among others, the Resolutieboek Burgemeesteren en Raad; broodzettingreg<br>
-&nbsp; The datafile: <a href="monthly-grain-groningen.xls">spreadsheet</a> <span class="small">(.xls, 212 Kb)</span></p>

<p>
<em>Beer and excise</em><br>
-&nbsp; Author: Richard Unger<br>
-&nbsp;<a href="beer.php">About this datafile</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li>Amsterdam 1570-1606 -
<a href="beer/amsterdam1570-1606.xls">spreadsheet</a> <span class="small">(.xls, 17 Kb)</span></li>
<li>Amsterdam 1680-1799 -
<a href="beer/amsterdam1680-1799.xls">spreadsheet</a> <span class="small">(.xls, 24 Kb)</span></li>
<li>Arnhem 1353-1427 -
<a href="beer/arnhem1353-1427.xls">spreadsheet</a> <span class="small">(.xls, 22.5 Kb)</span></li>
<li>Delft 1646-1806 -
<a href="beer/delft1646-1806.xls">spreadsheet</a> <span class="small">(.xls, 26.5 Kb)</span></li>
<li>Dordrecht 1600-1626 -
<a href="beer/dordrecht1600-1626.xls">spreadsheet</a> <span class="small">(.xls, 18.5 Kb)</span></li>
<li>Dordrecht 1770-1833 -
<a href="beer/dordrecht1770-1833.xls">spreadsheet</a> <span class="small">(.xls, 18.5 Kb)</span></li>
<li>Dordrecht 1820-1848 -
<a href="beer/dordrecht1820-1848.xls">spreadsheet</a> <span class="small">(.xls, 38 Kb)</span></li>
<li>Gouda 1360-1585 -
<a href="beer/gouda1360-1585.xls">spreadsheet</a> <span class="small">(.xls, 24 Kb)</span></li>
<li>Gouda 1360-1585 (2) -
<a href="beer/gouda1360-1585-2.xls">spreadsheet</a> <span class="small">(.xls, 24 Kb)</span></li>
<li>Gouda 1437-1533 -
<a href="beer/gouda1437-1553.xls">spreadsheet</a> <span class="small">(.xls, 31.5 Kb)</span></li>
<li>Gouda 1575-1749 -
<a href="beer/gouda1575-1749.xls">spreadsheet</a> <span class="small">(.xls, 24.5 Kb)</span></li>
<li>Haarlem 1590-1610 -
<a href="beer/haarlemprod1590-1610.xls">spreadsheet</a> <span class="small">(.xls, 73 Kb)</span></li>
<li>Hoorn 1692-1794 -
<a href="beer/hoorn1692-1794.xls">spreadsheet</a> <span class="small">(.xls, 20.5 Kb)</span></li>
<li>Leiden 1601-1794 -
<a href="beer/leiden1601-1794.xls">spreadsheet</a> <span class="small">(.xls, 22.5 Kb)</span></li>
<li>Leiden 1656-1748 -
<a href="beer/leiden1656-1748.xls">spreadsheet</a> <span class="small">(.xls, 61.5 Kb)</span></li>
<li>Middelburg 1367-1574 -
<a href="beer/middelburg1367-1574.xls">spreadsheet</a> <span class="small">(.xls, 36 Kb)</span></li>
<li>Beer Posthumus -
<a href="beer/beerposth.xls">spreadsheet</a> <span class="small">(.xls, 16.5 Kb)</span></li>
<li>Holland gijlimpost 1650-1675 -
<a href="beer/hollandgijlimpost1650-1675.xls">spreadsheet</a> <span class="small">(.xls, 17 Kb)</span></li>
<li>Gemeenelandsmiddelen 1650-1805 -
<a href="beer/gemeenelands1650-1805.xls">spreadsheet</a> <span class="small">(.xls, 29 Kb)</span></li>
<li>Gemeenelandsmiddelen 1650-1805 (2) -
<a href="beer/gemeenelands1650-1805 2.xls">spreadsheet</a> <span class="small">(.xls, 34.5 Kb)</span></li>
<li>Gemeenelandsmiddelen 1693-1805 -
<a href="beer/gemeenelands1693-1805.xls">spreadsheet</a> <span class="small">(.xls, 26 Kb)</span></li>
<li>Gemeenelandsmiddelen 1750-1889 -
<a href="beer/gemeenelands1750-1889.xls">spreadsheet</a> <span class="small">(.xls, 18 Kb)</span></li>
</ul>

<p>
<em>The price of bread</em><br>
-&nbsp; Author: Jan de Vries<br>
-&nbsp; Source: Jan de Vries (2019), The Price of Bread: Regulating the Market in the Dutch Republic, Cambridge University Press.<br>
-&nbsp; <a href="grain-price-integration-1594-1855.pdf">Dutch Bread and Grain Prices, 1594-1855: Measuring Grain Market Integration</a> <span class="small">(.pdf, 234 Kb)</span><br>
-&nbsp; The datafiles:
</p>
<p>Netherlands bread prices, 1594-1855 - <a href="netherlands-bread-prices-1594-1855.xlsx">spreadsheet</a> <span class="small">(.xlsx, 264 Kb)</span></p>
<ol>
<li>Average annual rye bread prices in local units</li>
<li>Average annual unbolted wheat bread prices in local units</li>
<li>Average annual rye bread prices in stuivers per kilogram</li>
<li>Average annual fine wheat bread prices in stuivers per kilogram</li>
<li>Average annual unbolted wheat bread prices in stuivers per kilogram</li>
<li>Regional and national average annual bread prices, 1594-1913</li>
</ol>
<p>Netherlands rye and wheat prices, 1594-1855 - <a href="netherlands-rye-wheat-prices-1594-1855.xlsx">spreadsheet</a> <span class="small">(.xlsx, 137 Kb)</span></p>
<ol>
<li>Average annual rye prices</li>
<li>Average annual wheat prices</li>
<li>Regional and national average annual rye and wheat prices, 1594-1913</li>
</ol>
<div class="top"><a href="#top">top</a></div>

<h5><a name="ottoman">Ottoman Empire</a></h5>
<p><em>Prices and wages in Istanbul, 1469-1914</em><br>
-&nbsp; Author: Sevket Pamuk<br>
-&nbsp; The datafile: <a href="istanbul.xls">spreadsheet</a> <span class="small">(.xls, 136 Kb)</span></p>

<p>
<em>Prices and wages in Istanbul, 1469-1914</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Istanbul_1469-1914.xls">spreadsheet</a> available at GPIH-website </p>

<h5><a name="poland">Poland</a></h5>
<p>
<em>Monthly Prices of Grains in Gda&#324;sk in the 18th Century</em><br>
-&nbsp; Author: Miko&#322;aj Malinowski<br>
-&nbsp; <a href="gdansk-malinowski.pdf">About this datafile</a> <span class="small">(.pdf, 126 Kb)</span><br>
-&nbsp; The datafile: <a href="gdansk-malinowski.xls">spreadsheet</a> <span class="small">(.xls, 261 Kb)</span></p>

<p>
<em>Prices and wages in Krakow, 1769-1914</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Krakow_1796-1914.xls">spreadsheet</a> available at GPIH-website </p>

<p>
<em>Prices in Wroclaw, 1507-1618</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Wroclaw_1507-1618.xls">spreadsheet</a> available at GPIH-website </p>

<h5><a name="portugal">Portugal</a></h5>
<p>
<em>Prices, wages and exchange rates in Portugal, 1750-1855</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Portugal_1750-1855.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="russia">Russia</a></h5>
<p>
<em>Prices and wages in Russia, 1590s-1871</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; THe datafile: <a href="http://gpih.ucdavis.edu/files/Russia_p_w_1590s-1871.xls">spreadsheet</a> available at GPIH-website </p>

<p>
<em>Wages in Russia, 1613-1871</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; Datafile 1: <a href="http://gpih.ucdavis.edu/files/Wages_other_Russia_1613-1871.xls">spreadsheet</a> available at GPIH-website<br>
-&nbsp; Datafile 2: <a href="http://gpih.ucdavis.edu/files/Russia_w_salaries_1613-1725.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices of different goods in Russia, c.1500-c.1871</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; Datafile 1: eggs - <a href="http://gpih.ucdavis.edu/files/Russia_egg_prices_c1500-c1870.xls">spreadsheet</a> available at GPIH-website<br>
-&nbsp; Datafile 2: firewood - <a href="http://gpih.ucdavis.edu/files/Russia_firewood_p_1606-1871.xls">spreadsheet</a> available at GPIH-website<br>
-&nbsp; Datafile 3: paper - <a href="http://gpih.ucdavis.edu/files/Russia_paper_prices_1590s-1790s.xls">spreadsheet</a> available at GPIH-website<br>
-&nbsp; Datafile 4: wheat - <a href="http://gpih.ucdavis.edu/files/Russia_wheat_c1500-c1870.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Moscow prices and wages, 1613-1871</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Wages_Moscow_1613-1871.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Silver and gold content of the Russian ruble, 1535-1913</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Russia_Ag_content_ruble_1535-1913.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="scotland">Scotland</a></h5>
<p>
<em>Scottish Economic History Database, 1550 - 1780</em><br>
-&nbsp; Authors: A.J.S. Gibson and T.C. Smout<br>
-&nbsp; <a href="scotland/">About this database and datafiles</a></p>

<p>
<em>Prices of various goods in Scottish towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Edinburgh, 1495-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Edinburgh_1495-1800.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="spain">Spain</a></h5>
<p>
<em>Spanish consumer prices indices 1815-1936</em><br>
-&nbsp; Author: Esmeralda Ballesteros (1861-1935) and Rafael Barqu&iacute;n Gil (1815-1860)<br>
-&nbsp;<a href="barquin1.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="barquin1.xls">spreadsheet</a> <span class="small">(.xls, 23 Kb)</span></p>

<p>
<em>Monthly Spanish wheat prices 1814-1883</em><br>
-&nbsp; Author: Rafael Barqu&iacute;n Gil<br>
-&nbsp;<a href="barquin2.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="barquin2.xls">spreadsheet</a> <span class="small">(.xls, 287 Kb)</span></p>

<p>
<em>Civil / Agricultural year Spanish wheat prices 1814-1883</em><br>
-&nbsp; Author: Rafael Barqu&iacute;n Gil<br>
-&nbsp;<a href="barquin3.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="barquin3.xls">spreadsheet</a> <span class="small">(.xls, 75 Kb)</span></p>

<p>
<em>Exchange rate 1821-1883</em><br>
-&nbsp; Author: Rafael Barqu&iacute;n Gil<br>
-&nbsp;<a href="barquin4.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="barquin4.xls">spreadsheet</a> <span class="small">(.xls, 24 Kb)</span></p>

<p>
<em>Prices of various goods in Spanish towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Catalu&ntilde;a, 1674-1769</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Cataluna_1494-1808.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Spain, 1351-1800</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Spain_1351-1800.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Valladolid, 1499-1600</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Valladolid_1499-1600.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="sweden">Sweden</a></h5>
<p>
<em>Prices of various goods in Swedish towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website </p>

<p>
<em>Swedish prices and wages, 1732-1874</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Sweden_1732-1874.xls">spreadsheet</a> available at GPIH-website </p>

<p>
<em>Prices in &Ouml;sterg&ouml;tland, 1592-1735</em><br>
-&nbsp; Author: G&ouml;ran Hansson<br>
-&nbsp;<a href="ostergotland.php">About this datafile</a><br>
-&nbsp;<a href="ostergotland.xls">The datafile</a> - <span class="small">(.xls, 226 Kb)</span></p>

<p>
<em>Prices in Stockholm 1539-1620</em><br>
-&nbsp; Author: Johan S&ouml;derberg<br>
-&nbsp; The datafile: <a href="stockholm.xls">spreadsheet</a> <span class="small">(.xls, 118 Kb)</span></p>

<h5><a name="switzerland">Switzerland</a></h5>
<p>
<em>Prices of various goods in Swiss towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="united">United Kingdom</a></h5>

<p><em>Rents York Bridgemasters' Accounts</em><br>
-&nbsp; Author: Annelies Tukker<br>
-&nbsp; About this file: This datafile was used in: Annelies Tukker, <a href="thesis-annelies-tukker.pdf">Mankind: "I Must Nedys Labure, Yt Ys My Lyvynge". Relative Wages in Fifteenth Century York</a> <span class="small">(pdf-file, 1.2 Mb)</span>. </a><br>
-&nbsp; The datafile: <a href="rents-york.xlsx">Rents York Bridgemasters' Accounts</a> <span class="small">(.xlsx,  560Kb)</span></p>

<p>
<em>Monthly grain prices in England, 1270-1955</em><br>
-&nbsp; These datafiles were used in: Nicholas Poynder, <a href="poynder.pdf">Grain storage in theory and history</a> <span class="small">(pdf-file, 40 Kb)</span>. Paper presented at the Third Conference of the European Historical Economics Society, Lisbon, October 29-30 (1999).<br>
-&nbsp; <a href="poynder-england.php">About this file</a><br>
-&nbsp; The datafiles:</p>
<ul class="square">
<li><a href="winchester.xls">Wheat and malt prices in Winchester (1657-1817)</a> <span class="small">(.xls,  36Kb)</span></li>
<li><a href="wheatoxford.xls">Wheat prices in Oxford (1618-1645)</a> <span class="small">(.xls, (20 Kb)</span></li>
<li><a href="cambridge.xls">Wheat and barley prices in Cambridge (1594-1681)</a> <span class="small">(.xls, 37 Kb)</span></li>
<li><a href="varioustowns.xls">Wheat, barley and oats prices in various towns (1270-1620)</a> <span class="small">(.xls, 128 Kb)</span></li>
<li><a href="englandgrain1.xls">Barley and oats prices in England (1841-1929)</a> <span class="small">(.xls, 54 Kb)</span></li>
<li><a href="englandgrain2.xls">Wheat, barley and oats prices in England (1929-1955)</a> <span class="small">(.xls, 68 Kb)</span></li>
</ul >

<p>
<em>Wages and the cost of living in Southern England (London) 1450-1700</em><br>
-&nbsp; Author: Jan Luiten van Zanden<br>
-&nbsp;<a href="dover.php">About this datafile</a><br>
-&nbsp; The datafile: <a href="dover.xls">spreadsheet</a> <span class="small">(.xls, 120 Kb)</span></p>

<p>
<em>Prices of various goods in UK towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>English prices and wages, 1209-1914</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/England_1209-1914_(Clark).xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>English vs metric measures</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/English_vs_metric.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Weight vs. volume: How many kilograms per liter?</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Weight_vs_volume.xls">spreadsheet</a> available at GPIH-website</p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="northamerica"><em>North America</em></a></h5>

<h5><a name="canada">Canada</a></h5>
<p>
<em>Prices of various goods in Canadian towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website </p>

<h5><a name="unitedstates">United States</a></h5>
<p>
<em>Prices of various goods in US towns during the 1870s</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Ward-Devereux_P_1872-78.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Chesapeak, 1733-1827</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Chesapeake_1733-1827.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Massachusetts, 1630-1883</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Massachusetts_1630-1883.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Maryland, 1752-1856</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Maryland_1752-1856.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>San Francisco wholesale prices, 1847-1900</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/San_Francisco_wholesale_prices_1847-1900_and_California_wages_1870-1928.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>California wages, 1870-1928</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/San_Francisco_wholesale_prices_1847-1900_and_California_wages_1870-1928.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Vermont, 1780-1943</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Vermont_1780-1943.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in West Virginia, 1788-1860</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/West_Virginia_1788-1860.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Silver in North America 1649-1977</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Silver_North_America_1649-1977.xls">spreadsheet</a> available at GPIH-website</p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="southamerica"><em>South America</em></a></h5>

<p>
<em>Latin American colonial metrology</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Latin_Am_colonial_metrol.doc">text document</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Argentina, Bolivia, Chile, Colombia, Mexico and Peru</em><br>
-&nbsp; Authors: Leticia Arroya Abad, Elwyn A. R. Davies, and Jan Luiten van Zanden<br>
-&nbsp; <a href="prices-wages-argentina-bolivia.pdf">About this datafile</a> <span class="small">(.pdf, 177 Kb)</span><br>
-&nbsp; The datafile: <a href="prices-wages-argentina-bolivia.xls">spreadsheet</a> <span class="small">(.xls, 2.8 Mb)</span></p>

<h5><a name="brazil">Brazil</a></h5>
<p>
<em>Prices of different goods in Salvador de Bahia</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Brazil_1674-1769.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Silver content of the Brazilian real, 1673-1769</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Brazil_monetary_hist.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="chile">Chile</a></h5>
<p>
<em>Prices in Chile, 1631-1830</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Chile_1631-1830.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="colombia">Colombia</a></h5>
<p>
<em>Bogota prices and wages, 1635-1809</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Colombia_1635-1809.xls">spreadsheet</a> available at GPIH-website</p>

<h5><a name="peru">Peru</a></h5>
<p>
<em>Prices of various goods in Peru, 1627-1822</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Peru_1627-1822.xls">spreadsheet</a> available at GPIH-website</p>

<div class="top"><a href="#top">top</a></div>

<h5><a name="oceania"><em>Oceania</em></a></h5>

<h5><a name="australia">Australia</a></h5>
<p>
<em>Prices and wages in New South Wales, 1818-1983</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/NS_Wales_food_p_w_1818-1983.xls">spreadsheet</a> available at GPIH-website</p>

<p>
<em>Prices and wages in Van Diemen&rsquo;s Land, 1806-1850</em><br>
-&nbsp; Author: Global Price and Income History Group<br>
-&nbsp; The datafile: <a href="http://gpih.ucdavis.edu/files/Van_Diemen_Land_1806-50.xls">spreadsheet</a> available at GPIH-website</p>
<br>

		<div class="top"><a href="#top">top</a></div>
	</div>
</div>

<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</body>
</html>
