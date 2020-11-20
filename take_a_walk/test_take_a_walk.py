import take_a_walk 

def test_is_valid_walk():
    assert take_a_walk.is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True
    assert take_a_walk.is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False
    assert take_a_walk.is_valid_walk(['w']) == False
    assert take_a_walk.is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False