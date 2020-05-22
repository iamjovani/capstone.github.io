from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")

# Enter your database connection details below
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = ''


# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Intialize MySQL
#mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('Main.html')

if __name__ == '__main__':
   app.run(debug = True)