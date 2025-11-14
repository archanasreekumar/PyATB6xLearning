# Question - ✅ Count vowels and consonants in a String

vowels = "AEIOUaeiou"
in_str = input("Enter a string: ")
str_len = len(in_str)
vowel_count = 0

for char in in_str:
    if char in vowels:
        vowel_count += 1
print(f"vowel count: {vowel_count}")
print(f"consonant count: {str_len - vowel_count}")


