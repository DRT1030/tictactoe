import nltk
nltk.download()
from nltk.tokenize import word_tokenize
from sympy import symbols, Eq, solve
import re

class MathAI:
    def __init__(self):
        self.variables = {}

    def explain(self, expression):
        # Tokenize the input expression
        tokens = word_tokenize(expression)

        # Identify the operation (e.g., +, -, *, /)
        operation = None
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operation = token
                break

        # Extract the operands (e.g., numbers or variables)
        operands = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                operands.append(token)

        # Parse the operands (e.g., convert to integers or variables)
        parsed_operands = []
        for operand in operands:
            if operand.isdigit():
                parsed_operands.append(int(operand))
            else:
                if operand not in self.variables:
                    self.variables[operand] = symbols(operand)
                parsed_operands.append(self.variables[operand])

        # Perform the operation
        result = None
        if operation == '+':
            result = parsed_operands[0] + parsed_operands[1]
        elif operation == '-':
            result = parsed_operands[0] - parsed_operands[1]
        elif operation == '*':
            # Handle multiplication with multiple factors
            factors = []
            for operand in parsed_operands:
                if isinstance(operand, int):
                    factors.append(operand)
                else:
                    factors.append(operand)
            result = 1
            for factor in factors:
                result *= factor
        elif operation == '/':
            # Handle division with multiple divisors
            dividend = parsed_operands[0]
            divisors = []
            for operand in parsed_operands[1:]:
                if isinstance(operand, int):
                    divisors.append(operand)
                else:
                    divisors.append(operand)
            result = dividend
            for divisor in divisors:
                result /= divisor

        # Generate the step-by-step explanation
        explanation = []
        explanation.append(f"{operands[0]} {operation} {operands[1]} = ?")
        if operation == '*':
            explanation.append(f" Multiply {', '.join(map(str, factors))} together:")
            for i, factor in enumerate(factors):
                explanation.append(f"  {factor} {'*' if i < len(factors) - 1 else '='} {result}")
        elif operation == '/':
            explanation.append(f" Divide {dividend} by {', '.join(map(str, divisors))}:")
            for i, divisor in enumerate(divisors):
                explanation.append(f"  {dividend} {'/' if i < len(divisors) - 1 else '='} {divisor} = {result}")
        else:
            explanation.append(f"{parsed_operands[0]} {operation} {parsed_operands[1]} = {result}")
        explanation.append(f"Therefore, {operands[0]} {operation} {operands[1]} = {result}")

        return explanation

# Test the MathAI class
ai = MathAI()
expression = "2 * 3 * 4"
explanation = ai.explain(expression)
print("\n".join(explanation))

expression = "12 / 3 / 2"
explanation = ai.explain(expression)
print("\n".join(explanation))
