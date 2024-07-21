# SOFTWARES

>KAPE
>Autopsy
>FTK Imager

>AccessData Registry Viewer
>Zimmermans Registry Explorer
>RegRipper

# Information places #

# OS version
> SOFTWARE\Microsoft\Windows NT\CurrentVersion

# Control Set
>SYSTEM\ControlSet001
>SYSTEM\ControlSet002
>SYSTEM\Select\Current
>SYSTEM\Select\LastKnownGood

# Computer Name & TimeZone
>SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName
>SYSTEM\CurrentControlSet\Control\TimeZoneInformation

# Networks
>SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces

# Past Networks
>SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged
>SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Managed

# Autostart Programs
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Run
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\RunOnce
>SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
>SOFTWARE\Microsoft\Windows\CurrentVersion\policies\Explorer\Run
>SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# Service
>SYSTEM\CurrentControlSet\Services

# SAM / HIVE
>	

# RECENT FILES
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.pdf

# RECENT FILES (OFFICE)
>NTUSER.DAT\Software\Microsoft\Office\VERSION
>NTUSER.DAT\Software\Microsoft\Office\15.0\Word
>NTUSER.DAT\Software\Microsoft\Office\VERSION\UserMRU\LiveID_####\FileMRU

# SHELL BAGS
>USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\Bags
>USRCLASS.DAT\Local Settings\Software\Microsoft\Windows\Shell\BagMRU
>NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU
>NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags

# MRU DIALOGS
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePIDlMRU
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedPidlMRU

# SEARCH ADDRESS / SEARCH BARS
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths
>NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\WordWheelQuery

# USER ASSIST
>NTUSER.DAT\Software\Microsoft\Windows\Currentversion\Explorer\UserAssist\{GUID}\Count

# SHIM CACHE
>SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache
<!-- AppCompatCacheParser.exe --csv <path to save output> -f <path to SYSTEM hive for data parsing> -c <control set to parse> -->


# AMCACHE
>C:\Windows\appcompat\Programs\Amcache.hve
>Amcache.hve\Root\File\{Volume GUID}\

# BAM / DAM
>SYSTEM\CurrentControlSet\Services\bam\UserSettings\{SID}
>SYSTEM\CurrentControlSet\Services\dam\UserSettings\{SID}

# DEVICE ID
>SYSTEM\CurrentControlSet\Enum\USBSTOR
>SYSTEM\CurrentControlSet\Enum\USB

# First/Last Times
>SYSTEM\CurrentControlSet\Enum\USBSTOR\Ven_Prod_Version\USBSerial#\sProperties\{83da6326-97a6-4088-9453-a19231573b29}\####

# USB Device Volume Name
> SOFTWARE\Microsoft\Windows Portable Devices\Devices