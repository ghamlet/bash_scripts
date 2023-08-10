import subprocess
import re

let = False
point_counter = 0
point = 0



pattern = re.compile("\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}")


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    global cat
    cat = output.decode()
    print(cat)
    


run_command("ping 192.168.0.1")   


coincidence = re.search(pattern, cat, flags=0)
if coincidence:
    print("ipaddr", coincidence[0])

# for i in range(x,len):
#     if (cat[i] == "." or cat[i] == " ") and let == False:
        
#         continue
#     elif cat[i] == ":":
#         addr = "".join([addr, ""])
#         let = True

#     elif let == True and point_counter == False:
#         addr = "".join([addr, cat[i]])
#         point+=1
#         if point ==3:
#             point_counter = True

#     else:
#         addr = "".join([addr, cat[i]])


