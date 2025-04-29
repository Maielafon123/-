# data_parsers/file_system.py
import os
from pathlib import Path
import docx
# data_parsers/file_system.py
import sys
sys.path.append("C:\\Users\\cvtcvtcvt\\Desktop\\digital_self_game")  # ← Абсолютный путь

from config import BASE_DIRS, IGNORE_FILES

def scan_documents() -> dict:  # ← Убедитесь, что функция названа точно так!
    """Сканирует документы на наличие ключевых слов"""
    file_data = {
        "txt": [],
        "docx": [],
        "exe": [],
        "secret_keywords": []
    }

    SECRET_WORDS = ["секрет", "парол", "тайный", "confidential"]

    for location in [BASE_DIRS["desktop"], BASE_DIRS["documents"]]:
        for root, _, files in os.walk(location):
            for file in files:
                file_path = Path(root) / file
                if file.lower() in IGNORE_FILES:
                    continue

                try:
                    # Анализ TXT
                    if file.endswith(".txt"):
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read(2000)
                            file_data["txt"].append(str(file_path))
                            if any(word in content.lower() for word in SECRET_WORDS):
                                file_data["secret_keywords"].append(str(file_path))
                    
                    # Анализ DOCX
                    elif file.endswith(".docx"):
                        doc = docx.Document(file_path)
                        content = " ".join([para.text for para in doc.paragraphs[:5]])
                        file_data["docx"].append(str(file_path))
                        if any(word in content.lower() for word in SECRET_WORDS):
                            file_data["secret_keywords"].append(str(file_path))
                    
                    # EXE-файлы
                    elif file.endswith(".exe"):
                        file_data["exe"].append(str(file_path))
                        
                except Exception as e:
                    print(f"Ошибка анализа файла {file_path}: {e}")
                return file_data
if __name__ == "__main__":
    print("Тест модуля file_system:")
    print(scan_documents())