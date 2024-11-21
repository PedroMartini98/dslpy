import sys
sys.path.append("..")
from bank import greeting

def main():
    test_hello()
    test_h()
    test_wrong()

def test_hello():
    assert greeting("hello") == ("$0")
    assert greeting("hello, david") == ("$0")
    
def test_h():
    assert greeting("how are you") == ("$20")
def test_wrong():
    assert greeting("cat") == ("$100")

if __name__ == "__main__":
    main()