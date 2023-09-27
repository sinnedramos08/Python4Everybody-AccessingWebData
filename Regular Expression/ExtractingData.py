import re
fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-AccessingWebData\Regular Expression\mbox.txt")

#Extract all the "X-DSPAM-Confidence: #" numbers
numlist=[]
for line in fh:
    line=line.rstrip()
     #note: characters in set enclosed in brackets are the only 
     #characters recognized by regex to be included, in this case 
     #characters 0-9 and dot only are included
     #adding specific characters like: abc, $, %, need to be declared
     #in the brackets to be included
    xdspam_line=re.findall("X-DSPAM-Confidence: ([0-9.]+)", line) 
    if len(xdspam_line) <1:
        continue   
    num=float(xdspam_line[0])
    numlist.append(num)

print(f"Max: {max(numlist)}")
