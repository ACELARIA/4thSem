def add(a, b):
    """Addition function"""
    return a + b

def subtract(a, b):
    """Subtraction function"""
    return a - b

def multiply(a, b):
    """Multiplication function"""
    return a * b

def divide(a, b):
    """Division function with zero division check"""
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def show_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("🧮 SIMPLE CALCULATOR")
    print("="*40)
    print("1. ➕ Addition")
    print("2. ➖ Subtraction") 
    print("3. ✖️  Multiplication")
    print("4. ➗ Division")
    print("5. 🔄 Quick calculation")
    print("6. 📊 Calculator history")
    print("7. ❌ Exit")
    print("-" * 40)

def get_operation_choice():
    """Get valid operation choice from user"""
    while True:
        try:
            choice = int(input("Choose operation (1-7): "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("❌ Please choose a number between 1-7")
        except ValueError:
            print("❌ Please enter a valid number!")

def perform_calculation(operation, a, b):
    """Perform calculation and return result with operation string"""
    operations = {
        1: (add, "+"),
        2: (subtract, "-"),
        3: (multiply, "×"),
        4: (divide, "÷")
    }
    
    func, symbol = operations[operation]
    result = func(a, b)
    
    # Format the calculation string
    if isinstance(result, str):  # Error case
        calc_string = f"{a} {symbol} {b} = {result}"
    else:
        # Format result to remove unnecessary decimal places
        if result == int(result):
            result = int(result)
        calc_string = f"{a} {symbol} {b} = {result}"
    
    return result, calc_string

def quick_calculation():
    """Quick calculation mode - enter expression directly"""
    print("\n🔄 Quick Calculation Mode")
    print("Enter calculation (e.g., '5 + 3', '10 / 2', '7 * 8'):")
    
    expression = input("Calculate: ").strip()
    
    try:
        # Simple parsing for basic operations
        if '+' in expression:
            parts = expression.split('+')
            if len(parts) == 2:
                a, b = float(parts[0].strip()), float(parts[1].strip())
                result = add(a, b)
                print(f"✅ {a} + {b} = {result}")
                return f"{a} + {b} = {result}"
        
        elif '-' in expression:
            parts = expression.split('-')
            if len(parts) == 2:
                a, b = float(parts[0].strip()), float(parts[1].strip())
                result = subtract(a, b)
                print(f"✅ {a} - {b} = {result}")
                return f"{a} - {b} = {result}"
        
        elif '*' in expression or '×' in expression:
            separator = '*' if '*' in expression else '×'
            parts = expression.split(separator)
            if len(parts) == 2:
                a, b = float(parts[0].strip()), float(parts[1].strip())
                result = multiply(a, b)
                print(f"✅ {a} × {b} = {result}")
                return f"{a} × {b} = {result}"
        
        elif '/' in expression or '÷' in expression:
            separator = '/' if '/' in expression else '÷'
            parts = expression.split(separator)
            if len(parts) == 2:
                a, b = float(parts[0].strip()), float(parts[1].strip())
                result = divide(a, b)
                print(f"✅ {a} ÷ {b} = {result}")
                return f"{a} ÷ {b} = {result}"
        
        else:
            print("❌ Invalid expression format!")
            return None
            
    except ValueError:
        print("❌ Invalid numbers in expression!")
        return None
    except:
        print("❌ Error processing expression!")
        return None

def main():
    """Main calculator function"""
    print("🌟 Welcome to Simple Calculator!")
    history = []
    
    while True:
        show_menu()
        choice = get_operation_choice()
        
        if choice in [1, 2, 3, 4]:  # Arithmetic operations
            print(f"\n{'Addition' if choice == 1 else 'Subtraction' if choice == 2 else 'Multiplication' if choice == 3 else 'Division'}")
            
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            
            result, calc_string = perform_calculation(choice, a, b)
            
            print(f"\n✅ Result: {calc_string}")
            history.append(calc_string)
        
        elif choice == 5:  # Quick calculation
            calc = quick_calculation()
            if calc:
                history.append(calc)
        
        elif choice == 6:  # Show history
            print(f"\n📊 Calculator History ({len(history)} calculations):")
            if history:
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
            else:
                print("  No calculations yet!")
        
        elif choice == 7:  # Exit
            print("\n👋 Thanks for using Simple Calculator!")
            if history:
                print(f"You performed {len(history)} calculations today!")
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()