def main():
    path = "books/frankenstein.txt"
    file_content = get_file_content(path)
    words = file_content.split()
    word_count = len(words)
    lowercase_string = file_content.lower()
    ch_results = count_characters(lowercase_string)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in document")
    print()
    print_charater_count_to_console(ch_results)
    print("--- End report ---")

    #print(count_characters(lowercase_string))
    

def get_file_content(path):
    with open(path) as f:
        return f.read()

def count_characters(lowercase_string):
    character_count = {}
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    for letter in ascii_lowercase:
        character_count[letter] = lowercase_string.count(letter)
    return character_count

def print_charater_count_to_console(ch_results):
    ch_sorted = dict(sorted(ch_results.items(), key=lambda x: x[1], reverse=True))
    for ch in ch_sorted:
        print(f"The '{ch}' character was found {ch_sorted[ch]} times")

main()