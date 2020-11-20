def score(dice):
    # Convert list to dict with counts
    count_dict = {}
    for roll in dice:
        if roll in count_dict:
            count_dict[roll] += 1
        else: 
            count_dict[roll] = 1

    # Map dict to scoring 
    score = 0
    for roll_value, count in count_dict.items(): 
        if count < 3: 
            score += count * score_singles(roll_value)
        elif count == 3: 
            score += score_trips(roll_value)
        elif count >= 3 and count < 6: 
            score += score_trips(roll_value) + (count - 3) * score_singles(roll_value)
        elif count == 6: 
            score += 2 * score_trips(roll_value)
    return score 

def score_trips(roll_value):
    if roll_value == 1: 
        return 1000
    else: 
        return roll_value * 100

def score_singles(roll_value):
    if roll_value == 1: 
        return 100
    elif roll_value == 5:
        return 50 
    else: 
        return 0
