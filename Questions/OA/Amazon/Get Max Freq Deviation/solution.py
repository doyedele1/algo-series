def getMaxFreqDeviation(s):
    res = 0
    chars = list(set(s))

    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            char1, char2 = chars[i], chars[j]
            currDiff, maxDiff, minDiff, lastChar1Diff, lastChar2Diff = 0, 0, 0, 0, 0
            meetChar1, meetChar2 = False, False
            
            for char in s:
                if char == char1:
                    meetChar1 = True
                    currDiff += 1
                    maxDiff = max(lastChar1Diff, maxDiff)

                    lastChar1Diff = currDiff
                
                elif char == char2:
                    meetChar2 = True
                    currDiff -= 1
                    minDiff = min(lastChar2Diff, minDiff)
                    lastChar2Diff = currDiff
                
                else: continue

                if meetChar1 and meetChar2:
                    res = max(currDiff - minDiff, maxDiff - currDiff, res)
            
            return res

# print(getMaxFreqDeviation("aabb"))