from .database import db


def init_database():
    db.create_table(
        "groups",
        [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "chat_id INTEGER UNIQUE",
            "publish_frequency INTEGER",
        ],
    )
