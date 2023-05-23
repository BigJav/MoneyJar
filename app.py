import streamlit as st
import pandas as pd
import base64

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
        self.transaction_history = pd.DataFrame(columns=['Jar', 'Transaction Type', 'Amount'])

    def add_income(self, income):
        self.income += income
        for jar in self.jars:
            self.jars[jar] += income * self.percentages[jar]
            self.transaction_history = self.transaction_history.append({'Jar': jar, 'Transaction Type': 'Deposit', 'Amount': income * self.percentages[jar]}, ignore_index=True)

    def withdraw(self, jar, amount):
        if self.jars[jar] >= amount:
            self.jars[jar] -= amount
            self.transaction_history = self.transaction_history.append({'Jar': jar, 'Transaction Type': 'Withdrawal', 'Amount': amount}, ignore_index=True)
            return amount
        else:
            st.write("Insufficient funds in", jar)
            return 0

    def display_jars(self):
        for jar in self.jars:
            st.write(jar, ":", self.jars[jar])

    def save_to_csv(self):
        self.transaction_history.to_csv('transaction_history.csv', index=False)

def get_table_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="transaction_history.csv">Download CSV File</a>'
    return href

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
if st.button('Display Jars'):
    my_jars.display_jars()

# Save to CSV and provide download link
if st.button('Save Transaction History'):
    my_jars.save_to_csv()
    st.markdown(get_table_download_link(my_jars.transaction_history), unsafe_allow_html=True)
