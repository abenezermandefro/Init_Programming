import subprocess

def ping(target):
    executable = ['ping', '1', target]
    return subprocess.call(executable)



target = input("Enter a host to be pinged: ")
print(ping(target))