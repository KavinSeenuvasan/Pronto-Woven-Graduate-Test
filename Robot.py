def getMinimumDistance(inputValue):
    if(inputValue==''):
        return "String cannot be empty"

    #Initialize x and y coordinates
    pos=[0,0]

    direction=['N','E','S','W']
    commandList=['F','B','L','R']
    currentDirection=0 #Setting default current facing direction of robot is North

    inputValue=inputValue.split(',')

    #Move robot on valid moves
    for value in inputValue:
        command=value[0]
        if command not in commandList:
            return "Invalid command"
        number=int(value[1])

        #Calculate the position of the robot according to the input given
        if command == 'F':
            if direction[currentDirection] == 'N':
                pos[1]=pos[1]+number
            elif direction[currentDirection] == 'E':
                pos[0]=pos[0]+number
            elif direction[currentDirection] == 'S':
                pos[1]=pos[1]-number
            else:
                pos[0]=pos[0]-number

        elif command == 'B':
            if direction[currentDirection] == 'N':
                pos[1]=pos[1]-number
            elif direction[currentDirection] =='E':
                pos[0]=pos[0]-number
            elif direction[currentDirection] == 'S':
                pos[1]=pos[1]+number
            else:
                pos[0]=pos[0]+number

        elif command == 'R':
            currentDirection=(currentDirection+number)%4

        else:
            currentDirection=abs(currentDirection-number)%4

    #Calculate distance
    distance=abs(pos[0])+abs(pos[1])
    return "Minimum distance required to get back to the starting point is: " + str(distance)

print(getMinimumDistance(input("Enter the input value separated by comma:")))
