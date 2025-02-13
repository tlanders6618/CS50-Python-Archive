from bank import value;

def test_hello(): #hello in input, case insensitive
    assert value("hElLo there.")==0;
    assert value("Hellow.")==0;
    assert value("  Hellow.  ")==0;

def test_h(): #anything (other than hello) starting with h means $20
    assert value("heck no")==20;
    assert value("hello")!=20;

def test_100(): #doesn't start with h or have hello means 100
    assert value ("hello")!=100;
    assert value("howdy.")!=100;
    assert value("yo")==100;
