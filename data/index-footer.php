<h3>Index:</h3>
<p>
	<?php
		$host="cutie-computie.org";	#hostname of system, can be a hostname or an IP address
		$leadingdirs="/usr/local/www/data";	# directories leading up to the web server's hosted data
		$rawdir=getcwd();	# raw, unstripped, directory location absolute to the file system
		$dir=substr($rawdir, (strpos($rawdir,$leadingdirs)+strlen($leadingdirs)));	# stips the raw directory of the server root location
		foreach (scandir('.') as $file){
			echo("<a href=\"http://$host$dir/$file\">$file</a><br>");
		}
	?>
</p>
