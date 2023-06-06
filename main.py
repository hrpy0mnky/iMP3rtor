import pdfplumber # Операции с PDF
from gtts import gTTS # Синтез речи из текста
from pathlib import Path # Пути (не путю)
import gui


# Преобразователь
def convertation(f_path, language):

    # Проверка расширения файла
    if Path(f_path).is_file():

        # Представление в виде страниц
        with pdfplumber.PDF(open(file=f_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        
        # Объединение текста
        text = ''.join(pages)

        #Удаление абзацев и отступов
        text = text.replace('\n', '')

        #Преобразование
        audio = gTTS(text=text, lang=language, slow=False)
        f_name = Path(f_path).stem
        audio.save(f'{f_name}.mp3')

        return f'{f_name}.mp3 is successfully saved'

#Переменные для пути и языка
f_path = ""
language = ""

# Точка входа
if __name__ == '__main__':
    gui.application()
    
