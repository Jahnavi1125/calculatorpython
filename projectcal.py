import re
from math import sqrt

def parse_expression(text):
    text = text.lower()
    
    # Remove unwanted characters but keep math symbols and decimal points
    text = re.sub(r"[^\w\s\.\+\-\*\/\%\^]", "", text)
    
    # Replace words with math operators
    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = re.sub(r"\b(times|x|multiplied by)\b", "*", text)
    text = re.sub(r"\b(divide|divided by|over)\b", "/", text)
    text = re.sub(r"\b(to the power of|power)\b", "**", text)
    text = re.sub(r"\bsquare root of\b", "sqrt", text)
    
    # Remove extra filler words
    text = re.sub(r"\b(what is|calculate|find|the|of|and|then)\b", "", text)

    # Convert 'sqrt 16' to 'sqrt(16)' using regex
    text = re.sub(r"sqrt\s*(\d+(\.\d+)?)", r"sqrt(\1)", text)

    return text.strip()

def calculate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": None}, {"sqrt": sqrt})
        return result
    except Exception as e:
        return f"❌ Error: {e}"

def calculator():
    print("\n🧮 Welcome to the Word-Based Calculator!")
    print("Examples:")
    print("• What is 5 plus 3")
    print("• Calculate 10 divided by 2")
    print("• Find the square root of 16 plus 9")
    print("• What is 2 to the power of 3")
    print("Type 'exit' to quit.\n")

    while True:
        query = input(">> ")
        if query.lower() == "exit":
            print("👋 Goodbye!")
            break
        parsed = parse_expression(query)
        print("🔍 Parsed:", parsed)
        result = calculate_expression(parsed)
        print("✅ Result:", result)

calculator()
