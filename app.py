# app.py
import streamlit as st
from calc import add, subtract, multiply, divide

def main():
    st.title("Simple Calculator App")
    
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    
    operation = st.selectbox(
        "Select Operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )
    
    result = 0
    
    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
