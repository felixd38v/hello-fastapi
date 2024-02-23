
# Import the FastAPI class from the fastapi module.
# This FastAPI class is used to create instances of the FastAPI aplication

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for GET requests to 
@app.get("/hello")
def greet():
	# Return a string as the response
    return "Hello FastAPI"
