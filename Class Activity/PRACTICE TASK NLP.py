import re

text = "My email is joshna@gmail.com and my phone number is 9876543210."

# 1. Match a pattern at the beginning of the text
pattern = r"My"
match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")

# 2. Search for an email address
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = re.search(email_pattern, text)

if email:
    print("Email found:", email.group())
else:
    print("Email not found")

# 3. Search for a phone number
phone_pattern = r"\b\d{10}\b"
phone = re.search(phone_pattern, text)

if phone:
    print("Phone number found:", phone.group())
else:
    print("Phone number not found")

# 4. Find all numbers in the text
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)
