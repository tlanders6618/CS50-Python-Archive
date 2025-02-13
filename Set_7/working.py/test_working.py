import pytest;
from working import convert;

def test_format():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00");
        convert("9:00AM to 5:00PM");
        convert("9:00 AM 5:00 PM");
        convert("9 AM to 5:62 PM");
        convert("13:00 AM to 5:59 AM");
        convert("25:59 AM to 46:71 AM");
    with pytest.raises(ValueError):
        #separate so check50 stops giving me a :( even though the above tests already account for it
        convert("9:60 AM to 5:60 PM");

def test_convert():
    assert convert("10:00 AM to 1:30 PM")=="10:00 to 13:30";
    assert convert("3:00 AM to 4:01 AM")=="03:00 to 04:01";
    assert convert("11 AM to 11 PM")=="11:00 to 23:00";
    assert convert("12:31 AM to 12:34 PM")=="00:31 to 12:34"; #convert 12am but not 12pm

def test_third():
    with pytest.raises(ValueError):
        convert("Just doing my job.");
