import urllib.request, urllib.parse,urllib.error

response = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in response:
    print(line.decode().strip())
