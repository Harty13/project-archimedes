<?php
header("Location: https://iisg.amsterdam/en/research/projects/hpw/calculate.php",TRUE,301);
exit('go to <a href="https://iisg.amsterdam/en/research/projects/hpw/calculate.php">new website</a>');
?>






<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
	<title>Value of the guilder / euro</title>
	<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
	<style type="text/css" media="all">@import url(/styles/sochist.css);</style>
	<META HTTP-EQUIV="EXPIRES" CONTENT="<?php echo date("D, d M Y H:i:s", time()+31*24*60*60) . " GMT"; ?>">
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
		<dl id="language">
			<dd>English | <a href="calculate-nl.php">Nederlands</a></dd>
		</dl>
	</div>
	<div class="navthird">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/search-ghome-sochist.inc.php"; ?>
	</div>
	<div class="content">

<h2>Value of the Guilder / Euro</h2>

<h3>Comparing the purchasing power of the guilder from 1450 to any other year.</h3>

<p>
To determine the value of an amount of money in one year compared to another, enter the values in the appropriate places below.<br>
For example, you may want to know:<br>
How much money would you need today to have the same "purchasing power" of Fl 100 in year <strong>1950</strong>.<br><br>

You can make this computation among all the years between 1450 and the present.</p>

<form action="calculate2.php" method="post">
1. How much money <em>today</em> has the same &quot;purchasing power&quot; as <br>
	<select name="valuta">
	<option value="gulden">fl.</option>
	<option value="euro" SELECTED>&euro;</option>
	</select>
&nbsp;<input type="text" name="money" size="4"> in the year <input type="text" name="year2" size="4">?&nbsp;&nbsp;&nbsp;
<input type="submit" name="submit" value="Calculate">
</form>
<br>
If you are only interested in comparing the value of an amount of money in one past year in the prices of another year, you can use this sentence.<br><br>

<form action="calculate2.php" method="post">
2. How much money in the year <input type="text" name="year1" size="4"> has the same "purchasing power" as 
	<select name="valuta">
	<option value="gulden">fl.</option>
	<option value="euro" SELECTED>&euro;</option>
	</select>
&nbsp; <input type="text" name="money" size="4"> in the year <input type="text" name="year2" size="4">?&nbsp;&nbsp;&nbsp;
<input type="submit" name="submit" value="Calculate">
</form>

<p>Use a <strong>.</strong> between guilders/euros and cents:<br>
e.g. fl 10.50 (not fl 10,50)<br><br>

&gt;&gt; <a href="cpi-netherlands2016.xls">The datafile (2016)</a> <span class="small">Excel spreadsheet, 102 Kb</span><br>
&gt;&gt; <a href="cpi.php">Source note for "Value of the Guilder / Euro ?"</a></p>

<a name="other"></a>
<h3>Purchasing Power of Other Currencies</h3>
<ul>
<li><a href="http://www.measuringworth.com/ppowerus/">Purchasing Power of the Dollar</a>, 1774 - Present.</li>
<li><a href="http://www.measuringworth.com/ppoweruk/">Purchasing Power of the British Pound</a>, 1270 - Present.</li>
</ul>

	</div>
</div>

<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</center>
</body>
</html>
