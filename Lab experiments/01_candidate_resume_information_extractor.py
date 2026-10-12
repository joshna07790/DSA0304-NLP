
import re

resume = """
Name: Arun Kumar
Email: arun.kumar@gmail.com
Mobile: +91 9876543210
Portfolio: https://www.arunkumar.com
LinkedIn: http://linkedin.com/in/arunkumar
DOB: 15/08/2002
Graduation: 20-06-2024
"""

patterns = {
    "Email Addresses": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    "Mobile Numbers": r'(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)',
    "URLs": r'https?://[^\s]+',
    "Dates": r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'
}

print("CANDIDATE RESUME INFORMATION EXTRACTOR")
print("-")

for category, pattern in patterns.items():
    matches = re.findall(pattern, resume)
    print(f"\n{category}:")
    if matches:
        for item in matches:
            print(" ", item)
    else:
        print("  Not available")
