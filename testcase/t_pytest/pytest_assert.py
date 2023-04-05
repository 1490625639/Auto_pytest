# 判断xx为真
import pytest


# 判断xx为真
def test_1():
    a = True
    assert a


# 判断xx不为真
def test_2():
    a = True
    assert not a
# 判断b包含a
def test_3():
    a="hello"
    b="hello_world"
    assert a in b
# 判断相等
def test_4():
    a="hello"
    b="hello"
    assert a==b
# 判断不等
def test_4():
    a="hello"
    b="hello1"
    assert a!=b
if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])
