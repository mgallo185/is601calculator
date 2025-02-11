# Homework 3 by Michael Gallo

# Setting up  Calculator with basic functions and history
# 
calculator/ contains 3 files. 
1. __init__.py runs the repl.
2. calculate.py is the class Calculation which containts objects of calculations and keeps the history of all calculations
3. operations.py is the class Operation which contains static methods of each type of operation, i.e., addition, subtraction, etc.

test/ contains 3 files
1. test_repl.py: tests tests cases of the repl and inputs situations
2. test_calculation.py: tests the calculation class history
3. test_operation.py: tests operations class


# Setting up the program
1. Open Ubuntu and cd into directory where homework3 is
2. code . to open vs code in that directory
3. create (if you havent ) and activate virtual enviroment: source venv/bin/activate
4. pip install -r requirements.txt
5. python main.py to run the code
6. pytest --pylint --cov to run the tests
