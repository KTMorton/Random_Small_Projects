
inputFile = "usdeclar.txt"
outputFile = "usdeclarclean.txt"

inFile = open(inputFile)
outFile = open(outputFile, "w+")

punctuation = [';',':',',','.','!','?','[', ']']
special = ['\n']
wordList = {}

for line in inFile:
    for word in line:
        for char in word:
            if char in punctuation:
                line = line.replace(char, '')
            if char in special:
                line = line.replace(char, " ")
    outFile.write(line)


inFile.close()
outFile.close()

outFile = open(outputFile, "r")

for line in outFile:
    line = line.split(" ")
    for word in line:
        if word in wordList:
            wordList[word] += 1
        else:
            wordList[word] = 1
wordList.pop('')
print(len(wordList))
wordListKeys = []
wordListValues = []
# for i in wordList.values():
#     wordListValues.append(i)
#
# wordListValues.sort()
# for i in wordListValues:
#     for key, value in wordList.items():
#         if value == i and key not in wordListKeys:
#             wordListKeys.append(key)

#sort alphabetically by key
for i in wordList.keys():
    print(i)
    wordListKeys.append(i)
print(wordListKeys)
wordListKeys.sort()

for i in wordListKeys:
    wordListValues.append(wordList.get(i))

#scrabble scorer
scoreDict = {'A':1, 'B':3,'C':3, 'D':2, 'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
scores = []
for word in wordListKeys:
    total = 0
    for char in word:
        if char.upper() in scoreDict:
            total += scoreDict.get(char.upper())
    scores.append(total)



for j in range(len(wordListKeys)):
    print(wordListKeys[j], wordListValues[j], " Scrable Score: " + str(scores[j]))

outFile.close()