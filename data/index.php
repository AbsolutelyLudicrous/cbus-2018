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
				// echo '<pre>';
				// echo '<print_r(scandir('.'));
				// echo '<echo '</pre>';
				foreach (scandir('.') as $file){
					echo("<a href=\"http://cutie-computie.org/\">file</a>");
					//echo('<a href="http://cutie-computie.org/','>foo</a>');//,getcwd(),'/',$file,'">',$file,'</a>','<br>');
				}
			?>
		</p>
	</body>
</html>
