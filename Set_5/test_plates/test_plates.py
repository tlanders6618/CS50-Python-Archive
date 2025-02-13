from plates import is_valid;

def test_num(): #numbers at end only and no starting with 0
    assert is_valid("AAA22A")==False;
    assert is_valid("AAA222")==True;
    assert is_valid("AAA022")==False;

def test_maxmin(): #between 2 and 6 chars inclusive
    assert is_valid("A")==False;
    assert is_valid("ABCDEFGHIJ")==False;

def test_punc(): #no spaces or punctuation
    assert is_valid("AAA..A")==False;
    assert is_valid("AAA PI")==False;

def test_start(): #starts with 2 letters
    assert is_valid("A23456")==False;
    assert is_valid("AA2345")==True;
