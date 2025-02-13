from jar import Jar;
import pytest;

def getjar(size=616): #jars have default capacity of 12
    if (size==616):
        jarjar=Jar();
    else:
        jarjar=Jar(size);
    return jarjar;

def test_capacity():
    uno=getjar();
    assert uno.capacity==12;
    trix=getjar(300);
    assert trix.capacity==300;
    five=getjar(0);
    assert five.capacity==0;
    assert five.size==trix.size and trix.size==uno.size and uno.size==0;
    with pytest.raises(ValueError):
        ivy=getjar(-1);

def test_deposit():
    dos=getjar();
    with pytest.raises(ValueError):
        dos.deposit(600); dos.deposit(13);
    dos.deposit(9);
    assert dos.size==9;
    dos.deposit(3);
    assert dos.size==12;
    with pytest.raises(ValueError):
        dos.deposit(1);

def test_withdraw():
    ocho=getjar();
    with pytest.raises(ValueError):
        ocho.withdraw(99); ocho.withdraw(1);
    ocho.deposit(8); ocho.withdraw(7);
    assert ocho.size==1;
    ocho.withdraw(1);
    assert ocho.size==0;

def test_string():
    vi=getjar();
    assert str(vi)=="";
    vii=getjar();
    vii.deposit(5);
    assert str(vii)=="🍪🍪🍪🍪🍪";
    vii.withdraw(3);
    assert str(vii)=="🍪🍪";



