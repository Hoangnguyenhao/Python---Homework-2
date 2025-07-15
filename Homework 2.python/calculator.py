def calculate(a: float, b: float, op: str):
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return 'Error: Division by zero' if b == 0 else a / b
        case _:
            return 'Invalid operation'

def main():
    try:
        x = float(input("Enter first number: ").strip())
        y = float(input("Enter second number: ").strip())
        op = input("Enter operation (+ - * /): ").strip()
        result = calculate(x, y, op)
        print(f"Result: {result}")
    except Exception:
        print("Invalid input.")

if __name__ == '__main__':
    main()
