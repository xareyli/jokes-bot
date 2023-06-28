from .database import db


def add_group(group_id):
    try:
        db.insert_data("groups", ("chat_id", "publish_frequency"), (group_id, 3))
        return True
    except:
        return False


def update_group_publish_frequency(group_id, new_hours):
    try:
        db.execute_query("UPDATE groups SET publish_frequency = ? WHERE chat_id = ?", (new_hours, group_id))
        return True
    except:
        return False

def get_all_groups():
    try:
        return db.execute_query("SELECT * FROM groups")
    except:
        return ()

def delete_group(group_id):
    try:
        return db.execute_query("DELETE FROM groups WHERE chat_id = ?", (group_id, ))
    except:
        return False
