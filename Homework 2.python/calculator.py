def calculate(a: float, b: float, operator: str) -> float:
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        case _:
            raise ValueError(f"Invalid operator: {operator}")

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()

        result = calculate(a, b, operator)
        print(f"Result: {a} {operator} {b} = {result:.2f}")

    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)

if __name__ == "__main__":
    main()
