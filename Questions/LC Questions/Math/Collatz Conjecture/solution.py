# n = 5

# even => n/2, odd => 3n+1
#  reach 1


# 5, 16, 8, 4, 2, 1 => 5
# 10, 5 = 5+1 = 6


# {1:0, 5:5, 16:4, 8:3, 4:2, 2:1}

class CollatzConjecture:
    def _init_(self):
        self.cache = { 1: 0 } # number : steps

    def steps(self, number):

        start = number # 4   3   2   1
        steps = [] # [5, 16, 8, 4, 2]

        while (start != 1):

            if start in self.cache:
                break

            steps.append(start)

            if (start % 2 == 0):
                start = start // 2
            else:
                start = (3*start)+1
        
        totalSteps = self.cache.get(start, 0) + 1

        while steps:
            curr = steps.pop()
            self.cache[curr] = totalSteps
            totalSteps += 1

        return self.cache[number]