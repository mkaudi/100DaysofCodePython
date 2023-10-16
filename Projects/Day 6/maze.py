def jump():
    turn_left()
    while right_is_clear() != True:
        move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear() == True: 
        move()
    turn_left()

while is_facing_north() != True:
    turn_left()
    
while at_goal() != True:
    if front_is_clear() == True:
        move()
    elif right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()  