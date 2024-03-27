import operation as op 

def test_add():
    assert op.add(4,5) == 9

def test_subtract():
    assert op.subtract(25,8) == 17

def test_multiply():
    assert op.multiply(4,5) == 20

def test_divide():
    assert op.divide(10,5) == 2    

def test_get_squared():
    assert op.get_squared(9) == 81