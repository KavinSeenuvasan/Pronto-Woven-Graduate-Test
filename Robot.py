def getMinimumDistance(inputValue):

    #get x and y coordinates
    pos = [0,0]

    direction = ['N','E','S','W']
    currentDirection = 0 #default current facing direction of robot is North

    inputValue=inputValue.split(',')

    #Move robot on valid moves
    for inp in inputValue:
        movement = inp[0]
        val= int(inp[1])

        #calculating the position of the robot according to the value given
        if movement =='F':
            if direction[currentDirection]=='N':
                pos[1]=pos[1]+val

            if direction[currentDirection]=='E':
                pos[0]=pos[0]+val

            if direction[currentDirection]=='S':
                pos[1]=pos[1]-val

            if direction[currentDirection]=='W':
                pos[0]=pos[0]-val

        if movement =='B':
            if direction[currentDirection]=='N':
                pos[1]=pos[1]-val

            if direction[currentDirection]=='E':
                pos[0]=pos[0]-val

            if direction[currentDirection]=='S':
                pos[1]=pos[1]+val

            if direction[currentDirection]=='W':
                pos[0]=pos[0]+val

        if movement=='R':
            currentDirection=(currentDirection+val)%4
        if movement=='L':
            currentDirection=abs(currentDirection-val)%4

        #prints the current position of the robot as every move
        print("x,y:", pos[0],pos[1])

    #get distance
    distance=abs(pos[0])+abs(pos[1])
    print("Distance required to travel from ending position " + str(pos) +" to starting position [0,0] is " + str(distance))

#give the input
getMinimumDistance(input("Enter the input value separated by comma: "))
