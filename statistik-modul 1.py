import re

buffer = open('/Users/mischu/Desktop/Intern/statistiktool/1.txt', 'r').read()
matches = re.findall(r'\d\d\/\w\w\w\/\d\d\d\d', buffer)
print matches
