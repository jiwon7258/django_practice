""" 
웹 클라리언트
웹 서버에 HTTP 요청을 보내는 웹 클라이언트
 """
import urllib.request

print(urllib.request.urlopen("http://www.example.com").read().decode("utf-8"))
