from collections import defaultdict

def countSentences(wordSet, sentences):
    wordCount = defaultdict(int)
    for word in wordSet:
        word = ''.join(sorted(word))
        wordCount[word] += 1

    res = []

    for sentence in sentences:
        words = sentence.split(' ')
        count = 1
        for word in words:
            k = ''.join(sorted(word))
            if k in wordCount:
                count *= wordCount[k]
        res.append(count)

    return res