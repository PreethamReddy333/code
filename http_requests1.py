import requests
# 1 & 2 & 3 & 4 Send an HTTP GET request to the Wikipedia page
#url = 'https://www.cbit.ac.in/current_students/exam-time-table/'
response = requests.get("https://www.cbit.ac.in/")
# Access the response content
print("Response content:", response.content)

# Save the response to a file
with open('exam_timetable_cbit.html', 'wb') as file:
    file.write(response.content)
#print response headers
print("HTTP Headers:")
print(response.headers)

#print the response HTTP body
print("HTTP Body:")
print(response.text)

