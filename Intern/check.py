import paramiko
import sqlite3

ip = raw_input("Ip: ")
user = raw_input("Username: ")
pwd = raw_input("Password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username=user, password=pwd)

platform = ssh.exec_command("uname -s")
os = ssh.exec_command("uname -n")
hardware = ssh.exec_command("uname -i | cut -c1-3")
osversion = ssh.exec_command("lsb_release -d | cut -d' ' -f2")
kernelversion = ssh.exec_command("uname -r")

ssh.close()

con = sqlite3.connect('exploits_metadata.db')
cursor = con.cursor()
for row in cursor.execute("SELECT * FROM EXPLOITS WHERE Platform=? AND (OperatingSystem=? OR \
OperatingSystem='No constraints') AND Architecture=? AND OsVersion=? AND KernelVersion=?", \
(platform, os, hardware, osversion. kernelversion)):
    print row



