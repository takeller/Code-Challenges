import persistence 

def test_persistence():
    assert persistence.persistence(39) == 3
    assert persistence.persistence(4) == 0
    assert persistence.persistence(25) == 2
    assert persistence.persistence(999) == 4
    assert persistence.persistence(-25) == 2
    assert persistence.persistence(25.5) == 'Error: Input must be an integer'
