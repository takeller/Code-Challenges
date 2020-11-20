def is_valid_walk(walk, walk_time = 10):
    if len(walk) != walk_time: 
        return False 
    # x and y coordinates
    x = 0 
    y = 0 

    for direction in walk: 
        if direction == 'n': 
            y += 1
        elif direction == 'e':
            x += 1
        elif direction == 's':
            y -= 1
        elif direction == 'w':
            x -= 1

    return x == 0 and y == 0 