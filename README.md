# NLP_ScriptValidationTextInput
This code checks if an input string contains only English letters and spaces, indicating whether the text is valid or contains non-English characters.

This code checks whether an input string contains only English alphabetic characters and spaces.
1. Imports re module: Allows the use of regular expressions for pattern matching.
2. Defines validate_script() function: Takes a text string and validates if it contains only English letters and spaces.
3. Uses re.fullmatch(r'[A-Za-z\s]+', text): Matches the entire text to ensure it only includes uppercase/lowercase English letters (A-Z, a-z) and spaces (\s).
      If the text matches, it prints "Text is valid and in English script."
      If the text contains non-English characters (e.g., symbols, numbers, or other languages), it prints "Text contains non-English characters."
4. Gets user input: Prompts the user to enter text, which is then validated by the validate_script() function.

