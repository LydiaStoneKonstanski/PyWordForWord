import os
import string

# do the read line by line.

print(">>> start")

print(os.getcwd())

def kprint(filename):
    file = open(filename, "r")
    while True:
        content=file.readline()
        if not content:
            break
        print(content, end="")
    file.close()


def kreadfile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def kprintwc(filename):
    txt = kreadfile(filename)
    testtuple = wc(txt)
    print(testtuple, filename)

def kwritefile(filename, content):
    file = open(filename, "w")
    file.writelines(str(content))
    file.close()

def kappendfile(filename, content, title, use_divider=False):
    file = open(filename, "a")
    divider = "\n-----------\n\n"
    file.write(str(title + "\n"))
    file.writelines(str(content))
    if use_divider:
        file.write(divider)
    file.write("\n")
    file.close()


def wc(inputstring):
    chs = 0 # characters
    wds = 0 # words
    lns = 0 # lines

    chs = len(inputstring)

    for ch in inputstring:
        if ch == '\n':
            lns += 1

    wds = len([word.strip(string.punctuation) for word in inputstring.split()])
    result = {
        "Lines": lns,
        "Words": wds,
        "Characters": chs
    }
    return result


def wordFrequency(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]

    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

def letterFrequency(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]
    # print(wdlist)

    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        chword = list(word) # 'kris' -> ['k'....
        for ch in chword:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1

    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

def wordDistribution(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]
    wdlistlen = len(wdlist)
    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return {k: v/wdlistlen for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

def letterDistribution(inputstring):
    d = {}
    wdlist = [word.strip(string.punctuation).lower() for word in inputstring.split()]
    ltlistlen = 0
    # d = {'kris': 1, 'chris': 1, 'lydia': 2} if the 'kris chris lydia lydia'
    for word in wdlist:
        chword = list(word)  # 'kris' -> ['k'....
        for ch in chword:
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1
                ltlistlen += 1

    return {k: v/ltlistlen for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}



if __name__ == "__main__":
    input_filenames = [
        "testdata/testdata0.txt",
        "testdata/testdata1.txt",
        "testdata/testdata2.txt",
        "testdata/testdata3.txt",
        "testdata/testdata4.txt",
        "testdata/testdata5a.txt",
        "testdata/testdata6.txt",
        "testdata/testdata7.txt",
    ]
    output_filename = "ResultsOfProcessing.txt"
    #Clear the contents of the output file
    file = open(output_filename, "w")
    file.close()

    for input_filename in input_filenames:
        kappendfile(output_filename, input_filename, "File Name")
        content = kreadfile(input_filename)

        w_dist = wordDistribution(content)
        kappendfile(output_filename, w_dist, "Word Distribution")

        let_dist = letterDistribution(content)
        kappendfile(output_filename, let_dist, "Letter Distribution")

        let_frequency = letterFrequency(content)
        kappendfile(output_filename, let_frequency, "Letter Frequency")

        w_frequency = wordFrequency(content)
        kappendfile(output_filename, w_frequency, "Word Frequency")

        word_count = wc(content)
        kappendfile(output_filename, word_count, "Word Count", True)



    #kprintwc(filename)
    # for n in range(8):
    #     # there is a weird file name in the input datasets.
    #     t = '5a' if n == 5 else str(n)
    #     fname = "testdata/testdata" + t + ".txt"
    #     kprintwc(fname)

    # print(wordFrequency('kris chris lydia lydia'))
    # print(wordFrequency(kreadfile("testdata/testdata0.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata1.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata2.txt")))
    # print(wordFrequency(kreadfile("testdata/testdata3.txt")))
    #
    # randj = wordFrequency(kreadfile("testdata/testdata3.txt"))
    # for w in sorted(randj, key=randj.get, reverse=True):
    #     print(w, randj[w])

    # for n in range(8):
    #     # there is a weird file name in the input datasets.
    #     t = '5a' if n == 5 else str(n)
    #     fname = "testdata/testdata" + t + ".txt"
    #     print(wordFrequency(kreadfile("testdata/testdata3.txt")))
    #
    # print(letterFrequency('kris chris lydia lydia'))
    #
    # for n in range(8):
    #     # there is a weird file name in the input datasets.
    #     t = '5a' if n == 5 else str(n)
    #     fname = "testdata/testdata" + t + ".txt"
    #     print(fname, letterFrequency(kreadfile(fname)))
