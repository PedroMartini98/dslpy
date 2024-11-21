def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    new_word=""
    for char in word:
        if char not in ["A","a","E","e","I","i","O","o","U","u"]:
            new_word += char
    return new_word


if __name__ == "__main__":
    main()