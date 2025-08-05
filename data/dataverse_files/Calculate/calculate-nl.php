<?php
header("Location: https://iisg.amsterdam/en/research/projects/hpw/calculate.php",TRUE,301);
exit('go to <a href="https://iisg.amsterdam/en/research/projects/hpw/calculate.php">new website</a>');
?>








<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">

<html>
<head>
	<title>De waarde van de gulden / euro</title>
	<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
	<style type="text/css" media="all">@import url(/styles/sochist.css);</style>
	<META HTTP-EQUIV="EXPIRES" CONTENT="<?php echo date("D, d M Y H:i:s", time()+31*24*60*60) . " GMT"; ?>">
</head>

<body>
<center>
<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/top-home-sochist-nl.inc.php"; ?>

<div class="bulk">
	<div class="navsecond">
		<dl id="menu">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/menu-hpw.inc.php"; ?>
		</dl>
		<dl id="email">
			<dd>Email: <?php require_once "_email_hpw.inc.php"; ?></dd>
		</dl>
		<dl id="language">
			<dd><a href="calculate.php">English</a> |  Nederlands</dd>
		</dl>
	</div>
		<div class="navthird">
		<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/search-ghome-sochist-nl.inc.php"; ?>
		</div>
	<div class="content">

<h2>De waarde van de gulden / euro</h2>

<p><strong>Een vergelijking van de koopkracht van de gulden vanaf het jaar 1450 met een ander jaar.</strong></p>

<p>
Om de waarde van een som geld in een bepaald jaar te vergelijken met die in een ander jaar, vult u de bedragen hieronder in in de daarvoor bestemde vakjes.<br>
U wilt bijvoorbeeld weten:<br>
Hoeveel geld heb ik vandaag nodig om dezelfde 'koopkracht' te hebben als in het jaar <strong>1950</strong> met 100 fl.?<br><br>

U kunt deze berekening maken tussen alle jaren vanaf 1450 tot afgelopen jaar.</p>

<form action="calculate2-nl.php" method="post">
1. Welk bedrag heeft <em>vandaag</em> dezelfde 'koopkracht' als <br>
	<select name="valuta">
	<option value="gulden">fl.</option>
	<option value="euro" SELECTED>&euro;</option>

	</select>
&nbsp;<input type="text" name="money" size="4"> in het jaar <input type="text" name="year2" size="4">?&nbsp;&nbsp;&nbsp;
<input type="submit" name="submit" value="Bereken">
</form>
<br>
<p>
Als u alleen ge&iuml;nteresseerd bent in de koopkracht van een bedrag in een bepaald jaar vergeleken met een ander jaar, kunt u dat hier berekenen:</p>

<form action="calculate2-nl.php" method="post">
2. Welk bedrag heeft in het jaar <input type="text" name="year1" size="4"> dezelfde 'koopkracht' als 
	<select name="valuta">

	<option value="gulden">fl.</option>
	<option value="euro" SELECTED>&euro;</option>
	</select>
&nbsp; <input type="text" name="money" size="4"> in het jaar <input type="text" name="year2" size="4">?&nbsp;&nbsp;&nbsp;
<input type="submit" name="submit" value="Bereken">
</form>
<br>
<p>Let op: Gebruik een <strong>.</strong> tussen guldens/euros en centen:<br>

d.w.z. fl. 10.50 (niet fl. 10,50)<br><br>

<a href="cpi-netherlands2016.xls">&gt;&gt; Het databestand (2016)</a> <span class="small">Excel spreadsheet, 102 Kb</span><br>
<a href="cpi.php">&gt;&gt; Bronvermelding voor 'De waarde van de gulden / euro'</a></p>

<a name="andere"></a><h3>Koopkracht van andere valuta</h3>
<ul>
<li><a href="http://www.measuringworth.com/ppowerus/">Koopkracht van de Dollar</a>, 1774 - Heden.</li>

<li><a href="http://www.measuringworth.com/ppoweruk/">Koopkracht van de Britse Pond</a>, 1270 - Heden.</li>
</ul>

	</div>
	
</div>

<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist-nl.inc.php"; ?>
</center>
</body>

</html>
