# Simple Personal Information Manager

# Taking user inputs
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
hobbies = input("Enter your hobbies (comma-separated): ")

# Convert hobbies string to a list
hobby_list = [h.strip() for h in hobbies.split(",")]

# Display formatted output
print("\n===== Personal Information =====")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print("Hobbies:")
for i, h in enumerate(hobby_list, start=1):
    print(f"  {i}. {h}")
print("================================")
