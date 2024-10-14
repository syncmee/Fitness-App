from flask import Flask, render_template,url_for

app = Flask(__name__)
app.secret_key = 'Secret_Key'



@app.route('/')
def homepage():
    return render_template('homepage.html')
#test

if __name__ == '__main__':
    app.run(debug=True)
