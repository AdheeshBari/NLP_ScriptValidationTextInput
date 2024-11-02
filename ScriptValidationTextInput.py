import re
def validate_script(text):
    # Check if input text contains only English characters
    if re.fullmatch(r'[A-Za-z\s]+', text):
        print("Text is valid and in English script.")
    else:
        print("Text contains non-English characters.")
user_input = input("Enter some text: ")
validate_script(user_input)

# OUTPUT EXAMPLES
# Input: "Hello World こんにちは"
# Output: Text contains non-English characters.
# Alternative Input: "Hello World"
# Output: Text is valid and in English script.
