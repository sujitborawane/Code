import re
string = "The quick brown fox jump over the lazy dog"
pattern = "[a-m]"
result = re.findall(pattern, string)
print(result)