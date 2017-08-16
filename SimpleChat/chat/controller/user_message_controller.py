from django.db import connection

from ..models import MessageStream

class UserMessageController(object):

	user_id = None

	def __init__(self, user_id):
		self.user_id = user_id

	def get_existing_messages(self):
		cursor = connection.cursor()
		cursor.execute('SELECT a.message_timestamp, b.user_name, a.message FROM chat_messagestream a INNER JOIN chat_user b ON b.id=a.sender_id WHERE receiver_id = %s ORDER BY message_timestamp', [self.user_id])
		data = cursor.fetchall()
		return [(item[0].strftime("%c"), item[1], item[2]) for item in data]

	def post_message(self, message_timestamp, receiver_id, message):
		record = MessageStream(message_timestamp=message_timestamp, sender_id=self.user_id, receiver_id=receiver_id, message=message)
		record.save()