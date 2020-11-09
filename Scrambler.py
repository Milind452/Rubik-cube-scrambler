class Scrambler:
    scrambleLength = 25
    def generateScramble(faces, turns):
        """
        Generates a random scramble of 20 turns.
        @param faces - tuple containing all 6 faces of the cube (F, R, U, L, B, D)
        @param turns - tuple containing all types of turns possible on a cube (F, F2, F')

        @return scramble - list of the genearated scramble
        """

        scramble = list()
        for i in range(0, scrambleLength, 1):
            tmp = random.randint(0, len(turns) - 1)
            if tmp == 0:
                scramble.append(faces[random.randint(0, len(faces) - 1)] + "")
            elif tmp == 1:
                scramble.append(str(faces[random.randint(0, len(faces) - 1)]) + "2")
            else:
                scramble.append(str(faces[random.randint(0, len(faces) - 1)]) + "'")

        return self.fixScramble(scramble)

    def Scrambler():
        for x in scramble:
            face = x[0]
            if len(x) < 2:
                direction = None
            else:
                direction = x[1]
            turn = 0
            if direction == "'":
                turn = 3
            elif direction == "2":
                turn = 2
            else:
                turn = 1
            rotate(face, turn)

