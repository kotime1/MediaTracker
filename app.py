from flask import Flask
import requests
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("movies.sql")

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"The Boy and the Heron"}

headers = {
	"X-RapidAPI-Key": "9f56ed5b94msh23ffd8dd8332fe8p11435bjsn4cf6f274250e",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())