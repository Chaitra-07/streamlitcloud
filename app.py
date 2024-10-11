import streamlit as st

# Title of the web app
st.title('Square Calculator')

# Create a numeric input widget for the user
number = st.number_input('Enter a number:', min_value=0.0, step=1.0)

# Button to calculate the square
if st.button('Calculate Square'):
    square = number ** 2
    st.write(f'The square of {number} is {square}.')
