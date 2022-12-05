from app import app

if __name__ == "__main__":
    app.secret_key = 'the random string'
    app.run(debug=True, port=8080)
