'''
    Explanation I:
        - We can use a lookup dict to match these characters to integers
        - Each time we see a new char, we increase the iterator and sort using the lambda function

    Explanation II:
        - Count the elemtns of T
        - If we have some count[char] = number of occurences of char in T, we can return these elements in any order
        - The order is S + (characters not in S in any order)
        
        TC - O(len(S) + len(T))
        SC - O(len(T)
'''

import collections

class Solution1:
    def customSortString(self, order: str, s: str) -> str:
        lookup = collections.defaultdict(int)
        i = 0
        
        for c in order:
            lookup[c] = i
            i += 1
            
        return "".join(sorted(s, key=lambda x: lookup[x]))

# COUNT AND WRITE        
class Solution2(object):
    def customSortString(self, S, T):
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = collections.Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S. That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)