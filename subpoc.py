import subprocess
import re

let = False
point_counter = 0
point = 0



pattern = r'\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}\.{1}\d{1,3}'


def cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    global cat
    cat = output.decode()
    print(cat)
    


cmd("ipconfig")   


coincidence = re.findall(pattern, cat)


for ip in coincidence:
    print("ipaddr", ip)

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


