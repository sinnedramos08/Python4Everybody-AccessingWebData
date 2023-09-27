import re

fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-AccessingWebData\Regular Expression\mbox.txt")

for line in fh:
    line=line.rstrip()
    if re.search("^From:", line): #The symbol '^' means starts with
        print(line)

fh.seek(0)