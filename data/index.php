<!DOCTYPE html>
<html>
	<body>
		<p>
			I dunno, stuff?
			<br><br>
			What should go on a splash page you're not really meant to see?
			<br>
			(This, apparently.)
			<br><br>
			Hey nerds!
			If you want to checkout the backend, the real meat of... <i>this</i>, check out the <a href="https://github.com/AbsolutelyLudicrous/cbus-2018">Github repo</a>.
		</p>

		<h3>Index:</h3>
		<p>
			<?php
				$SERVERROOT="/usr/local/www/data";	# root of the webserver, from where data is served
				$rawdir=getcwd();	# raw, unstripped, directory location absolute to the file system
				$dir=substr($rawdir, (strpos($rawdir,$SERVERROOT)+strlen($SERVERROOT)));	# stips the raw directory of the server root location
				echo $dir,'<br>';
				foreach (scandir('.') as $file){
					echo("<a href=\"http://cutie-computie.org$dir/$file\">$file</a><br>");
				}
			?>
		</p>
	</body>
</html>
