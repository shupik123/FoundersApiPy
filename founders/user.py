from urllib import error
from urllib import request
import json

class user_info:
	def __init__(self, _id):
		try:
			response = request.urlopen('http://api.founders.gg/users/{}'.format(_id)).read()
			response = str(response)[2:-1]
			json_data = json.loads(response)
			# example: [{'username': 'Xelada', 'rank': 'Admin', 'servers': '2,4', 'lastSeen': 1568418961, 'created': 0}]
			json_data = json_data[0]

			try:
				if json_data['error'] == 'This resource was not found':
					self.success = False

			except KeyError:
				self.success = True
				self.username = json_data['username']
				self.rank = json_data['rank']
				self.servers = json_data['servers']
				self.lastSeen = json_data['lastSeen']
				self.created = json_data['created']

		except:
			self.success = False

def info(_id):
	return user_info(_id)

def all():
	return {
		'Xelada': 1,
		'dylanrocks2': 56,
		'shupik': 65,
		'Xeladarocks': 66,
		'TestUser1': 71,
		'TestUser2': 72
	}