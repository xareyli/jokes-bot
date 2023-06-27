from .database import db


def add_group(group_id):
    try:
        db.insert_data("groups", ("chat_id", "publish_frequency"), (group_id, 3))
        return True
    except:
        return False
