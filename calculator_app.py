import math
import streamlit as st


def calculate_basic(operation: str, num1: float, num2: float):
    if operation == "Add":
        return num1 + num2
    if operation == "Subtract":
        return num1 - num2
    if operation == "Multiply":
        return num1 * num2
    if operation == "Divide":
        if num2 == 0:
            return ("error", "Error: Division by zero")
        return num1 / num2
    if operation == "Sin()":
        return math.sin(num1)
    return ("error", "Invalid operation!")


def calculate_scientific(operation_sci: str, value: float, power: float):
    if operation_sci == "Square Root":
        if value < 0:
            return ("error", "Error: Cannot take the square root of a negative number.")
        return math.sqrt(value)
    if operation_sci == "Power":
        return math.pow(value, power)
    if operation_sci == "Sin":
        return math.sin(math.radians(value))
    if operation_sci == "Cos":
        return math.cos(math.radians(value))
    if operation_sci == "Tan":
        return math.tan(math.radians(value))
    if operation_sci == "Log (base 10)":
        if value <= 0:
            return ("error", "Error: Logarithm is only defined for numbers greater than 0.")
        return math.log10(value)
    if operation_sci == "Ln (natural log)":
        if value <= 0:
            return ("error", "Error: Natural logarithm is only defined for numbers greater than 0.")
        return math.log(value)
    return ("error", "Invalid scientific operation!")


def main():
    st.title("Basic Web Calculator")

    # Input fields
    num1 = st.number_input("Enter first number", value=0.0, key="basic_num1")
    num2 = st.number_input("Enter second number", value=0.0, key="basic_num2")

    # Operation selection
    operation = st.selectbox(
        "Choose operation",
        ["Add", "Subtract", "Multiply", "Divide", "Sin()"],
        key="basic_op",
    )

    # Calculate
    if st.button("Calculate"):
        outcome = calculate_basic(operation, num1, num2)
        if isinstance(outcome, tuple) and outcome[0] == "error":
            st.error(outcome[1])
        else:
            st.success(f"Result: {outcome}")

    # Scientific Calculator
    st.header("Scientific Functions")
    operation_sci = st.selectbox(
        "Choose scientific operation",
        ["Square Root", "Power", "Sin", "Cos", "Tan", "Log (base 10)", "Ln (natural log)"],
        key="sci_op",
    )

    value = st.number_input("Enter value", value=0.0, key="sci_value")
    power = st.number_input("Enter power (if applicable)", value=2.0, key="sci_power")

    if st.button("Calculate Scientific"):
        outcome = calculate_scientific(operation_sci, value, power)
        if isinstance(outcome, tuple) and outcome[0] == "error":
            st.error(outcome[1])
        else:
            st.success(f"Result: {outcome}")


if __name__ == "__main__":
    main()
