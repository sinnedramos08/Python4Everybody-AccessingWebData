'''
The basic outline of this problem is to read the file, 
look for integers using the re.findall(), looking for a 
regular expression of '[0-9]+' and then converting the extracted 
strings to integers and summing up the integers.
'''
import re
fh=open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-AccessingWebData\Regular Expression\regex_sum_1474882.txt")


numlist=[]
for line in fh:
    line=line.rstrip()
    num=re.findall("([0-9]+)",line)
    if len(num)<1: 
        continue
    for i in range(len(num)):
        numlist.append(int(num[i]))

print(sum(numlist))