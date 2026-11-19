import streamlit as st

# Title and Header
st.title("Retail Business Dashboard")



# Instruction
st.subheader("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")


# Number input for sales target
target_sales = st.number_input("Enter Monthly Sakes Target(in USD):",
                      min_value=0,
                      max_value=50000,
                      value=50000)


# Dropdown for region selection
region = st.selectbox("Select Region:",
                      ["North", "South", "East", "West"])


# Submit button
if st.button("Submit"):
    # Display entered values
  st.write(f"Your Target Sales is ${target_sales}")

    # Success message
st.success("Confirms successful update.")


    # Extra message for ambitious target



