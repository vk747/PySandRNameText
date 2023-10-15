# to search and replace the pattern in filename in all files recursively
import os
import sys
from datetime import datetime

path = os.getcwd() + "/"
print("Calling_Dir: "+ path)

# Get search and replace name from CLI arguments in string
search_name = sys.argv[1]
replace_name = sys.argv[2]

# Get debug log file path
dpath=os.path.join(os.path.expanduser("~"),"py_debug","debug")
if not os.path.exists(dpath):
    os.makedirs(dpath)
d_fpath=os.path.join(dpath,"S&RAllName.txt")
open(d_fpath, 'w').close()
current_time = datetime.now()
timestamp_str = current_time.strftime("%d/%m/%Y, %H:%M:%S")
open(d_fpath,"a").write("Timestamp (DD-MM-YY): " + timestamp_str + '\n')
open(d_fpath,"a").write("----------------------------------------------------------------\n")

for (root, dirs, file) in os.walk(path):
    for f in file:
        if search_name in f:
            string = f
            #print("ROOT:"+root)
            #print("STRING:"+string)
            string_1 = string.replace(search_name,replace_name)
            #print("STRING_1:"+string_1)
            if root[-1] == "/":
              #print(root+string)
              os.rename(root+string, root+string_1)
              #print(root+string+" replaced with "+root+string_1)
              open(d_fpath,"a").write(root+string+" replaced with "+root+string_1 + '\n')
              open(d_fpath,"a").write("----------------------------------------------------------------\n")
            else:
              #print(root+"/"+string)
              os.rename(root+"/"+string, root+"/"+string_1)
              print(root+"/"+string+" replaced with "+root+"/"+string_1)
              # Problem here
              open(d_fpath,"a").write(root+"/"+string+" replaced with "+root+"/"+string_1 + '\n')
              open(d_fpath,"a").write("----------------------------------------------------------------\n")
