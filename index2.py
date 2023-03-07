txt = '00002'
import re

regexpattern = "^0+(?!$)"
os = re.sub(regexpattern, "", txt)
print(int(os))