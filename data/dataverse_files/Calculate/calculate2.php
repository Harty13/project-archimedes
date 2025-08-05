<?php 


header("Location: https://iisg.amsterdam/en/research/projects/hpw/calculate.php",TRUE,301);
exit('go to <a href="https://iisg.amsterdam/en/research/projects/hpw/calculate.php">new website</a>');





require "_class_website_protectie.php";
require "_settings.inc.php";

$websiteProtectie = new _class_website_protectie();

$money = $websiteProtectie->request('post', 'money');
$year1 = $websiteProtectie->request('post', 'year1');
$year2 = $websiteProtectie->request('post', 'year2');
$valuta = $websiteProtectie->request('post', 'valuta');

$money = substr($money, 0, 10);
$year1 = substr($year1, 0, 4);
$year2 = substr($year2, 0, 4);
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
		</div>
	<div class="content">

<h2>Value of the Guilder / Euro</h2>
<p>
<?php 
	require("./_mysql.inc.php");
	$sql = new mysql_class;

	$sql->Create($setting_server, $setting_user, $setting_password, $setting_db, "", "584213");

	$min_max = $sql->QueryRow("SELECT MAX(year), MIN(year) FROM cpi_nederland ");

	if( empty($year1) ) //assume the mean today
		$year1 = (int) $min_max[0];
	else if( $year1 < $min_max[1])
		$year1 = (int) $min_max[1];
	else if( $year1 > $min_max[0])
		$year1 = (int) $min_max[0];

	if( $year2 < $min_max[1])
		$year2 = (int) $min_max[1];
	else if( $year2 > $min_max[0])
		$year2 = (int) $min_max[0];

	$cpi1 = $sql->QueryItem("SELECT cpi FROM cpi_nederland WHERE year = " . $year1);
	$cpi2 = $sql->QueryItem("SELECT cpi FROM cpi_nederland WHERE year = " . $year2);

	// er ontstaat soms een vreemde afrondings probleem bij decimale waardes (bij gelijke opgegeven jaren)
	// daarom op deze manier
	if ( $cpi1 == $cpi2 ) {
		$money2 = $money;
	} else {
		$money2 = ($cpi1 / $cpi2) * $money;
	}

	if( $valuta == 'gulden' ) {
		echo "<strong>fl " . number_format($money, 2, ".", " ") . "</strong> in the year <strong>$year2</strong> <BR><BR>has a \"purchasing power\" of <BR><BR><strong>fl. " . number_format($money2,2, ".", " ") . "</strong> (&euro; " . number_format($money2/2.20371,2, ".", " ") . ") in the year <strong>$year1</strong>";
	} else if( $valuta == 'euro' ) {
		echo "<strong>&euro; " . number_format($money, 2, ".", " ") . "</strong> from the year <strong>$year2</strong> <BR><BR>has a \"purchasing power\" of <BR><BR><strong>&euro; " . number_format($money2,2, ".", " ") . "</strong> (fl. " . number_format($money2*2.20371,2, ".", " ") . ") in the year <strong>$year1</strong>";
	}

	// for 
	echo "\n<!--\n";
	echo "IP1:" . $_SERVER['REMOTE_ADDR'] . "\n";
	echo "IP2:" . $_SERVER['HTTP_X_FORWARDED_FOR'] . "\n";
	echo "<hpw>\n";
	if( $valuta == 'gulden' ) {
		echo "\t<hpw_request_type>fl</hpw_request_type>\n";
		echo "\t<hpw_request_value>" . number_format($money, 2, ".", "") . "</hpw_request_value>\n";
		echo "\t<hpw_request_year>$year2</hpw_request_year>\n";
		echo "\t<hpw_result_year>$year1</hpw_result_year>\n";
		echo "\t<hpw_result1_type>fl</hpw_result1_type>\n";
		echo "\t<hpw_result1_value>" . number_format($money2,2, ".", "") . "</hpw_result1_value>\n";
		echo "\t<hpw_result2_type>euro</hpw_result2_type>\n";
		echo "\t<hpw_result2_value>" . number_format($money2/2.20371,2, ".", "") . "</hpw_result2_value>\n";
	} else if( $valuta == 'euro' ) {
		echo "\t<hpw_request_type>euro</hpw_request_type>\n";
		echo "\t<hpw_request_value>" . number_format($money, 2, ".", "") . "</hpw_request_value>\n";
		echo "\t<hpw_request_year>$year2</hpw_request_year>\n";
		echo "\t<hpw_result_year>$year1</hpw_result_year>\n";
		echo "\t<hpw_result1_type>euro</hpw_result1_type>\n";
		echo "\t<hpw_result1_value>" . number_format($money2,2, ".", "") . "</hpw_result1_value>\n";
		echo "\t<hpw_result2_type>fl</hpw_result2_type>\n";
		echo "\t<hpw_result2_value>" . number_format($money2*2.20371,2, ".", "") . "</hpw_result2_value>\n";
	}
	echo "</hpw>\n";
	echo "-->\n";
?>

</p>

<h3><a href="/hpw/calculate.php">Calculate again?</a></h3>

	</div>
	</div>

<?php require_once $_SERVER["DOCUMENT_ROOT"] . "/scripts/footer-sochist.inc.php"; ?>

</center>
</body>
</html>
