from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("product_name", required=True, help="Product name requied")


class Product(Resource):

	def get(self, product_id = None):
		if product_id is None:
			return jsonify(data='get req without prod id return all')
		return jsonify(data='get req', product_id = product_id)

	def put(self, product_id=None):
		if product_id is None:
			return jsonify(data='update req without prod id return all')
		return jsonify(data='put req', product_id=product_id)

	def post(self):
		args = parser.parse_args()
		name = args['product_name']
		return jsonify(data='post req', product_name = name)

	def delete(self, product_id=None):
		if product_id is None:
			return jsonify(data='delete req without prod id return all')
		return jsonify(data='delete req', product_id = product_id)


api.add_resource(Product, '/product', '/product/<string:product_id>')


if __name__ == "__main__":
	app.run(debug=True)