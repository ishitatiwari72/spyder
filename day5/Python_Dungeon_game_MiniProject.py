# Dungeon Game/
"""
Challenge 1
    It would be a 2 dimensional maze game 
    We would put the player in a random room in the grid 
    We would also put a monster in a random room in the grid 
    We would out a door in a random room in the grid 
    The player would then move around the grid to find the door 
    Don’t let he player go out of the edges of the grid 
    If they hit the monster room they are eaten by the monster  
    or if they reach the gate they win 
    Grid of Room = Collection of Coordinates 
    Player is a tuple, it contains two values  3
    
""" 


""" 
Challenge 2 
Welcome message is getting printed every-time 
Can we display the grid for the visual 
""" 

import random
grid=[[1,2,3],[4,5,6],[7,8,9]]
play_r = random.randint(0,2)
play_c = random.randint(0,2)
mon_r = random.randint(0,2)
mon_c = random.randint(0,2)
door_r = random.randint(0,2)
door_c = random.randint(0,2)
print("player >>",grid[play_r][play_c])
print("monster baba >>",grid[mon_r][mon_c])
print("khul ja sim sim >>",grid[door_r][door_c])
while grid[play_r][play_c] in range(0,2) and grid[play_r][play_c] != grid[mon_r][mon_c] and grid[play_r][play_c] != grid[door_r][door_c] :
    print("press 1 to move up\npress 2 to move down\nprress 3 to move right\npress 4 to move left")
    i=int(input("enter your choice"))
    
    if i==1:
        play_r = play_r - 1
        
        if grid[play_r][play_c] == grid[mon_r][mon_c] :
            print("abe tu mar gya bhaiiii")
            break
        elif grid[play_r][play_c] == grid[door_r][door_c]:
            print("bhai bhai jeeet gye apn toh")
            break
        else:
            continue

    elif i==2:
        play_r = play_r + 1
        if grid[play_r][play_c] == grid[mon_r][mon_c] :
            print("abe tu mar gya bhaiiii")
            break
        elif grid[play_r][play_c] == grid[door_r][door_c]:
            print("bhai bhai jeeet gye apn toh")
            break
        else:
            continue

    elif i==3:
        play_c = play_c + 1
        if grid[play_r][play_c] == grid[mon_r][mon_c] :
             print("abe tu mar gya bhaiiii")
             break
        elif grid[play_r][play_c] == grid[door_r][door_c]:
            print("bhai bhai jeeet gye apn toh")
            break
        else:
            continue

    elif i==4:
        play_c = play_c - 1 
        if grid[play_r][play_c] == grid[mon_r][mon_c] :
            print("abe tu mar gya bhaiiii")
            break
        elif grid[play_r][play_c] == grid[door_r][door_c]:
            print("bhai bhai jeeet gye apn toh")
            break
        else:
            continue
        

   


   
            
        