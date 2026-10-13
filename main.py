
print("=========== Python Text Analyzer tool ==========")

user_text = input("Enter sentence here : ")
#len will basically help me to find the total words
total_chars_with_space = len(user_text)
total_chars_no_space = len(user_text.replace(" ", ""))
# if there is any white space in user name this will split will erase those white gap
words_list = user_text.split()
total_words = len(words_list)
vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_text:
    if char in vowels:
        vowel_count += 1  # (Note: Python will have  vowel_count += 1 .
upper_case = user_text.upper()
lower_case = user_text.lower()
reversed_text = user_text[::-1]
print("=" * 100)
print("\n" + "=" * 30)
print("your text reports :")
print("=" * 30)
print("Original Text:", user_text)
print("Total Words:", total_words)
print("Characters (with space):", total_chars_with_space)
print("Characters (withoutspace):", total_chars_no_space)
print("Total Vowels:", vowel_count)
print("UPPERCASE:", upper_case)
print("lowercase:", lower_case)
print("Reversed Text:", reversed_text)
print("=" * 30)
        
