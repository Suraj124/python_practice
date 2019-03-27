import urllib.request
try:
    url=urllib.request.urlopen("https://www.w3schools.com/python/default.asp")
    contenet=url.read()
    url.close()
except urllib.request.HTTPError:
    print("URL not found")
    exit()

f=open("python.html","wb")
f.write(contenet)
f.close()