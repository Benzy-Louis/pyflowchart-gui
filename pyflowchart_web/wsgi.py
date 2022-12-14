"""Web Server Gateway Interface aka wsgi"""
from app import init_app

app = init_app()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
