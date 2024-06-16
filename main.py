def main():
    path = "books/frankenstein.txt"
    file_content = get_file_content(path)
    words = file_content.split()
    word_count = len(words)
    lowercase_string = file_content.lower()
    print(f"{word_count} words found in document")
    print(count_characters(lowercase_string))
    

def get_file_content(path):
    with open(path) as f:
        return f.read()

def count_characters(lowercase_string):
    character_count = {}
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    for letter in ascii_lowercase:
        character_count[letter] = lowercase_string.count(letter)
    return character_count


main()