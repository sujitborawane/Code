import re
s = "G.H.Raisoni"
match = re.search('Raisoni',s)
print('Start Index:',match.start())
print('End Index:',match.end())