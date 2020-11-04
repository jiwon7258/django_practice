from wsgiref.simple_server import make_server

# WSGI 규격을 준수하는 웹 애플리케이션 코드
def my_app(environ, start_resoponse):

    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    # 웹 애플리케이션을 호출한다
    start_resoponse(status, headers)

    response = [b"This is a sample WSGI Application"]

    return response


if __name__ == "__main__":
    print("Started WSGI server on port 8888...")
    server = make_server("", 8888, my_app)
    server.serve_forever()