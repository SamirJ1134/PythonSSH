#!/usr/bin/python3
 
import paramiko
import getpass
 
infile=open('/Users/ip.txt', 'r')
ip = 'x.x.x.x'
for line in infile:
    user = input("username: ")
    passwd = getpass.getpass("password: ")
    ip = line.split('\n')
    ip = line.rstrip()
    client=paramiko.SSHClient()
    client.load_host_keys('/Users/samir/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        out=open('out.txt', 'a')
        stdin, stdout, stderr = client.exec_command('cat /etc/hostname')
        out.write(stdout.read().decode('utf8'))
        stdin.close()
        stdout.close()
        stderr.close()
        stdin, stdout, stderr = client.exec_command('ls  /var/www')
        if stdout == '':
            out.write('This directory is empty')
        else:
            out.write('This directory has files in it')
        stdin.close()
        stdout.close()
        stderr.close()
        out.close()
        client.close()
 
infile.close()
