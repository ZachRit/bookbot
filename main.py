def get_contents(book):
    with open(book) as f:
        return f.read()

def word_count(book):
    return len(book.split())

def char_count(book):
    char_list = {}
    words = book.lower()
    for char in words:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1 
    return char_list

def sort_char(chars):
    char_list = []
    for element in chars:
        if element.isalpha():
            char_list.append({"char": element, "count": chars[element]})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_contents(book_path)
    words = word_count(text)  
    char_dict = char_count(text)
    char_sorted = sort_char(char_dict)
    print(f"{words} words found in the document")
    print(char_dict)
    for chars in char_sorted:
        print(f"The {chars['char']} character was found {chars['count']} times")
main()


