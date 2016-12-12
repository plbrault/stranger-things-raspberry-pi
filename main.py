from flask import Flask, request
from lib.controller import spell

app = Flask('StrangerThingsApi')

@app.route('/send', methods=['POST'])
def handleRequest():
    spell(request.data.decode('utf-8'))
    return 'Will, is that you?'

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
