import pyshorteners

url = input('Enter your url : \n')

print('URL after shorting : ',pyshorteners.shortener().tinyurl(url))