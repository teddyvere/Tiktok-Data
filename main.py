from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/patches')
def about():
    return render_template('patches.html')

if __name__ == '__main__':
    app.run(debug=True)
