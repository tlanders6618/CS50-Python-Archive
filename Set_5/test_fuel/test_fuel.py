from fuel import convert;
from fuel import gauge;
import pytest;

def test_convert():
    with pytest.raises(ValueError):
        convert("c/a");
    with pytest.raises(ZeroDivisionError):
        convert("9/0");
    with pytest.raises(ValueError):
        convert("3/1");
    assert convert("50/100")==50;

def test_gauge():
    assert gauge(1)=="E";
    assert gauge(99)=="F";
    assert gauge(80)=="80%";
