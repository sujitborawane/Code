import re
string = "The quick brown fox jump over the lazy dog"
pattern = "q..k"
match = re.search(pattern, string)
if match:
    print("Match Found")
else:
    print("Not Found")