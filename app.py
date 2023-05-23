import streamlit as st

class MoneyJar:
    def __init__(self, income):
        self.income = income
        self.jars = {
            "Living Necessities": 0,
            "Savings to Spend": 0,
            "Financial Freedom": 0,
            "Play": 0,
            "Giving": 0,
            "Personal Development": 0
        }
        self.percentages = {
            "Living Necessities": 0.5,
            "Savings to Spend": 0.1,
            "Financial Freedom": 0.1,
            "Play": 0.1,
            "Giving": 0.1,
            "Personal Development": 0.1
        }

    def add_income(self, income):
        self.income += income
        for jar in self.jars:
            self.jars[jar] += income * self.percentages[jar]

    def withdraw(self, jar, amount):
        if self.jars[jar] >= amount:
            self.jars[jar] -= amount
            return amount
        else:
            st.write("Insufficient funds in", jar)
            return 0

    def display_jars(self):
        for jar in self.jars:
            st.write(jar, ":", self.jars[jar])

# Streamlit UI
st.title('Money Jar System')

# Initialize MoneyJar with 0 income
my_jars = MoneyJar(0)

# Input for adding income
income = st.number_input('Enter your income', min_value=0.0, step=0.1)
if st.button('Add Income'):
    my_jars.add_income(income)
    st.write('Income added!')

# Input for withdrawing from a jar
jar = st.selectbox('Select a jar to withdraw from', list(my_jars.jars.keys()))
amount = st.number_input('Enter amount to withdraw', min_value=0.0, step=0.1)
if st.button('Withdraw'):
    my_jars.withdraw(jar, amount)
    st.write('Withdrawn!')

# Display jars
st.button('Display Jars')
my_jars.display_jars()
