#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
规则文件，定义规则类，实现is_worning方法，该方法必须返回布尔类型，True时报警，False不报警
"""

import time

from VisitorManage.models import Visitor

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
		
class OnlyVisitor(object):
	"""docstring for OnlyVisitor"""
	def __init__(self):
		super(OnlyVisitor, self).__init__()

	def is_worning(self,room_status):
		persons_str = room_status.persons
		persons = eval(persons_str)
		worning = True
		for person_id in persons:
			visitor = Visitor.objects.get(id=person_id)
			if visitor.is_staff:
				worning = False
				break
		if worning:
			return True
		else:
			return False

class ImportTimeAnomaly(object):
	"""docstring for ImportTimeAnomaly"""
	def __init__(self):
		super(ImportTimeAnomaly, self).__init__()

	def compare_time(self,l_time,start_t,end_t):
		s_time = time.mktime(time.strptime(start_t,'%Y-%m-%d %H:%M:%S'))
		e_time = time.mktime(time.strptime(end_t,'%Y-%m-%d %H:%M:%S'))
		log_time = time.mktime(time.strptime(l_time,'%Y-%m-%d %H:%M:%S'))
		if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
			return True
		return False
	
	def is_worning(self,room_status):
		optiontime = room_status.optiontime
		refuse_start = " ".join([optiontime.split(" ")[0],"00:00:00"])
		refuse_end = " ".join([optiontime.split(" ")[0],"06:00:00"])
		current_time = None
		if self.compare_time(optiontime,refuse_start,refuse_end):
			return True
		else:
			return False
		

		