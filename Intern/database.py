import sqlite3

conn = sqlite3.connect('exploits_metadata.db')

conn.execute('''CREATE TABLE EXPLOITS(
       S_No INT PRIMARY KEY     NOT NULL,
       Name             TEXT    NOT NULL,
       CVE              TEXT    NOT NULL,
       Platform         TEXT    NOT NULL,
       KernelVersion    TEXT    NOT NULL,
       Architecture     TEXT    NOT NULL,
       OperatingSystem  TEXT    NOT NULL,
       OsVersion        TEXT    NOT NULL,
       Comments         TEXT    NOT NULL);''')

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (1, 'OpenSSH 6.8-6.9 local privilege escalation', 'CVE-2015-6565', 'Linux', 'No info yet', \
      'No info yet', No info yet', 'No info yet', 'OpenSSH 6.8-6.9' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (2, 'MySQL/PerconaDB/MariaDB-Privilege Escalation/Race Condition PoC Exploit', \
      'CVE-2016-6663 / OCVE-2016-5616', 'Linux', 'No info yet', 'No info yet', No info yet', 'No info yet',\
       'MySQL / MariaDB / PerconaDB 5.5.x/5.6.x/5.7.x' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (3, 'MySQL/MariaDB/PerconaDB-Root Privilege Escalation PoC Exploit', 'CVE-2016-6664 / OCVE-2016-5617',\
       'Linux', 'No info yet', 'No info yet', No info yet', 'No info yet',\
        'MySQL / MariaDB / PerconaDB 5.5.x/5.6.x/5.7.x' )");

conn.execute("INSERT INTO EXPLOITS\
 (S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (4, 'Linux Kernel 4.4.0(Ubuntu)-DCCP Double-Free Privilege Escalation', 'CVE-2017-6074', 'Linux',\
       '4.4.0', 'No info yet', 'Ubuntu', 'No info yet', 'Linux Kernel 4.4.0 (Ubuntu)' )");

conn.execute("INSERT INTO EXPLOITS\
 (S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (5, 'PonyOS 4.0-fluttershy LD_LIBRARY_PATH Kernel Privilege Escalation', 'Not Available', 'Linux', \
      'No info yet', 'No info yet', 'ponyos', '4.0', 'PonyOS 4.0-fluttershy LD_LIBRARY_PATH' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (6, 'Linux Kernel 4.8.0 udev 232-Privilege Escalation', 'CVE-2017-7874', 'Linux', '4.8.0', 'No info yet',\
       'No info yet', 'No info yet', 'Linux Kernel 4.8.0' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (7, 'Oracle VM VirtualBox 5.1.14 r112924-Unprivileged Host User to Host Kernel Privilege Escalation \
      via ALSA config', 'CVE-2017-3576', 'Linux', 'No info yet', 'No info yet', 'No info yet', 'No info yet', \
      'Oracle VM VirtualBox 5.1.14' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (8, 'Nginx (Debian-Based Distros + Gentoo)-logrotate Privilege Escalation', 'CVE-2016-1247', 'Linux', \
      'No info yet', 'No info yet', 'Nginx', 'No info yet', 'Nginx (Debian-Based Distros + Gentoo)' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (9, 'Nagios 4.2.2-Privilege Escalation', 'CVE-2016-8641', 'Linux', 'No info yet', 'No info yet', \
      'Nagios', '4.2.2', 'Nagios 4.2.2' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (10, 'LogRhythm Network Monitor Auth Bypass Root RCE', 'Not Available','Linux', 'No info yet', \
      'No info yet', 'No info yet', 'No info yet', '3.3.2.1061 (latest) or below' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (11, 'Linux Kernel 2.6.22<3.9-Dirty COW PTRACE_POKEDATA Race Condition Privilege Escalation(/etc/passwd)'\
      , 'CVE-2016-5195', 'Linux', '2.6.22,2.6.23,2.6.24,2.6.25,2.6.26,2.6.27,2.6.28,2.6.29,2.6.30,2.6.31,2.6.32,2.6.33,\
      2.6.34,2.6.35,2.6.36,2.6.37,2.6.38,2.6.39,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8', 'No info yet', 'No info yet', \
      'Linux Kernel 2.6.22<3.9' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (12, 'Linux Kernel 2.6.22<3.9-Dirty COW /proc/self/mem Race Condition Privilege Escalation(/etc/passwd)',\
       'CVE-2016-5195', '2.6.22,2.6.23,2.6.24,2.6.25,2.6.26,2.6.27,2.6.28,2.6.29,2.6.30,2.6.31,2.6.32,2.6.33,\
      2.6.34,2.6.35,2.6.36,2.6.37,2.6.38,2.6.39,3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8', 'No info yet', 'No info yet', \
      'Linux Kernel 2.6.22<3.9' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (13, 'Nagios Core<4.2.4  Root Privilege Escalation PoC Exploit', 'CVE-2016-9566', 'Linux', 'No info yet',\
       'Nagios', '3.0a1,3.0a2,3.0a3,3.0a4,3.0a5,3.0b1,3.0b2,3.0b3,3.0b4,3.0b5,3.0b6,3.0b7,3.0rc1,3.0rc2,3.0rc3,3.0,\
       3.0.1,3.0.2,3.0.3,3.0.4,3.0.5,3.0.6,3.1.0,3.1.1,3.1.2,3.2.0,3.2.1,3.2.2,3.2.3,3.3.1,3.4.0,3.4.1,3.4.2,3.4.3,\
       3.4.4,3.5.0,3.5.1,4.0.0,4.0.1,4.0.2,4.0.3,4.0.4,4.0.5,4.0.6,4.0.7,4.0.8,4.1.0,4.1.1,4.2.0,4.2.1,4.2.2,4.2.3',\
        'Nagios<4.2.4' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (14, 'Vesta Control Panel 0.9.7<=0.9.8-16 Local Privilege Escalation Exploit', 'Not Available', 'Linux',\
       'No info yet', 'No info yet', No info yet', 'No info yet', 'Vesta Control Panel 0.9.7<=0.9.8-16' )");

conn.execute("INSERT INTO EXPLOITS \
(S_No,NAME,CVE,Platform,KernelVersion,Architecture,OperatingSystem,OsVersion,Comments) \
      VALUES (15, 'GNU Screen 4.5.0-Privilege Escalation', 'Not Available', 'Linux', 'No info yet', 'No info yet',\
       'No info yet', 'No info yet', 'GNU Screen 4.5.0' )");

conn.commit()
conn.close()