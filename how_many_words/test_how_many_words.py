import how_many_words


def test_how_many_words(): 
    sentence1 = "Hello World! ? 54 94"
    sentence1_word_count = 2 
    sentence2 = "Hello My name 456 Is Taylor AND i am a back-end engineer. 57 83"
    sentence2_word_count = 11
    sentence3 = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"
    sentence3_word_count = 21
    assert how_many_words.how_many(sentence1) == sentence1_word_count
    assert how_many_words.how_many(sentence2) == sentence2_word_count
    assert how_many_words.how_many(sentence3) == sentence3_word_count