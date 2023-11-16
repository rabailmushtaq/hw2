#!/usr/bin/env python
# coding: utf-8

# In[8]:


import unittest
from math_quiz import generate_random_integer, generate_operator, calculate_result

class TestMathQuizFunctions(unittest.TestCase):
    def test_generate_random_integer(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        operators = ['+', '-', '*']
        for _ in range(1000):
            operator = generate_operator()
            self.assertIn(operator, operators)

    def test_calculate_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_result(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == '__main__':
    unittest.main()


# In[ ]:





# In[ ]:




