import sqlite3
from datetime import datetime

DB_PATH = 'trade_data.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            order_type TEXT,
            price REAL,
            qty REAL,
            timestamp TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            signal_name TEXT,
            signal_value TEXT,
            signal_strength TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_trade(symbol, order_type, price, qty):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO trades (symbol, order_type, price, qty, timestamp) VALUES (?, ?, ?, ?, ?)', 
              (symbol, order_type, price, qty, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def log_signal_data(symbol, signals):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for s in signals:
        c.execute('INSERT INTO signals (symbol, signal_name, signal_value, signal_strength, timestamp) VALUES (?, ?, ?, ?, ?)', 
                  (symbol, s.get('name'), str(s.get('value')), s.get('signal'), datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
