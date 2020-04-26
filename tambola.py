data = {}
data[1, 0, 1] = [11, False]
data[1, 0, 4] = [40, False]
data[1, 0, 5] = [50, False]
data[1, 0, 7] = [71, False]
data[1, 0, 8] = [87, False]
data[1, 1, 0] = [4, False]
data[1, 1, 2] = [28, False]
data[1, 1, 3] = [31, False]
data[1, 1, 5] = [55, False]
data[1, 1, 6] = [68, False]
data[1, 2, 1] = [16, False]
data[1, 2, 3] = [34, False]
data[1, 2, 4] = [44, False]
data[1, 2, 6] = [69, False]
data[1, 2, 8] = [90, False]

data[2, 0, 2] = [29, False]
data[2, 0, 3] = [31, False]
data[2, 0, 4] = [41, False]
data[2, 0, 5] = [51, False]
data[2, 0, 6] = [63, False]
data[2, 1, 0] = [1, False]
data[2, 1, 1] = [10, False]
data[2, 1, 3] = [32, False]
data[2, 1, 6] = [65, False]
data[2, 1, 7] = [70, False]
data[2, 2, 0] = [9, False]
data[2, 2, 4] = [49, False]
data[2, 2, 6] = [69, False]
data[2, 2, 7] = [79, False]
data[2, 2, 8] = [86, False]

data[3, 0, 2] = [21, False]
data[3, 0, 3] = [32, False]
data[3, 0, 4] = [48, False]
data[3, 0, 5] = [55, False]
data[3, 0, 6] = [60, False]
data[3, 1, 0] = [1, False]
data[3, 1, 1] = [11, False]
data[3, 1, 2] = [24, False]
data[3, 1, 6] = [65, False]
data[3, 1, 8] = [82, False]
data[3, 2, 1] = [19, False]
data[3, 2, 3] = [35, False]
data[3, 2, 6] = [69, False]
data[3, 2, 7] = [73, False]
data[3, 2, 8] = [83, False]

data[4, 0, 1] = [15, False]
data[4, 0, 3] = [31, False]
data[4, 0, 4] = [40, False]
data[4, 0, 6] = [67, False]
data[4, 0, 8] = [86, False]
data[4, 1, 0] = [9, False]
data[4, 1, 2] = [22, False]
data[4, 1, 4] = [44, False]
data[4, 1, 5] = [55, False]
data[4, 1, 7] = [76, False]
data[4, 2, 1] = [18, False]
data[4, 2, 2] = [23, False]
data[4, 2, 3] = [33, False]
data[4, 2, 7] = [77, False]
data[4, 2, 8] = [89, False]

data[5, 0, 0] = [1, False]
data[5, 0, 3] = [32, False]
data[5, 0, 4] = [40, False]
data[5, 0, 6] = [62, False]
data[5, 0, 8] = [80, False]
data[5, 1, 1] = [10, False]
data[5, 1, 2] = [26, False]
data[5, 1, 4] = [42, False]
data[5, 1, 5] = [57, False]
data[5, 1, 7] = [71, False]
data[5, 2, 0] = [2, False]
data[5, 2, 1] = [14, False]
data[5, 2, 3] = [39, False]
data[5, 2, 7] = [73, False]
data[5, 2, 8] = [82, False]

data[6, 0, 1] = [12, False]
data[6, 0, 3] = [31, False]
data[6, 0, 5] = [55, False]
data[6, 0, 6] = [65, False]
data[6, 0, 8] = [81, False]
data[6, 1, 0] = [2, False]
data[6, 1, 2] = [23, False]
data[6, 1, 4] = [47, False]
data[6, 1, 6] = [67, False]
data[6, 1, 7] = [70, False]
data[6, 2, 1] = [17, False]
data[6, 2, 2] = [24, False]
data[6, 2, 3] = [36, False]
data[6, 2, 7] = [73, False]
data[6, 2, 8] = [88, False]


def checkCorner(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        topLeft = 0
        topRight = 0
        for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if (ticket, 0, col) in data:
                if topLeft == 0:
                    topLeft = data[(ticket, 0, col)]
                topRight = data[(ticket, 0, col)]
        bottomLeft = 0
        bottomRight = 0
        for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if (ticket, 2, col) in data:
                if bottomLeft == 0:
                    bottomLeft = data[(ticket, 2, col)]
                bottomRight = data[(ticket, 2, col)]
        if topLeft[1] == True and topRight[1] == True and bottomLeft[1] == True and bottomRight[1] == True:
            print("******* You win 'Corner' Claim in Ticket# {}".format(ticket))


def checkHouse(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        isThisTicketFullHouse = True
        for row in [0, 1, 2]:
            for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if (ticket, row, col) in data and data[ticket, row, col][1] == False:
                    isThisTicketFullHouse = False
        if isThisTicketFullHouse == True:
            print("******* You win 'FULL HOUSE' Claim in Ticket# {}".format(ticket))


def checkLine(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        for row in [0, 1, 2]:
            isThisRowFull = True
            for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if (ticket, row, col) in data and data[ticket, row, col][1] == False:
                    isThisRowFull = False
            if isThisRowFull == True:
                print(
                    "******* You win '{} LINE' Claim in Ticket# {}".format(row+1, ticket))


def checkHindustan(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        isThisTicketClaimCorrect = True
        for row in [0, 1, 2]:
            for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if (ticket, row, col) in data:
                    if data[ticket, row, col][0] >= 1 and data[ticket, row, col][0] <= 45:
                        if data[ticket, row, col][1] == False:
                            isThisTicketClaimCorrect = False

        if isThisTicketClaimCorrect == True:
            print(
                "******* You win 'HINDUSTAN' Claim in Ticket# {}".format(ticket))


def checkPakistan(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        isThisTicketClaimCorrect = True
        for row in [0, 1, 2]:
            for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if (ticket, row, col) in data:
                    if data[ticket, row, col][0] >= 46 and data[ticket, row, col][0] <= 90:
                        if data[ticket, row, col][1] == False:
                            isThisTicketClaimCorrect = False
        if isThisTicketClaimCorrect == True:
            print(
                "******* You win 'PAKISTAN' Claim in Ticket# {}".format(ticket))


def checkMin1NumberFromEveryColumn(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        isThisClaimTrue = True
        for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            isThisMinColFull = False
            for row in [0, 1, 2]:
                if (ticket, row, col) in data and data[ticket, row, col][1] == True:
                    isThisMinColFull = True
            if isThisMinColFull == False:
                isThisClaimTrue = False
        if isThisClaimTrue == True:
            print(
                "******* You win 'MIN 1 NUMBER FROM EVERY COLUMN' Claim in Ticket# {}".format(ticket))


def check123(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        countOfTrue = {}
        countOfTrue[0] = 0
        countOfTrue[1] = 0
        countOfTrue[2] = 0
        for row in [0, 1, 2]:
            for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                if (ticket, row, col) in data and data[ticket, row, col][1] == True:
                    countOfTrue[row] += 1
        if countOfTrue[0] >= 1 and countOfTrue[1] >= 2 and countOfTrue[2] >= 3:
            print("******* You win '123' Claim in Ticket# {}".format(ticket))


def checkLucky7(data, first7Numbers):
    for ticket in [1, 2, 3, 4, 5, 6]:
        isThisTicketTrue = True
        for number in first7Numbers:
            isThisNumberThere = False
            for row in [0, 1, 2]:
                for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    if (ticket, row, col) in data and data[ticket, row, col][0] == number:
                        isThisNumberThere = True
            if isThisNumberThere == False:
                isThisTicketTrue = False
        if isThisTicketTrue == True:
            print("******* You win 'LUCKY 7' Claim in Ticket# {}".format(ticket))


def checkDiamond(data):
    for ticket in [1, 2, 3, 4, 5, 6]:
        a = 0
        b = 0
        c = 0
        d = 0
        j = 0
        for i in data.keys():
            if i[0] == ticket:
                j += 1
                if j == 3:
                    a = i[2]
                if j == 7:
                    b = i[2]
                if j == 9:
                    c = i[2]
                if j == 13:
                    d = i[2]
        if data[ticket, 0, a][1] == True and data[ticket, 1, b][1] == True and data[ticket, 1, c][1] == True and data[ticket, 2, d][1] == True:
            print("* You win 'Diamond' Claim in Ticket# {}".format(ticket))


while True:
    first7Numbers = []
    tambolaNumber = input("Enter next tambola number : ")
    try:
        tambolaNumber = int(tambolaNumber)
        first7Numbers.append(tambolaNumber)
        for ticket in [1, 2, 3, 4, 5, 6]:
            for row in [0, 1, 2]:
                for col in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    if (ticket, row, col) in data and data[ticket, row, col][1] == False and data[ticket, row, col][0] == tambolaNumber:
                        data[ticket, row, col][1] = True
                        print("Circle Number {} in Ticket# {}, Row# {}, Col# {}".format(
                            tambolaNumber, ticket, row, col))
        if len(first7Numbers) == 7:
            checkLucky7(data, first7Numbers)
        checkCorner(data)
        checkHouse(data)
        checkLine(data)
        checkMin1NumberFromEveryColumn(data)
        checkHindustan(data)
        checkPakistan(data)
        check123(data)
        checkDiamond(data)

    except ValueError:
        continue
