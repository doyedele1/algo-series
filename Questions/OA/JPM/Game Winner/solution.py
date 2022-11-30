def gameWinner(colors):
    wendyMoves, bobMoves = 0, 0

    for i in range(len(s) - 2):
        if colors[i:i+3] == "www": wendyMoves += 1
        if colors[i:i+3] == "bbb": bobMoves += 1

    if wendyMoves > bobMoves: return("wendy")
    else: return("bob")
