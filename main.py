def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        #print(words)
        #print(file_contents)

        def counting_words(x):
            word_count = 0
            for word in x:
                word_count += 1
            return word_count

        print(counting_words(words))




main()