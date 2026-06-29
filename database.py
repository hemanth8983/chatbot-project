import sqlite3

conn = sqlite3.connect("chatlogs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT
)
""")

conn.commit()

def save_chat(user, bot):
    cursor.execute(
        "INSERT INTO logs(user_message, bot_response) VALUES (?, ?)",
        (user, bot)
    )
    conn.commit()