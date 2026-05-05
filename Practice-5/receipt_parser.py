import re
import json


# 1. String has 'a' followed by zero or more 'b'
def match_a_followed_by_zero_or_more_b(text):
    pattern = r"ab*"
    return bool(re.fullmatch(pattern, text))


# 2. String has 'a' followed by two to three 'b'
def match_a_followed_by_2_3_b(text):
    pattern = r"ab{2,3}"
    return bool(re.fullmatch(pattern, text))


# 3. Find sequences of lowercase letters joined with underscore
def find_lowercase_with_underscore(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, text)


# 4. Find sequences of one uppercase letter followed by lowercase letters
def find_upper_lower(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)


# 5. String has 'a' followed by anything, ending in 'b'
def match_a_anything_b(text):
    pattern = r"a.*b$"
    return bool(re.fullmatch(pattern, text))


# 6. Replace space, comma, or dot with colon
def replace_special(text):
    pattern = r"[ ,.]+"
    return re.sub(pattern, ":", text)


# 7. Snake case to camel case
def snake_to_camel(text):
    words = text.split("_")
    return words[0] + ''.join(word.capitalize() for word in words[1:])


# 8. Split string at uppercase letters
def split_at_uppercase(text):
    pattern = r"(?=[A-Z])"
    return re.split(pattern, text)


# 9. Insert spaces between words starting with capital letters
def insert_spaces(text):
    pattern = r"([A-Z])"
    return re.sub(pattern, r" \1", text).strip()


# 10. Camel case to snake case
def camel_to_snake(text):
    pattern = r'([a-z0-9])([A-Z])'
    return re.sub(pattern, r'\1_\2', text).lower()


# Receipt Parser
def parse_receipt(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Extract prices
    prices = re.findall(r'\d[\d ]*,\d{2}', text)

    # Convert prices to numbers
    numeric_prices = []
    for price in prices:
        clean_price = price.replace(" ", "").replace(",", ".")
        numeric_prices.append(float(clean_price))

    # Product names
    products = re.findall(r'\d+\.\n(.*?)\n\d+,\d+\s*x', text, re.MULTILINE)

    # Total amount
    total = re.search(r'ИТОГО:\n([\d ]+,\d{2})', text)

    total_amount = None
    if total:
        total_amount = total.group(1)

    # Date and time
    datetime_match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', text)

    # Payment method
    payment = re.search(r'(Банковская карта|Наличные):', text)

    result = {
        "products": products,
        "prices": prices,
        "total_amount": total_amount,
        "datetime": datetime_match.group(1) if datetime_match else None,
        "payment_method": payment.group(1) if payment else None
    }

    return result


# Testing examples
print("1:", match_a_followed_by_zero_or_more_b("abbb"))
print("2:", match_a_followed_by_2_3_b("abb"))
print("3:", find_lowercase_with_underscore("hello_world test_text"))
print("4:", find_upper_lower("Hello World Python"))
print("5:", match_a_anything_b("axxxb"))
print("6:", replace_special("Hello, world. Python"))
print("7:", snake_to_camel("hello_world_python"))
print("8:", split_at_uppercase("HelloWorldPython"))
print("9:", insert_spaces("HelloWorldPython"))
print("10:", camel_to_snake("helloWorldPython"))


# Parse receipt file
receipt_data = parse_receipt("raw.txt")

print("\nParsed Receipt:")
print(json.dumps(receipt_data, indent=4, ensure_ascii=False))