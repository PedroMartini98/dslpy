import sys
sys.path.append('..')
from vanity import is_valid

def main():
    test_cs50()
    test_cs05()
    test_cs50P()
    test_pi()
    test_h()
    test_outtime()
def test_cs50():
    assert is_valid('CS50') == True
def test_cs05():
    assert is_valid('CS05') == False
def test_cs50P():
    assert is_valid('CS05') == False
def test_pi():
    assert is_valid('PI3.14') == False
def test_h():
    assert is_valid('h') == False
def test_outtime():
    assert is_valid('OUTATIME') == False



if __name__ == "__main__":
    main()