temp = "racecar"
tempLength = len(temp)
for i, letter in enumerate(temp):
    if not (temp[i:i+1]==temp[tempLength-(1+i):tempLength-i]):
        print(False)
print(True)