def findWinner(s):
    wendyMoves, bobMoves = 0, 0

    for i in range(len(s) - 2):
        if s[i:i+3] == 'www': wendyMoves += 1
        if s[i:i+3] == 'bbb': bobMoves += 1

    if bobMoves <= wendyMoves: return('wendy')
    else: return('bob')