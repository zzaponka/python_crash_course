first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print("Just a full name:")
print(full_name)
print()
print("F-string with a variable's method:")
print(f"Hello, {full_name.title()}!")
print()
print("Separate message with all that:")
message = f"Hello, {full_name.title()}!"
print(message)
