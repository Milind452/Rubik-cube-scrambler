class Cube:

    # Tuple for each face of the cube
    faces = ('F', 'R', 'U', 'L', 'B', 'D')

    # Tuple for each direction that a face can be turned (Example: 0 - F | 1 - F2 | 2 - F')
    turns = (0, 1, 2)

    # 3D matrix of the cube
    cube = [[['w', 'w', 'w'],             # 000  001  002
             ['w', 'w', 'w'],             # 010  011  012
             ['w', 'w', 'w']],            # 020  021  022

            [['o', 'o', 'o'],             # 100  101  102
             ['o', 'o', 'o'],             # 110  111  112
             ['o', 'o', 'o']],            # 120  121  122

            [['g', 'g', 'g'],             # 200  201  202
             ['g', 'g', 'g'],             # 210  211  212
             ['g', 'g', 'g']],            # 220  221  222

            [['r', 'r', 'r'],             # 300  301  302
             ['r', 'r', 'r'],             # 310  311  312
             ['r', 'r', 'r']],            # 320  321  322

            [['b', 'b', 'b'],             # 400  401  402
             ['b', 'b', 'b'],             # 410  411  412
             ['b', 'b', 'b']],            # 420  421  422

            [['y', 'y', 'y'],             # 500  501  502
             ['y', 'y', 'y'],             # 510  511  512
             ['y', 'y', 'y']]]            # 520  521  522


	# Order of rotation for different turns
	link = {'F': ((0, 2, 0), (0, 2, 1), (0, 2, 2),
				(3, 0, 0), (3, 1, 0), (3, 2, 0),
				(5, 0, 2), (5, 0, 1), (5, 0, 0),
				(1, 2, 2), (1, 1, 2), (1, 0, 2)),

			'R': ((0, 2, 2), (0, 1, 2), (0, 0, 2),
				(4, 0, 0), (4, 1, 0), (4, 2, 0),
				(5, 2, 2), (5, 1, 2), (5, 0, 2),
				(2, 2, 2), (2, 1, 2), (2, 0, 2)),

			'U': ((3, 0, 2), (3, 0, 1), (3, 0, 0),
				(2, 0, 2), (2, 0, 1), (2, 0, 0),
				(1, 0, 2), (1, 0, 1), (1, 0, 0),
				(4, 0, 2), (4, 0, 1), (4, 0, 0)),

			'L': ((0, 0, 0), (0, 1, 0), (0, 2, 0),
				(2, 0, 0), (2, 1, 0), (2, 2, 0),
				(5, 0, 0), (5, 1, 0), (5, 2, 0),
				(4, 2, 2), (4, 1, 2), (4, 0, 2)),

			'B': ((3, 2, 2), (3, 1, 2), (3, 0, 2),
				(0, 0, 2), (0, 0, 1), (0, 0, 0),
				(1, 0, 0), (1, 1, 0), (1, 2, 0),
				(5, 2, 0), (5, 2, 1), (5, 2, 2)),

			'D': ((1, 2, 0), (1, 2, 1), (1, 2, 2),
				(2, 2, 0), (2, 2, 1), (2, 2, 2),
				(3, 2, 0), (3, 2, 1), (3, 2, 2),
				(4, 2, 0), (4, 2, 1), (4, 2, 2))}

	# Order of rotation within a face
	faceLink = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0))

	# Coordinate of each face in the cube matrix
	center = {'F': (2,), 'R': (3,), 'U': (0,), 'L': (1,), 'B': (4,), 'D': (5,)}

	def showCube():
		"""
		Prints the cube in a manner that is easy to contemplate
		"""
		
		for i in range(0, 3, 1):
			for j in range(0, 3, 1):
				print(" ", end=" ")
			print(" ", end="  ")
			for k in range(0, 3, 1):
				print(cube[0][i][k], end=" ")
			print("\n")
			
		for i in range(0, 3, 1):
			for j in range(1, 5, 1):
				for k in range(0, 3, 1):
					print(cube[j][i][k], end=" ")
				print(" ", end="  ")
			print("\n")
			
		for i in range(0, 3, 1):
			for j in range(0, 3, 1):
				print(" ", end=" ")
			print(" ", end="  ")
			for k in range(0, 3, 1):
				print(cube[5][i][k], end=" ")
			print("\n")
		
	def swap(a, b):
    """
    Swaps two elements in the cube matrix whose coordinates are given as inputs
    @param a - First coordinate
    @param b - Second coordinate
    """
    tmp = cube[a[0]][a[1]][a[2]]
    cube[a[0]][a[1]][a[2]] = cube[b[0]][b[1]][b[2]]
    cube[b[0]][b[1]][b[2]] = tmp

	def rotate(face, turn=1):
    """
    Rotates the given face by the given number of turns
    @param face - The face that is to be rotated
    @param turn - The number of turns to be performed on the given face; default value set to 0
    """
   
    for i in range(turn):
        for x in range(0, 3, 1):
            for y in range(3, 12, 3):
                swap(link[face][x],link[face][y + x])
        x = center[face]
        for y in range(0, 2, 1):
            for z in range(2, 8, 2):
                swap(x + faceLink[y], x + faceLink[z + y])