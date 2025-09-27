from project.revision.hw_functions_utils import *

def main():
    result = is_number_bigger_than_given(candidate_number = 5)
    print(result)
    result = is_number_bigger_than_given(candidate_number = 5, threshold = 1)
    print(result)

    given_list = []
    add_salt_to_list([])
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    print(given_list)
    print(say_hello_buddy())
    ar_1 = [1,2,3,4,5]
    print(return_biggest_number_from_array(ar_1))
    n_1 = 4
    n_2 = 6
    print(multiply_two_numbers(n_1,n_2))

if __name__ == '__main__':
    main()