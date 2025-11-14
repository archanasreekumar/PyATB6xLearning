"""
Question - ✅Palidrome of String

🧩 Example Walkthrough

Let’s take the word "level":
Forward: "level"
Backward: "level"
Both are identical → Palindrome ✅
Now, "hello":
Forward: "hello"
Backward: "olleh"
Not the same → Not a palindrome ❌
"""

in_str = input("Enter a string: ").lower()
len_str = len(in_str)

for i in range(len_str//2):
    if in_str[i] != in_str[len_str-i-1]:
        print("Not palindrome")
        break
print("Palindrome")

