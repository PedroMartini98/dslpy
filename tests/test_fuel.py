import sys
sys.path.append('..')
from fuel import convert,gauge

def main():
    test_correct()
    test_rest()


def test_correct():
    assert convert('1/4') == 25
    print(gauge(25))
    assert gauge(25) == '25%'
def test_rest():
    assert convert('99/100') == 99 
    assert gauge(99) == 'F'
    assert convert('100/100') == 100 
    assert gauge(100) == 'F'
    assert convert('1/100') == 1  
    assert gauge(1) == 'E'
    assert convert('0/100') == 0  
    assert gauge(0) == 'E'




if __name__ == "__main__":
    main()