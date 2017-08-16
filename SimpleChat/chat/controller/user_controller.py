from ..models import User


def get_or_create_user_id_from_name(username):
	user_id = get_user_id_from_name(username)
	return user_id if user_id else create_user(username)

def get_user_id_from_name(username):
	try:
		user_ids = User.objects.get(user_name=username)
		user_id = user_ids.user_id
	except User.DoesNotExist:
		user_id = None
	return user_id

def create_user(username):
	record = User(user_name=username)
	record.save()
	return record.user_id