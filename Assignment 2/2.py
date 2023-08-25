import sys
number_of_words = 0
st = ""
with open(r'input.txt', 'r') as file: # open input file and read
    data = file.read()          #split file
    lines = data.split()        #add words to line
    print(lines)
    wordcount= {}
for word in lines:           #word count dict
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
print(wordcount)
sys.stdout = open('output.txt', 'w') #writting console to output file
sys.stdout.close()
