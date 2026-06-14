# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    (item_to_return for item_in_iterable in iterable if condition)

# more concrete example:
numbers_list = [1, 2, 3, 4, 5, 6]
generator_expression = (n * 2 for n in numbers_list if number > 3)

# Using generator
print(next(generator_expression))  # Output: 8
print(next(generator_expression))  # Output: 10
    """
    return (student for student in student_list if student[2].lower() == major.lower())
    pass
