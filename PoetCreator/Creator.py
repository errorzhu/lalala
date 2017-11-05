# -*-  coding: utf-8 -*-
import random


def genMap(text):
    text = text.replace('\n', ' ')
    text = text.replace('\“', '')
    text = text.replace('\”', '')
    text = text.replace('（', '')
    text = text.replace('）', '')
    punc = ['，', '。', '？', '；', ':', '!', '：', '！', '“', '”']
    for symbol in punc:
        # text = text.replace(symbol, ' ' + symbol + ' ')
        text = text.replace(symbol, '')
        text = text.replace(' ', '')
    # words = text.split(' ')
    tempwords = [word.encode('utf8') for word in text.decode('utf8') if word != '']
    words = tempwords
    wordDict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            # 为单词新建一个词典
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] = wordDict[words[i - 1]][words[i]] + 1
    return wordDict


def wordLenth(wordDict):
    sum = 0
    for k, v in wordDict.items():
        sum += v
    return sum


def getRandomWord(wordDict):
    index = random.randint(1, wordLenth(wordDict))
    for k, v in wordDict.items():
        index -= v
        if index <= 0:
            return k


def main():
    with open('target', 'r') as f:
        text = str(f.read())
        wordDict = genMap(text)
        currentWord = '君'
        line = 4
        length = 5
        result = ''
        for n in range(0, line):
            for i in range(0, length):
                result += currentWord
                currentWord = getRandomWord(wordDict[currentWord])
            result += '\n'

        print result


if __name__ == "__main__":
    main()
