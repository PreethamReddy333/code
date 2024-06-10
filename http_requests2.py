
import requests
# Send an HTTP GET request to the Wikipedia page
url = "https://www.cbit.ac.in/placement_post/placement/"
#response = requests.get(https://www.cbit.ac.in/placement_post/placement/)
response = requests.get(url)
# Access the response content
print("Response content:", response.content)
# Save the response to a file
with open('placement_cbit.html', 'wb') as file:
    file.write(response.content)
"""
# Convert a string to bytes using UTF-8 encoding
string = "Hello, World!"
print("UTF data:",string)
bytes_data = string.encode('utf-8')
# Print the bytes representation
print("Bytes data:", bytes_data)
"""
