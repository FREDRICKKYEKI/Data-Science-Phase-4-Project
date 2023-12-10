#!/usr/bin/python3
"""
Returns the status of our application
"""
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from os import getenv
import pandas as pd
from functions.recom_functions import knn_get_rec, final_recommender

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def page_not_found(_):
    """
    if the route is not found return an error
    """
    return (jsonify({"error": "Not found"}), 404)

@app.get('/status')
def status():
    """
    Return the status of the application
    """
    return jsonify({"status": "OK"})


@app.get("/")
def index():
    """
    Return the status of the application
    """
    movies_df = final_recommender()
    movies = list(movies_df["title"])
    return render_template('index.html', title="", movies=movies, home=True)

@app.route("/movies_like", methods=["POST"], strict_slashes=False)
def movie_recomm():
    """
    Return the status of the application
    """
    form_data = request.form
    title = form_data['movie']

    movies_df = knn_get_rec(title)
    movies = list(movies_df["title"])

    return render_template("index.html", title=title, movies=movies, home=False)


if __name__ == "__main__":
    host = getenv('API_HOST') or '0.0.0.0'
    port = getenv('API_PORT') or 5000

    app.run(host=host, port=port, threaded=True, debug=True)
