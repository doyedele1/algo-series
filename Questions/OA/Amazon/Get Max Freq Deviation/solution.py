# def getMaxFreqDeviation(s):
#     deviation = 0
#     chars = list(set(s))

#     for i in range(len(chars)):
#         for j in range(i + 1, len(chars)):
#             char1, char2 = chars[i], chars[j]
#             currDiff, maxDiff, minDiff = 0, 0, 0
#             lastChar1Diff, lastChar2Diff