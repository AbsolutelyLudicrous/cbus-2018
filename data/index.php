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
				print_r(scandir("."));

				// Create recursive dir iterator which skips dot folders
				$dir = new RecursiveDirectoryIterator('.', FilesystemIterator::SKIP_DOTS);
				
				// Flatten the recursive iterator, folders come before their files
				$it  = new RecursiveIteratorIterator($dir, RecursiveIteratorIterator::SELF_FIRST);
				
				// Maximum depth is 1 level deeper than the base folder
				$it->setMaxDepth(1);
				
				// Basic loop displaying different messages based on file or folder
				foreach ($it as $fileinfo) {
					if ($fileinfo->isDir()) {
						printf("dir: - %s\n", $fileinfo->getFilename());
					} elseif ($fileinfo->isFile()) {
						printf("file: %s - %s\n", $it->getSubPath(), $fileinfo->getFilename());
					}
				}
			?>
		</p>
	</body>
</html>
