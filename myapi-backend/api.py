#!/usr/bin/python2.7
# coding: utf-8
# Author :

import os
import sys

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

try:
    api_data_path = os.environ.get('API_DATA_PATH')
except:
    print("Le chemin vers le fichier de données n'est pas défini. Elle doit être définie dans une variable d'environnement nommé 'API_DATA_PATH'")


def get_data():
    """
      Renvoit le contenu d'un fichier dans une chaine
    """
    try:
        with open(api_data_path, 'r') as file_:
            data = file_.read()
    except BaseException as err:
        return api_data_path
    return data

@app.route('/')
def index():
    """
      Renvoit une phrase dans un dictionnaire au format JSON
    """
    response = {}
    response['body'] = get_data()
    return jsonify(response)


@app.route('/traceback')
def traceback():
    """
        Termine l'application avec un code erreur 1
    """
    os._exit(1)
    return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
