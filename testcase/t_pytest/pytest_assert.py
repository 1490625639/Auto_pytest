# �ж�xxΪ��
import pytest


# �ж�xxΪ��
def test_1():
    a = True
    assert a


# �ж�xx��Ϊ��
def test_2():
    a = True
    assert not a
# �ж�b����a
def test_3():
    a="hello"
    b="hello_world"
    assert a in b
# �ж����
def test_4():
    a="hello"
    b="hello"
    assert a==b
# �жϲ���
def test_4():
    a="hello"
    b="hello1"
    assert a!=b
if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])
