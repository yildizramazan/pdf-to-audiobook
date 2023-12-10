import PyPDF2
from gtts import gTTS, lang
import os
from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader


#all languages
lang_codes = {'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew', 'ja': 'Japanese', 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ms': 'Malay', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-CN': 'Chinese (Simplified)', 'zh-TW': 'Chinese (Mandarin/Taiwan)', 'zh': 'Chinese (Mandarin)'}
languages = ['Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Danish', 'German', 'Greek', 'English', 'Spanish', 'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Hebrew', 'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Malayalam', 'Marathi', 'Malay', 'Myanmar (Burmese)', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese (Simplified)', 'Chinese (Mandarin/Taiwan)', 'Chinese (Mandarin)']

window = Tk()
window.title("PDF to Audiobook Converter")
window.minsize(width=600, height=450)

clicked = StringVar(window)

# initial menu text
clicked.set("English")

# Create Dropdown menu
lang_dropdown = OptionMenu(window, clicked, *languages)
lang_dropdown.pack()

def ok():
    language_selected = clicked.get()
    print ("value is: " + language_selected)



def select_file():
    text = ""
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a PDF File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    print("The chosen PDF file:", file_path)
    pdf_file = open(f"{file_path}", "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    pdf_file.close()
    return f"um here is text {text}"

select_file_button = Button(window, text="Select PDF", command=select_file)
select_file_button.pack()

text_to_convert_to_audiobook = select_file()






button = Button(window, text="OK", command=ok)
button.pack()

window.mainloop()


