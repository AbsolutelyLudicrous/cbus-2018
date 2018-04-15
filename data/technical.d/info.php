<?php 
	if(file_exists('/usr/local/www/lockfiles/WEBSERVER_DEBUGGING')){
		phpinfo();}
	else{
		echo('The webserver does not currently have debugging information turned on, email mdanne@protonmail.com if you would like technical information');}
?>
