<?php 
// MENU ITEM

$url = $_SERVER["QUERY_STRING"];
if ( $url <> "" ) {
	$url = "?" . $url;
}
$url = urlencode(( $_SERVER["HTTP_X_FORWARDED_HOST"] != '' ? $_SERVER["HTTP_X_FORWARDED_HOST"] : $_SERVER["SERVER_NAME"] ) . '/hpw' . $_SERVER["SCRIPT_NAME"] . $url);

if ( !isset($label) ) {
	$label = "Print Version";
}
if ( !isset($language) ) {
	$language = "en";
}
?>
<dl id="print">
	<dd>
<script type="text/javascript" language="javascript">
<!--
function popupWindow(url, sName, sInstellingen)
{
	newwindow = window.open(url,sName,sInstellingen);
	if (window.focus) {
		newwindow.focus();
	}
	return false;
}
// -->
</script>
<?php 
$printurl = "/scripts/print.php?language=" . $language . "&url=" . $url;
$printurl = str_replace("&", "&amp;", $printurl);
?>
<a href="#" onclick="popupWindow('<?php echo $printurl; ?>','printwindow','width=800,height=600,directories=no,location=no,menubar=no,resizable=yes,scrollbars=yes,status=no,toolbar=no');return false;" ><?php echo $label ?></a></dd>
</dl>
