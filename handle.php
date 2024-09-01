<?php
$dat = $_POST["message"];
$lines = preg_split("/\n/", $dat);
foreach ($lines as &$line) {
    if (strlen($line) > 40)
    {
      echo(fail);
	}
}
echo $dat;
$fl = fopen("indat.txt", "w");
fwrite($fl, $dat);
fclose($fl);
$output = shell_exec('python3 generate.py');
echo "<pre>$output</pre>";
sleep(2);
header("Location: /out.png");
?>
