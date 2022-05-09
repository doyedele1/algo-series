class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        
        for i in range(len(colors) - 2):
            if colors[i:i+3] == 'AAA':
                alice += 1
            if colors[i:i+3]=='BBB':
                bob += 1
        
        if alice > bob: return True
        else: return False