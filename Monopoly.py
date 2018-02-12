from random import randint
from random import shuffle


def traverseBoard(targets,starting_position,board):
    x=starting_position
    while True:
        if x>39:
            x=0
        if ' '.join(board[x].split()[:-1]) in targets:
            return x
        x+=1

board=None
positionList=None

def rankPlaces(positionList,board):
    print("Compiling data from "+str(len(positionList)-1)+" visits..")
    visiting_tracker={}
    for x in range(40):
        visiting_tracker[positionList.count(x)]=x
    temp_list=sorted(visiting_tracker)
    temp_list.reverse()
    x=1
    for thing in temp_list:
        print(str(x)+": "+str(board[visiting_tracker[thing]])+" was visited "+str(positionList.count(visiting_tracker[thing]))+" times. That's "+str(round((positionList.count(visiting_tracker[thing])/len(positionList)*100),2))+"% of the time")
        x+=1
    
        
board=["Go (0)",
       "Mediterranean Avenue (1)",
       "Community Chest (2)",
       "Baltic Avenue (3)",
       "Income Tax (4)",
       "Reading Railroad (5)",
       "Oriental Avenue (6)",
       "Chance (7)",
       "Vermont Avenue (8)",
       "Connecticut Avenue (9)",
       "Jail (10)",
       "St. Charles Palace (11)",
       "Electric Company (12)",
       "States Avenue (13)",
       "Virginia Avenue (14)",
       "Pennsylvania Railroad (15)",
       "St. James Palace (16)",
       "Community Chest (17)",
       "Tennessee Avenue (18)",
       "New York Avenue (19)",
       "Free Parking (20)",
       "Kentucky Avenue (21)",
       "Chance (22)",
       "Indiana Avenue (23)",
       "Illinois Avenue (24)",
       "B. & O. Railroad Avenue (25)",
       "Atlantic Avenue (26)",
       "Ventnor Avenue (27)",
       "Water Works (28)",
       "Marvin Gardens (29)",
       "Go To Jail (30)",
       "Pacific Avenue (31)",
       "North Carolina Avenue (32)",
       "Community Chest (33)",
       "Pennsylvania Avenue (34)",
       "Short Line (35)",
       "Chance (36)",
       "Park Place (37)",
       "Luxury Tax (38)",
       "Boardwalk (39)",
       ]

chance_cards=["GOTO Go","GOTO Illinois Avenue","GOTO St. Charles Palace","FIND NearestUtility","FIND NearestRailRoad","FIND NearestRailRoad","-GET 50","JailFreeCard","WALK -3","GOTO Jail","-make Repairs","-pay 15","GOTO Reading Railroad","GOTO Boardwalk","-Pay 50 to each player","-GET 150"]
community_cards=["GOTO Go","-GET 200","-GET -50","-GET 150","JailFreeCard","GOTO Jail","-Get paid 50 from each player","-GET 100","-GET 20","-GET 100","-GET -100","-GET -150","-GET 25","-PAY 40 FOR EACH HOUSE AND 115 PER HOTEL","-GET 10","-GET 100"]
utilities=["Electric Company","Water Works"]
railroads=["Reading Railroad","Pennsylvania Railroad","B. & O. Railroad","Short Line"]
shuffle(chance_cards)
shuffle(community_cards)

#limit1=input("Number of times you want to pass 'GO'")
passed_go=0
position=0


dieRollList=[]
positionList=[]

while True:
    try:
        z=int(input("Number of dice rolls: "))
        break
    except:
        pass
w=0
try:
    while z>=w:
        w+=1
        #print()
        previousPosition=position
        print(previousPosition)
        dieRoll=randint(1,6)+randint(1,6)
        dieRollList.append(dieRoll) #keeps track of die rolls
        position=position+dieRoll #updates the position
        if position>39:
            position=position-40
        currentSquare=board[position]
        '''
        print("Currently on: "+currentSquare)
        print("Just rolled a: "+str(dieRoll))
        print("Therefore I am on position "+str(position))
        '''
        if ' '.join(currentSquare.split()[0:-1])=="Chance" or ' '.join(currentSquare.split()[0:-1])=="Community Chest":
            breakCondition=False
            while breakCondition==False:
                breakCondition=True
                if ' '.join(currentSquare.split()[0:-1])=="Community Chest":
                    #print("Reading a community chest card..")
                    card=community_cards[0]
                    #print("Card: "+str(card))
                    community_cards.pop(0)
                    community_cards.append(card)
                else:
                    #print("Reading a chance card..")
                    card=chance_cards[0]
                    #print("Card: "+str(card))
                    chance_cards.pop(0)
                    chance_cards.append(card)        
                if card[0]!="-":
                    if card.split()[0]=="GOTO":
                        goToSquare=card.split()[1:]
                        position=traverseBoard([' '.join(goToSquare)],position,board)
                    elif card.split()[0]=="FIND":
                        if "Utility" in card:
                            position=traverseBoard(utilities,position,board)
                        elif "RailRoad" in card:
                            position=traverseBoard(railroads,position,board)
                    elif card.split()[0]=="WALK":
                        position=position+int(card.split()[-1])
                        if ' '.join(board[position].split()[0:-1])=="Community Chest" or ' '.join(board[position].split()[0:-1])=="Chance":
                            breakCondition=False
                currentSquare=board[position]
                #print("Moved to "+board[position])

        elif ' '.join(currentSquare.split()[0:-1])=="Go To Jail":
            position=traverseBoard(["Jail"],position,board)
        positionList.append(position)
except:
    rankPlaces(positionList,board)
rankPlaces(positionList,board)
    
