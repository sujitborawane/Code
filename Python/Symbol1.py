import re
string = "Hello World!"
pattern = "World!$"
match = re.search(pattern, string)
if match:
    print("Match Found")
else:
    print("Not Found")