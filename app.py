# Import the Flask module
from flask import Flask, jsonify

# Import the PyMongo module to interact with MongoDB
from pymongo import MongoClient

# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("db",27017)

# Get a reference to the Database1
db = client["Database"]

# Get a reference to the collection users
collection = db["users"]

posts = [{ "nom": "Céline", "username": "cece", "password": "$2b$10$EBAr9MAOPPldOCsDnmgKl.RuoYqhit/.BZNaX.w4NHqeeZ/IrWEiu" },  
         { "nom": "Laura", "username": "laulau", "password": "$2b$10$daIsYtG7gYcK5Jw2VvOsgubenJINBXWZ3upeg4AOGKSDhVia/O7jq" },     
         { "nom": "Jolyane", "username": "jojo", "password": "$2b$10$enYQIgNhXs4LJBXLAbd3Gedphy5QISAS1p590lAHFQ0p6vHGr1YhC" },
         { "nom": "Timothée", "username": "timothee", "password": "$2b$10$WRKeDUZW9MljH4iuAaby3Ohv6h6AakF4jTiTDDvacR0rF3jtzyRdG" } ]

collection.insert_many(posts)

# Define the route for the index page
@app.route("/")
def index():
    # Fetch all documents from the users collection
    data = collection.find()

    # Format the data into a string
    formatted_data = "Users:<br><br>"
    for user in data:
        formatted_data += f"Nom: {user['nom']}<br>"
        formatted_data += f"Username: {user['username']}<br>"
        formatted_data += f"Password: {user['password']}<br><br>"

    # Return the formatted data
    return formatted_data

@app.route('/text')
def get_text():
    with open('/app/data/file.txt', 'r') as file:
        file_contents = file.read()
    return jsonify(file_contents)

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")
