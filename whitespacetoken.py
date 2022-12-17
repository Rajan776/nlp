import re
from nltk.tokentize import RegexpTokeinzer
tk=RegexpTokenizer(\s+',gaps=True)
gfg="MSC PART2 KC-COLLEGE"
msc=tk.tokenize(gfg)
print(msc)
Sentence="BASKETBALL,HOCKEY;GOLF,TENNIS"
print(re.split(';',Sentence))
print(re.split(',',Sentence))
