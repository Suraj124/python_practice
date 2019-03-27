import urllib.request
try:
    urllib.request.urlretrieve("https://hdqwalls.com/download/python-qhd-1366x768.jpg","python.jpg")
except urllib.request.HTTPError as obj:
    print("Error",obj)
