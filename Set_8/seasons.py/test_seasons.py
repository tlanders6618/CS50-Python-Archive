from seasons import validdate, convert;
import pytest;

def test():
    with pytest.raises(SystemExit):
        validdate("2022-13-02"); #13th month
        validdate("2023-09-32"); #32nd of Sept
        validdate("2024-01-00"); #0th of Jan
        validdate("2000-02-31"); #Feb 31st
        convert("2022-13-02");
        convert("2023-09-32");
    #minutes from given date to today's date
    assert convert("2024-07-31")=="zero"; #same as today's date
    assert convert("2024-08-01")=="one thousand, four hundred forty"; #24 hours
