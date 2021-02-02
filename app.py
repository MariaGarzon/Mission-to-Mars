# Use Flask to render a template
from flask import Flask, render_template, redirect
# Use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo
# To use the scraping code, we will convert from Jupyter notebook to Python
import scraping
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)
#chrome_path = r'/Users/Maria/Desktop/Mission-to-Mars/chromedriver' 
#driver = webdriver.Chrome(executable_path=chrome_path)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Set up the scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect("/", code=302)

if __name__ == "__main__":
    app.run

