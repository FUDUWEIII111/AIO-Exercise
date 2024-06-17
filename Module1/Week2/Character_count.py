def count_char(letter):
    list_of_char = letter
    char_count = {}
    for char in list_of_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def check_letter(letter):
    if letter.isalpha():
        return letter
    else:
        return "Please enter a valid string"

def main():
    letter = input("Enter a string: ")
    letter = check_letter(letter)
    number_of_char = count_char(letter)
    print(number_of_char)

if __name__ == "__main__":
    main()
