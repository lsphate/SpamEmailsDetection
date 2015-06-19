import glob, os, csv
from snowballstemmer import stemmer
from stop_words import get_stop_words

stmr = stemmer('english')
stopWords = [str(x) for x in get_stop_words('en')]
puncs = ['(', ')', '[', ']', '{', '}', '<', '>', '"', ".", ',', '@', '?', '!', '+', '$', '&', '*', ':', ';' '/', '\\', '_', '%', '#', '^', '=', '~', '`', '\'', '-']
dict = []
lenFilter = 2

# Read in Dictionary File
print "Loading Dictionary..."
for row in csv.reader(open("Dictionary.csv", "r")):
    dict = row
print "Dictionary length: " + str(len(dict))
print "=" * 80

testTA =  csv.writer(open("testTA.csv", "wb"))

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

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

print "Parsing Spam Vector of TA testing Part..."
os.chdir("./TAtest/")
for file in glob.glob("*.txt"):
    GenerateVector(file, testTA)

