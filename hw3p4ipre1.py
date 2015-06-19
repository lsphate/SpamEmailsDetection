import glob, os, csv
from snowballstemmer import stemmer
from stop_words import get_stop_words

stmr = stemmer('english')
stopWords = [str(x) for x in get_stop_words('en')]
puncs = ['(', ')', '[', ']', '{', '}', '<', '>', '"', ".", ',', '@', '?', '!', '+', '$', '&', '*', ':', ';' '/', '\\', '_', '%', '#', '^', '=', '~', '`', '\'', '-']
dict = []
lenFilter = 2

Dictionary = csv.writer(open("Dictionary.csv", "wb"))
trainS =  csv.writer(open("trainS.csv", "wb"))
trainH = csv.writer(open("trainH.csv", "wb"))
testS =  csv.writer(open("testS.csv", "wb"))
testH = csv.writer(open("testH.csv", "wb"))

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def CreateDictionary(path):
    print path
    for line in open(path):
        # Remove punctuations
        for ch in puncs:
            line = line.replace(ch, ' ')
        # Split words
        for word in line.split():
            try:
                w = stmr.stemWord(word.lower())
                if len(w) > lenFilter and RepresentsInt(w) == False and w not in stopWords and w not in dict:
                    dict.append(stmr.stemWord(word.lower()))
            except UnicodeDecodeError:
                continue


def GenerateVector(path, output):
    print path
    v = [0] * len(dict)
    for line in open(path):
        # Remove punctuations
        for ch in puncs:
            line = line.replace(ch, ' ')
        # Split words
        for word in line.split():
            try:
                w = stmr.stemWord(word.lower())
                if len(w) > lenFilter and RepresentsInt(w) == False and w not in stopWords and w in dict:
                    pos = dict.index(w)
                    try:
                        v[pos] += 1
                    except IndexError:
                        continue
            except UnicodeDecodeError:
                continue
    output.writerow(v)


# Create Dictionary File
print "Creating Dictionary Libiary..."
print "Walking Through Spam..."
os.chdir("./Training/spam/")
for file in glob.glob("*.txt"):
    CreateDictionary(file)

print "Walking Through Ham..."
os.chdir("../ham/")
for file in glob.glob("*.txt"):
    CreateDictionary(file)

print "Dumping Dictionary file..."
Dictionary.writerow(dict)

# print Dict
print len(dict)
print "=" * 80

print "Generating Vector..."
print "Parsing Spam Vector of Training Part..."
os.chdir("../spam/")
for file in glob.glob("*.txt"):
    GenerateVector(file, trainS)

print "Parsing Ham Vector of Training Part..."
os.chdir("../ham/")
for file in glob.glob("*.txt"):
    GenerateVector(file, trainH)

print "Parsing Spam Vector of Testing Part..."
os.chdir("../../Testing/Spam/")
for file in glob.glob("*.txt"):
    GenerateVector(file, testS)

print "Parsing Ham Vector of Testing Part..."
os.chdir("../ham/")
for file in glob.glob("*.txt"):
    GenerateVector(file, testH)
