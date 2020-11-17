def career_fair(arrival, duration):
    # arrival_dict = {}
    # for arrival_time_tuple in enumerate(arrival): 
    #     arrival_time_index = arrival_time_tuple[0]
    #     arrival_time = arrival_time_tuple[1]

    #     if str(arrival_time) in arrival_dict:
    #         arrival_dict[str(arrival_time)].append(duration[arrival_time_index]) 
    #     else: 
    #         arrival_dict[str(arrival_time)] = [duration[arrival_time_index]]

    arrival_dict = _build_dict(arrival, duration)
    previous_end_time = 0
    presentation_count = 0
    previous_arrival_time = 0
    for arrival_time in sorted(arrival):
        end_time = arrival_time + min(arrival_dict[str(arrival_time)])

        if arrival_time == previous_arrival_time: 
            continue 
        elif end_time < previous_end_time: 
            presentation_count -=1
        elif arrival_time < previous_end_time:
            continue
        
        presentation_count += 1
        previous_end_time = end_time
        previous_arrival_time = arrival_time
        
    return presentation_count

def _build_dict(arrival, duration): 
    arrival_dict = {}
    for arrival_time_tuple in enumerate(arrival): 
        arrival_time_index = arrival_time_tuple[0]
        arrival_time = arrival_time_tuple[1]

        if str(arrival_time) in arrival_dict:
            arrival_dict[str(arrival_time)].append(duration[arrival_time_index]) 
        else: 
            arrival_dict[str(arrival_time)] = [duration[arrival_time_index]]

    return arrival_dict