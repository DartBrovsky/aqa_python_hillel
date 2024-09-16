import ssl
from urllib import request
from urllib import parse
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse, ParseResult

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

base_url: str = "https://www.example.com"
try:
    response = request.urlopen(base_url, context=context)
    data = response.read()
    print(data)
except URLError as exception:
    print(exception)



data = {'key1': 'value1', 'key2': 'value2'}

data_to_post = parse.urlencode(data).encode('utf-8')
try:
    response = request.urlopen(base_url, data_to_post, context=context)
    result = response.read()
    print(result)
except HTTPError as exception:
    print(exception)

url: str = "https://www.example.com/path/to/login?login=user_login&password=user_password"

parsed_url: ParseResult = urlparse(url)

print("Схема:", parsed_url.scheme)
print("Мережева адреса:", parsed_url.netloc)
print("Шлях:", parsed_url.path)
print("Параметри:", parsed_url.params)
print("Запити:", parsed_url.query)
print("Фрагмент:", parsed_url.fragment)

