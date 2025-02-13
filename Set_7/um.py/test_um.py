from um import count;

def test_substring(): #um not counted if it's part of a word
    assert count("Yummy, scummy chum in my tummy tum.")==0; #works
    assert count("umumumumumumumumum")==0; #works

def test_caps(): #must be case and space insensitive
    assert count("UM. Welcome to the um bowl, where we serve only the UMmest Um in the uM.")==4;
    assert count(" UM ")==1; #works

def test_punctpunctpunctpunctuation(): #must ignore punctuation, or else
    assert count("U.M.")==0; #works
    assert count("Um, what, um, day, um, like, um, is it, man, um, yeah? Um. Um")==7;
    assert count("Um? Um, um...um. Um! <Um<; asnjakkkqp 'um'")==7;
