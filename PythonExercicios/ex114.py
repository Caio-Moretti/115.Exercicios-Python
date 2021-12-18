import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('ERRO')
else:
    print('FUNCIONOU')
    print(site.read())
