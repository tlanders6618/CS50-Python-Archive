from numb3rs import validate;

def test_digits(): #must have 4 numbers
    assert validate("2.3.3.3.3")==False;
    assert validate("2.3.3")==False;
    assert validate("2.3")==False;
    assert validate("2")==False;
    assert validate("123.45.6.78")==True;
    assert validate("2,3,3,78")==False; #must use periods

def test_range(): #must be 0-255
    assert validate("127.0.0.1")==True;
    assert validate("3.256.65.90")==False;
    assert validate("-1.255.255.255")==False; #no negatives
    assert validate("54.t.car.32")==False; #no words
