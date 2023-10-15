# to search and replace the text in filename in all files recursively
import os
import SearchandReplaceinFile
import sys
from datetime import datetime

path = os.getcwd() + "/"
print("Calling_Dir: "+ path)

# Get search and replace text from CLI arguments in string
search_string = sys.argv[1]
replace_string = sys.argv[2]

# Get debug log file path
dpath=os.path.join(os.path.expanduser("~"),"py_debug","debug")
if not os.path.exists(dpath):
    os.makedirs(dpath)
d_fpath=os.path.join(dpath,"S&RAllText.txt")
open(d_fpath, 'w').close()
current_time = datetime.now()
timestamp_str = current_time.strftime("%d/%m/%Y, %H:%M:%S")
open(d_fpath,"a").write("Timestamp (DD-MM-YY): " + timestamp_str + '\n')

for root, dirs, files in os.walk(path):
     for name in files:
      if ".swp" not in name and ".nfs" not in name:
        SearchandReplaceinFile.FSearchandReplaceinFile(root + "/" + name, search_string, replace_string, d_fpath)
