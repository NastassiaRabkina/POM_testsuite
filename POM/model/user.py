class User():
	def __init__ (self, username, password):
		self.username = username
		self.password = password

	@classmethod
	def create_user_without_username(cls, password):
		return cls(None, password)

	@classmethod
	def create_user_without_password(cls, username):
		return cls(username, None)
