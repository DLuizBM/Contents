print("Enter state name.")
est = input('\n')

est = est.upper()
if est != "MG" and est != "SP" and est != "RJ" and est != "MS":
    print("The state is not valid.")
    exit()

print("Enter price.")
p = float(input('\n'))

if est == "MG":
    p = p + p * 0.07
    print(f"The price for this state is {p}.")
elif est == "SP":
    p = p + p * 0.12
    print(f"The price for this state is {p}.")
elif est == "RJ":
    p = p + p * 0.15
    print(f"The price for this state is {p}.")
elif est == "MS":
    p = p + p * 0.08
    print(f"The price for this state is {p}.")

