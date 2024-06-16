def main():
    path = "books/frankenstein.txt"
    file_content = get_file_content(path)
    words = file_content.split()
    word_count = len(words)
    print(f"{word_count} words found in document")

def get_file_content(path):
    with open(path) as f:
        return f.read()

main()