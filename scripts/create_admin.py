from db.database import get_connection
from pages.register import hash_password
''
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
    INSERT OR IGNORE INTO users (name, email, password, role)
    VALUES (?, ?, ?, ?)
""", (
    "Admin",
    "admin@email.com",
    hash_password("admin123"),
    "admin"
))

conn.commit()
conn.close()
