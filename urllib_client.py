import urllib.request

#1&2&3 steps make an HTTP GET request
#response = urllib.request.urlopen("https://www.cbit.ac.in/about_post/office/")
response = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

#Read the response data
data = response.read()
#print the response data
print("Response:")
print(data.decode())


#4. close the response
response.close()
