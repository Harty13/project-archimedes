<?php 
require "_settings.inc.php";

if( $REQUEST_METHOD == "POST" ) {
	if( $password == 'Moskva98' ) {
		require("./_mysql.inc.php");
		$sql = new mysql_class;
		$sql->Create($setting_server, $setting_user, $setting_password, $setting_db, "", "695874");

		$db_year = $sql->QueryItem("SELECT year FROM cpi_nederland WHERE year = " . $year);

		if( empty($db_year) ) {
			$sql->Insert("INSERT INTO cpi_nederland(year, cpi) VALUES(" . $year.", '" . $cpi."')");
			echo "Nieuwe data is bewaard.";
		} else {
			echo "Jaar is al ingevoerd...";
		}
	} else {
		echo "Wachtwoord niet geldig";
	}
}
?>
<form action="" method="post">
Wachtwoord: <input type="password" name="password"><BR><BR>
Jaar: <input type="text" name="year"><BR>
CPI: <input type="text" name="cpi"><BR><BR>
<input type="submit" name="submit" value="Zend">
</form>
