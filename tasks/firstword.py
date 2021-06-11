def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    w1=''
    for i in range(len(text)):

        if text[i].isalpha() or ord(text[i]) == 39:
            w1 +=text[i]
            if not text[i+1].isalpha() and not (ord(text[i+1]) == 39):
                break
        if i+1 == (len(text)-1):
            w1 += text[i+1]
            break
    return w1


if __name__ == '__main__':
    print("Example:")
    print(first_word("hi"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
