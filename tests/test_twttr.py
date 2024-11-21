import sys
sys.path.append("..")
from twttr import shorten

def main():
    test_mutiple_words()
    test_no_vowels()
    test_one_word()


def test_one_word():
    assert shorten("Twitter") == "Twttr"

def test_mutiple_words():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_no_vowels():
    assert shorten("CS50") == "CS50"

if __name__ == "__main__":
    main()