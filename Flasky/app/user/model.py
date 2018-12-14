

class VerrifyStatus:
	checking = "checking"
	finish = "finish"


class User(object):
	username = None
	password = None
	status = VerrifyStatus.checking

	def __init__(self, username="username", password=None, status = VerrifyStatus.checking):
		self.username = username
		self.password = password
		self.status = status


