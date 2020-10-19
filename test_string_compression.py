import string_compression


def test_compression(): 
    assert string_compression.compress('aabcccccaaa') == 'a2b1c5a3'
    assert string_compression.compress('zzbbbjddddd') == 'z2b3j1d5'
    assert string_compression.compress('KKkkZllllllJJJ') == 'K2k2Z1l6J3'

    assert string_compression.compress('') == ''
    assert string_compression.compress('aabbcdkaalll') == 'aabbcdkaalll'
    assert string_compression.compress('BBccKKIIjj') == 'BBccKKIIjj'
