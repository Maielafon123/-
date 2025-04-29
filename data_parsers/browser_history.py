# data_parsers/browser_history.py
import sqlite3
from pathlib import Path
import os

def get_chrome_history(limit: int = 10) -> list[tuple[str, str]]:
    """Возвращает историю Chrome"""
    history_path = Path(
        os.environ['USERPROFILE'],
        'AppData', 'Local', 'Google', 'Chrome',
        'User Data', 'Default', 'History'
    )
    
    if not history_path.exists():
        return []  # Возвращаем пустой список вместо исключения
    
    try:
        conn = sqlite3.connect(str(history_path))
        cursor = conn.cursor()
        cursor.execute(f"SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT {limit}")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка чтения истории: {e}")
        return []