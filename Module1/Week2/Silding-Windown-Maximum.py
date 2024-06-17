def maximum_sliding_window(array, window_size):
    if len(array) == 0:
        return []
    if window_size > len(array):
        return []

    max_array = []
    for i in range(len(array) - window_size + 1):
        max_value = max(array[i:i+window_size])
        max_array.append(max_value)
    return max_array

def check_window_size(window_size):
    if window_size.isdigit():
        return int(window_size)
    else:
        return "Please enter a valid number"

def check_num_list(input_string):
    num_list_str = input_string.split()
    num_list = []
    for number in num_list_str:
        try:
            num = int(number)
            num_list.append(num)
        except ValueError:
            return "Please enter a valid list of numbers"
    return num_list
    

def main():
    window_size = input("Enter the window size: ")
    window_size = check_window_size(window_size)
    num_list = input("Enter the list of numbers: ")
    num_list = check_num_list(num_list)
    
    print(maximum_sliding_window(num_list, window_size))


if __name__ == "__main__":
    main()
