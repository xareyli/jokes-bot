from .database import db


def add_group(group_id):
    try:
        db.insert_data("groups", ("chat_id", "publish_frequency"), (group_id, 3))
        return True
    except:
        return False


def update_group_publish_frequency(group_id, new_hours):
    try:
        db.execute_query("UPDATE groups SET publish_frequency = ? WHERE chat_id = ?", (group_id, new_hours))
        return True
    except:
        return False
