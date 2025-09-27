from uuid import uuid4

def is_number_bigger_than_given(candidate_number:float, threshold:float = 10) -> bool:
    return candidate_number > threshold

def add_salt_to_list(given_list: list) -> None:
    identifier = uuid4().hex
    print(uuid4())
    given_list.append(identifier)

def say_hello_buddy():
    return 'Hello, Buddy'

def return_biggest_number_from_array(ar, elem = 1):
    biggest_number = ar[0]
    if elem > biggest_number:
        biggest_number = elem
    return biggest_number

ar_1 = [1,2,3,4,5]
a = return_biggest_number_from_array(ar_1)
print(a)
def multiply_two_numbers(n_1,n_2):
    return n_1*n_2

b = multiply_two_numbers(n_1 = 3, n_2 = 5)
print(b)