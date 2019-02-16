import re
import string
import collections

def GetPunctuation():
    punctuations = ''
    for symbol in string.punctuation:
        punctuations += re.escape(symbol)
    return punctuations

def removePattern(pattern, string):
    return re.sub(pattern, ' ', string, re.MULTILINE)
 
def bagOfWords(document):    
    data = re.sub('\\n', ' ', document, re.MULTILINE)
    dataLowerWithoutPunctuation = removePattern('['+ GetPunctuation() + ']', data.lower())
    removeDuplicatedSpace = re.sub(' +', ' ', dataLowerWithoutPunctuation.strip())
    CounterWords = collections.Counter(re.split(' ', removeDuplicatedSpace))
    return CounterWords

phrases = file('phrases.txt', 'r')
print(bagOfWords(phrases.read()))