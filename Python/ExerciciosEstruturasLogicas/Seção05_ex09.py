print("Enter a salary.")
sal = float(input())

print("Enter the installment.")
p = float(input())

sal = sal * 0.2

if p <= sal:
    print("Loan granted!")
else:
    print("Loan not granted.")

