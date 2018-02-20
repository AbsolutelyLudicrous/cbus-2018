<h3>Index:</h3>
<p>
	<?php
		$leadingdirs=getenv($WEBSERVERROOT);	# root of the webserver, from where data is served, set in apache
		$rawdir=getcwd();	# raw, unstripped, directory location absolute to the file system
		$dir=substr($rawdir, (strpos($rawdir,$leadingdirs)+strlen($leadingdirs)));	# stips the raw directory of the server root location
		foreach (scandir('.') as $file){
			echo("<a href=\"http://cutie-computie.org$dir/$file\">$file</a><br>");
		}
	?>
</p>
