"""
An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.

If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:

Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed"""

retry_count = 3
attempt_count = 1
response = 0
while attempt_count <= retry_count:
    response = int(input("Enter api response: "))
    print(f"Attempt {attempt_count}: Response {response}")
    if response == 200:
        print("Test Passed")
        break
    attempt_count += 1

if response != 200:
    print("❌ Test Failed after 3 attempts.")
