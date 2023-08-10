import subprocess
import re

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    output = output.decode()
    #print(output)# error.decode()))
    for line in output:
        if re.search("IPv4 Address", line):
            print(line)

run_command("ipconfig")