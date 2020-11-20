import greed_is_good

def test_score():
    assert greed_is_good.score([2, 3, 4, 6, 2]) == 0
    assert greed_is_good.score([4, 4, 4, 3, 3]) == 400
    assert greed_is_good.score([2, 4, 4, 5, 4]) == 450
    assert greed_is_good.score([1, 1, 1, 1, 1]) == 1200
    assert greed_is_good.score([3, 2, 6, 5, 6, 6]) == 650