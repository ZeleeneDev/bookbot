def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    total_number_of_words = number_of_words(file_content)

def number_of_words(string_of_words):
    word_count = 0
    words = string_of_words.split()
    for word in words:
        word_count += 1
    print(word_count)



main()