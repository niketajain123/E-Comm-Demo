from flask import Flask, render_template_string

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head><title>Home Page</title></head>
            <body>
                <h1>Welcome to Our Web Application</h1>
                <p>✅ Login feature is enabled.</p>
                <p>🛒 Shopping feature is enabled.</p>
                /shopGo to Shop</a>
            </body>
        </html>
    ''')

# Shop page
@app.route('/shop')
def shop():
    return render_template_string('''
        <html>
            <head><title>Shop Page</title></head>
            <body>
                <h1>Welcome to the Shop</h1>
                <p>This is a dummy shop page.</p>
                <a hrefo Home</a>
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)