#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    Args:
        min_value (int): The minimum value of the random integer.
        max_value (int): The maximum value of the random integer.
    
    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_operator():
    """
    Generate a random arithmetic operator (+, -, or *).
    
    Returns:
        str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])

def calculate_result(number1, number2, operator):
    """
    Calculate the result of an arithmetic operation.
    
    Args:
        number1 (int): The first operand.
        number2 (int): The second operand.
        operator (str): The arithmetic operator (+, -, or *).
    
    Returns:
        tuple: A tuple containing the arithmetic expression and its result.
    """
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    
    expression = f"{number1} {operator} {number2}"
    return expression, result

def math_quiz():
    score = 0
    total_questions = 3  # Adjust the number of questions as needed

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)
        operator = generate_operator()

        problem, answer = calculate_result(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()


# In[ ]:





# In[ ]:




