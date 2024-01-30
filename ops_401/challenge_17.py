def get_host ():
        host = input ("Enter an SSH Client to connect to or enter for default:") or "IP"
        return host 

def get_user():
        user=

def get_password():
        password= getpass.getpass(promp=Please provide a password")
                                  
def ssh_client():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramike.AutoAddPolicy())
    try:
        ssh.connect(get_host()), port, get_user(), get_password())
        stdin, stdout, stderr = ssh.exec_command('whoami')
        time.sleep(3)
        output = stdout.read()
        print ("_" * 50)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls-l")
        time.sleep(3)
        output = stdoubt.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command(uptime)
        time.sleep(3)
         output = stdoubt.read()
        print(output)
        print ("_" * 50)