# first solution
# def robot_original_position(moves):
	# angle = 0
	# for move in moves:
	# 	if(move == "L"):
	# 		angle -= 180
	# 	elif(move == "R"):
	# 		angle += 180
	# 	elif(move == "U"):
	# 		angle += 90
	# 	elif(move == "D"):
	# 		angle -= 90

	# if(angle == 0):
	# 	return True
	# else:
	# 	return False

# second solution - best solution
def robot_original_position2(moves):
	if(moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")):
		return True
	else:
		return False