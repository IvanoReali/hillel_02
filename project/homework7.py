from typing import List

def greet_person(name: str = "Guest") -> str:
    return f"Hello, {name}"

def is_even(number: int) -> bool:
    return number % 2 == 0

def reverse_string(text: str) -> str:
    return text[::-1]

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0.0

def add_person_to_list(people: List[str], person: str) -> List[str]:
    return people + [person]

def count_vowels(text: str) -> int:
    vowels = "а е є и і ї о у ю я a e i o u y"
    return sum(1 for ch in text.lower() if ch in vowels)

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9