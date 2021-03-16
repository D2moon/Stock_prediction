import urllib.request

response = urllib.request.urlopen('http://www.baidu.com/', None, 2)

print(response)

html = response.read().decode('utf-8')
f = open('code1.txt', 'w', encoding='utf-8')
f.write(html)
f.close()