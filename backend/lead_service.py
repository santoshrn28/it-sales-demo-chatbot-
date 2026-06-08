import sqlite3
from datetime import datetime

DB_NAME = "leads.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        company TEXT,
        email TEXT,
        phone TEXT,
        requirement TEXT,
        company_size INTEGER,
        timeline TEXT,
        score TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def calculate_score(company_size: int, timeline: str):
    score = 0

    if company_size and company_size >= 100:
        score += 50

    if timeline and timeline.lower() in ["immediate", "1 month", "3 months"]:
        score += 50

    if score >= 75:
        return "hot"
    elif score >= 40:
        return "warm"

    return "cold"


def save_lead(data):
    init_db()

    score = calculate_score(
        data.get("company_size", 0),
        data.get("timeline", "")
    )

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO leads
    (name, company, email, phone, requirement, company_size, timeline, score, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("name"),
        data.get("company"),
        data.get("email"),
        data.get("phone"),
        data.get("requirement"),
        data.get("company_size"),
        data.get("timeline"),
        score,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()

    return score


def get_leads():
    init_db()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    SELECT id, name, company, email, phone, requirement, company_size, timeline, score, created_at
    FROM leads
    ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "name": r[1],
            "company": r[2],
            "email": r[3],
            "phone": r[4],
            "requirement": r[5],
            "company_size": r[6],
            "timeline": r[7],
            "score": r[8],
            "created_at": r[9],
        }
        for r in rows
    ]
