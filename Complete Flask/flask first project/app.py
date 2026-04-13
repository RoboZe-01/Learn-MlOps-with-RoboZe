
# step 1 : Import Flask 

from flask import Flask 


# Step 2 : Create the "App" - This is your waiter

app = Flask(__name__)

# Step 3 : Create a "Route"  - This tells the waiter what to do when someone visits the home page

@app.route('/')
def home():
    return "Hello ! I am Your first Flask app ! "


# Step 4 : This runs the restaurant ( the server )

if __name__ == '__main__':
    app.run(debug=True , port=5000)