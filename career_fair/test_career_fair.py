import career_fair

def test_career_fair():
    arrival1 = [1, 3, 5]
    duration1 = [2, 2, 2]
    max_events1 = 3
    arrival2 = [1, 3, 3, 5, 7]
    duration2 = [2, 2, 1, 2, 1]
    max_events2 = 4
    arrival3 = [1, 1, 1, 1, 4]
    duration3 = [10, 3, 6, 4, 2]
    max_events3 = 2
    arrival4 = [948, 386, 218, 273, 540, 248, 386, 497, 886, 624, 421, 145, 969, 736, 916, 626, 535, 43, 12, 680, 153, 245, 296]
    duration4 = [819, 397, 693, 816, 992, 34, 670, 398, 554, 548, 826, 211, 663, 212, 809, 378, 762, 626, 336, 869, 996, 777, 768]
    max_events4 = 3
    arrival5 = [978, 409, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426, 670, 116, 95, 630]
    duration5 = [502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145]
    max_events5 = 4
    assert career_fair.career_fair(arrival1, duration1) == max_events1
    assert career_fair.career_fair(arrival2, duration2) == max_events2
    assert career_fair.career_fair(arrival3, duration3) == max_events3
    assert career_fair.career_fair(arrival4, duration4) == max_events4
    assert career_fair.career_fair(arrival5, duration5) == max_events5