from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'Javascript'}, {'name': 'Ruby'}, {'name': 'Python'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

@app.route('/languages', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

@app.route('/languages/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

@app.route('/languages', methods=['POST'])
def addOne():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})

@app.route('/languages/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    if not request.json:
        abort(404)
    langs[0]['name'] = request.json.get('name', langs[0]['name'])
    return jsonify({'language': langs[0]})

@app.route('/languages/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})



if __name__ == '__main__':
    app.run(debug=True, port=8080)
