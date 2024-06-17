def count_word(path):
    with open(path, 'r') as file:
        data = file.read()
        list_of_word = data.split()
        list_of_word = [word.lower() for word in list_of_word]
        word_count = {}
        for word in list_of_word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

def main():
    path = "D:/AIO/AIO-Exercise/Module1/Week2/P1_data.txt"
    number_of_word = count_word(path)
    print(number_of_word)

if __name__ == "__main__":
    main()
    