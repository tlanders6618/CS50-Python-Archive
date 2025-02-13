from twttr import shorten;

def test_shorten(): #remove all vowels, case insensitive; ignore punctuation and numbers
    assert shorten("LOKi1")=="LK1";
    assert shorten("love yourself")=="lv yrslf"; #y is not a vowel apparently
    assert shorten("assert?")=="ssrt?";

