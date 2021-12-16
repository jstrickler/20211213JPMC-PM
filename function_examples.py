import math

def get_message():
    return "Hello, JPMC world"

m = get_message()
print(get_message())

def show_message():
    message = get_message()
    print(message)

show_message()

def circle_area(diameter):
    radius = diameter / 2
    return math.pi * (radius **2)

def rectangle_area(length, width):
    return length * width

print(circle_area(42))
print(rectangle_area(55, 119))

def count_lines(search_term, *file_paths):
    total_count = 0
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    total_count += 1
    return total_count

print("total birds:", count_lines('bird', 'DATA/alice.txt', 'DATA/parrot.txt'))
print("total pigs:", count_lines('pig', 'DATA/alice.txt', 'DATA/words.txt', 'DATA/parrot.txt'))





