from flask import Flask, request
from flask_restful import Resource, Api
import ner

app = Flask(__name__)
api = Api(app)

todos = {}

tagger = ner.SocketNER(host='localhost', port=8080)

class nerAPI(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
	text_data = request.form['data']
	return tagger.get_entities(text_data)

api.add_resource(nerAPI, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

