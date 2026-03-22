def add(a,b):
    return a+b

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(1,1) == 5  # This will FAIL (should be 2, not 5)

    print("All tests passed!")

test_add()