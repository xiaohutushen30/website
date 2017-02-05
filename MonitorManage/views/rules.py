class PersonNumUniformity(object):
	"""docstring for PersonNumUniformity"""
	def __init__(self):
		super(PersonNumUniformity, self).__init__()

	def is_worning(self, room_status):
		frid_personnumber = int(room_status.frid_personnumber)
		ir_personnumber = int(room_status.ir_personnumber)
		if frid_personnumber != ir_personnumber:
			return True
		else:
			return False
		