from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'Javascript'}, {'name': 'Ruby'}, {'name': 'Python'}]
