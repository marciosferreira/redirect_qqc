from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect_all(path):
    return redirect(f'https://www.locashop.com.br/{path}', code=301)
