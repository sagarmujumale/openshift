import os
import socket

def playbook():
  cmd = 'ansible-playbook gitlab.yml'
  os.system(cmd)

def cert():
  while True:
    try:
      cert = raw_input("Enter the certificate name with full path. eg. /root/cert.pem  \n")
      f = open(cert,'r')
      move = "cp -rf " + cert + " gitlab/files/server-cert.pem"
      print(move)
      os.system(move)
      break
    except IOError:
      print("Provided cert file is either not exists or inaccessible")

def cert_key():
  while True:
    try:
      cert = raw_input("Enter the certificate key name with full path. eg. /root/key.pem  \n")
      f = open(cert,'r')
      move = "cp -rf " + cert + " gitlab/files/server-key.pem"
      print(move)
      os.system(move)
      break
    except IOError:
      print("Provided certificate key is either not exists or inaccessible")

def env():
  os.system("yum install epel-release")
  os.system("yum install ansible docker")
  os.system("systemctl restart docker")
  print("""################################################################################################################################### "
"Press 'yes/y/YES' if certificates are placed in gitlab/files directory. if not then press 'no/n/NO' to provide certificate path. "
"###################################################################################################################################""")
  cmd = "sed -i.bak '/GIT_HOST:/d' gitlab/vars/main.yml"
  os.system(cmd)
  host = socket.gethostname()
  HOSTNAME = 'GIT_HOST: ' + host
  with open("gitlab/vars/main.yml", "a+") as file_object:
    file_object.write(HOSTNAME + "\n")

def __main__():
  env()
  keeper = None
  yes = {"yes", "y", "Yes", "YES"}
  no = {"no", "n", "No", "NO"}
  while keeper not in ("yes", "no", "y", "n", "Yes", "No", "YES", "NO"):
    keeper = raw_input("Enter your choice:- ").lower()
    if keeper in yes:
      print("Installation has been started......")
      playbook()
      break
    if keeper in no:
      cert()
      cert_key()
      playbook()
      break
    else:
      print(" Invalid choice... Please enter yes or no.")

__main__()
