from main import *

def test_star_first_and_last():
    assert star_first_and_last("buffalo") == "*uffal*"

def test_initials():
    assert initials("Tracy", "Turtle") == "T.T."
    assert initials("Peter", "Parker") == "P.P."

def test_sandwich():
    assert sandwich("horse") == "hre"
    assert sandwich("slate") == "sae"

def test_end_of_word():
    assert end_of_word("boat") == "oat"
    assert end_of_word("mice") == "ice"
    assert end_of_word("elephant") == "lephant"

def test_replace_at_index():
    assert replace_at_index("eggplant", 3) == "egg-lant"
    assert replace_at_index("strange", 0) == "-trange"
    assert replace_at_index("ojo",1) == "o-o"