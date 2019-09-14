from urllib import error
from urllib import request
import json

class server_info:
	def __init__(self, _id):
		try:
			response = request.urlopen('http://api.founders.gg/servers/{}'.format(_id)).read()
			response = str(response)[2:-1]
			json_data = json.loads(response)
			# example: [{'username': 'Xelada', 'rank': 'Admin', 'servers': '2,4', 'lastSeen': 1568418961, 'created': 0}]
			json_data = json_data[0]

			try:
				if json_data['error'] == 'This resource was not found':
					self.success = False

			except KeyError:
				self.success = True

		except:
			self.success = False

def info(_id):
	return server_info(_id)

def all():
	return {
		'Founders': 1,
		'IAC': 2,
		'Founders 2': 3,
		'Vnlla': 4
	}