# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.
#
# expected_title = "Dashboard"
# actual_title = "Dashboard "

expected_title = "Dashboard"
actual_title = "Dashboard "

if expected_title.strip().upper() == actual_title.strip().upper():
    print("Passed API Request")
else:
    print("Failed API Request")