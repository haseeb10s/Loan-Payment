# Loan and Payment Calculator
def loan_calculator():
     print("Loan Calculator")

     # Input
     principal = float(input("Amount Borrowed $: "))
     interest_rate = float(input("Interest Rate: "))
     year_term = int(input("Loan year Term: "))

     # calculate monthly interest rate
     monthly_interest_rate = interest_rate / 12 / 100
     # calculate number of monthly payment
     num_payments = year_term * 12
     # calculate monthly payment
     monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** - num_payments)

     # declaring variables
     total_interest_paid = 0
     remaining_balance = principal

     print("\nAmount Borrowed: ${:.2f}".format(principal))
     print("Total Interest Paid: ${:.2f}".format(total_interest_paid))

     print("Pytm#      |  Monthly Payment: | Remaining Balance: ")
     print("-" * 43)

     for months in range(1, num_payments + 1):
         interest_payment = monthly_interest_rate * remaining_balance
         principal_payment = interest_payment - monthly_payment
         total_interest_paid += interest_payment
         remaining_balance -= principal_payment

         print(f"{months:9d} | ${monthly_payment:.2f}            | ${remaining_balance:.2f}")
     print("Okay")

if __name__ == "__main__":
    loan_calculator()