import http.client
#1.create an HTTP connection
conn =  http.client.HTTPSConnection("www.cbit.ac.in")

#2.send an HTTP request
conn.request("GET","/")

#3.Get the response from the server
response = conn.getresponse()
#print the response status code
print("Status:",response.status)
#Read the response data
data =response.read()
#print the response data
print("Response:")
print(data.decode())

#4.close the connection
conn.close()






