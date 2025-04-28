def get_book_text(filepath):
    #with can be used to open a file
    #.read() - reads the content of a file into a string
    with open(filepath) as f:
        return f.read()
          
def get_num_words(book_text):
    book_text = get_book_text("books/frankenstein.txt")
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    chars = {}

    for char in book_text:

        char = char.lower()

        if char not in chars:
            chars[char] = 1
        elif char in chars:
            chars[char] += 1
    
    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(num_chars):
    # return a SORTED LIST
    chars_list = []

    for char, count in num_chars.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list