import os
from data_parsers.browser_history import get_chrome_history
from data_parsers.file_system import scan_documents

def kill_chrome_processes():
    os.system('taskkill /f /im chrome.exe /im chromedriver.exe 2>nul')

def main():
    print("🔮 Игра начинает анализ вашей цифровой жизни...\n")
    kill_chrome_processes()
    
    try:
        
        history = get_chrome_history(limit=10)
        print("\n🌐 Найдено в истории браузера:")
        if history:
            for url, title in history:
                print(f"→ {title[:50]}... ({url[:30]})")
        else:
            print("→ История недоступна или пуста")
        
        
        files = scan_documents()
        print("\n📂 Документы:")
        print(f"Текстовых файлов: {len(files['txt'])}")
        print(f"Документов Word: {len(files['docx'])}")
        if files['secret_keywords']:
            print(f"\n🔒 Подозрительные файлы:")
            for file in files['secret_keywords'][:3]:
                print(f"→ {file}")
    
    except Exception as e:
        print(f"\n🚨 Ошибка: {e}")
    
    input("\nНажмите Enter чтобы выйти...")

if __name__ == "__main__":
    main()