import urllib.request, urllib.parse, urllib.error

response = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
#print the response text line by line
for line in response:
    print(lin.decode().strip())


#print count of each word in the web page
counts = dict()
for line in response:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)


