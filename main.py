def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    total_number_of_words = number_of_words(file_content)
    total_number_of_letters = number_of_letters(file_content)
    sorted_total_number_of_letters = sort_dict(total_number_of_letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_number_of_words} words found in the document")
    print(" ")
    for key in sorted_total_number_of_letters:
        value = sorted_total_number_of_letters[key]
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def number_of_words(string_of_words):
    word_count = 0
    words = string_of_words.split()
    for word in words:
        word_count += 1
    return word_count

def number_of_letters(string_of_words):
    letter_count_dict = {}
    lower_string_of_words = string_of_words.lower()
    #words = lower_string_of_words.split()
    for word in lower_string_of_words:
        for letter in word:
            if letter.isalpha():
                if letter in letter_count_dict:
                    letter_count_dict[letter] += 1
                else:
                    letter_count_dict[letter] = 1
    return letter_count_dict

def sort_dict(dict):
    sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

main()