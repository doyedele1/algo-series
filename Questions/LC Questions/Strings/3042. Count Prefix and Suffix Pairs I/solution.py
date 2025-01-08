class BruteForceSolution1:
    def count_prefix_suffix_pairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count
    
class BruteForceSolution2:
    def is_prefix(self, str1, str2):
        m = len(str1)
        n = len(str2)

        if m > n:
            return False
        
        for i in range(m):
            if str1[i] != str2[i]:
                return False
        return True

    def is_suffix(self, str1, str2):
        m = len(str1)
        n = len(str2)

        if m > n:
            return False
        
        for i in range(m - 1, -1, -1):
            if str1[i] != str2[n - m + i]:
                return False
        return True

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count