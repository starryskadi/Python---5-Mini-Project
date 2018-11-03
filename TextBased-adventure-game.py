print("TextBased Adventure Game")
# Rooms 3 room
print("Game Start, Find the treasure")
Room1 = True
a = 2
#Rooms 1
#3x3
# 9 10 11
# 5 6 7
# 1 2 3
moved_tiles = 0

while Room1 == True:
    if a == 1:
        print("There are walls in left and bottom")
        move = input("Where do you want to move?(R,T)(Right,Top)")
        if move == "R":
            a = a + 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 2:
        print("There is walls in bottom")
        move = input("Where do you want to move?(L,R,T)(Left,Right,Top)")
        if move == "L":
            a = a - 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "R":
            a = a + 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 3:
        print("There are walls in bottom and right")
        move = input("Where do you want to move?(L,T)(Left,Top)")
        if move == "L":
            a = a - 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 5:
        print("There is wall in left")
        move = input("Where do you want to move?(R,T,B)(Right,Top,Bottom)")
        if move == "R":
            a = a + 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "B":
            a = a - 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 6:
        print("You are now the center of the room")
        move = input("Where do you want to move?(L,R,T,B)(Left,Right,Top,Bottom)")
        if move == "L":
            a = a - 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "R":
            a = a + 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "B":
            a = a - 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 7:
        print("There is wall in Right")
        move = input("Where do you want to move?(L,T,B)(Left,Top,Bottom)")
        if move == "L":
            a = a - 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "T":
            a = a + 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "B":
            a = a - 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 9:
        print("There are walls in top and left")
        move = input("Where do you want to move?(R,B)(Right,Bottom)")
        if move == "R":
            a = a + 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "B":
            a = a - 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
    if a == 10:
        print("You found the treasure, Congratz")
        Room1 = False
    if a == 11:
        print("There are walls in right and top")
        move = input("Where do you want to move?(L,B)(Left,Bottom)")
        if move == "L":
            a = a - 1
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        if move == "B":
            a = a - 4
            moved_tiles+=1
            print("Moves: " + str(moved_tiles))
        
            
   
    
    # input("There is a door, Do you want to open it? (T)")
    # Room1 = False
    # Room2 = True

# while Room2 == True:
#     move = input("Where do you want to move?(L,R,T,B)(Left,Right,Top,Bottom)")
#     input("There is a door, Do you want to open it? (T)")
#     Room2 = False
#     Room3 = True

# while Room3 == True:
#     move = input("Where do you want to move?(L,R,T,B)(Left,Right,Top,Bottom)")
#     input("There is a door, Do you want to open it? (T)")
#     Room3 = False
# else:
#     print("You found the treasure! ")



#Rooms 2
#4x5

#Rooms 3
#5x1