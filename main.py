import PyPDF2
from gtts import gTTS, lang
from tkinter import *
from tkinter import filedialog


lang_codes = {'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew', 'ja': 'Japanese', 'jw': 'Javanese', 'km': 'Khmer', 'kn': 'Kannada', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ms': 'Malay', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'si': 'Sinhala', 'sk': 'Slovak', 'sq': 'Albanian', 'sr': 'Serbian', 'su': 'Sundanese', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-CN': 'Chinese (Simplified)', 'zh-TW': 'Chinese (Mandarin/Taiwan)', 'zh': 'Chinese (Mandarin)'}
languages = ['Afrikaans', 'Arabic', 'Bulgarian', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Danish', 'German', 'Greek', 'English', 'Spanish', 'Estonian', 'Finnish', 'French', 'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Hebrew', 'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Malayalam', 'Marathi', 'Malay', 'Myanmar (Burmese)', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese', 'Chinese (Simplified)', 'Chinese (Mandarin/Taiwan)', 'Chinese (Mandarin)']

window = Tk()
window.title("PDF to Audiobook Converter")
window.minsize(width=600, height=450)

clicked = StringVar(window)
clicked.set("English")

lang_dropdown = OptionMenu(window, clicked, *languages)
lang_dropdown.pack()


def get_key(val):
    for key, value in lang_codes.items():
        if val == value:
            return key

    return "key doesn't exist"

file_name = "Not selected yet."
lang_code = "en"
text = ""
def select_file():
    global text, file_name, lang_code
    language_selected = clicked.get()
    print(type(language_selected))
    print ("value is: " + language_selected)
    lang_code = get_key(language_selected)
    print(lang_code)
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a PDF File", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    print("The chosen PDF file:", file_path)
    pdf_file = open(f"{file_path}", "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    print(f"filepath: {file_path}, pdffile: {pdf_file}")
    file_name = file_path.split("/")[-1]
    label.config(text=f"{file_name}")
    print(file_name)
    pdf_file.close()


def text_to_speech():
    speech =  gTTS(f"Hello {text}", slow=False, lang=lang_code)
    speech_file = f"pdf_to_audiobook_{file_name}.mp3"
    speech.save(speech_file)


select_file_button = Button(window, text="Select PDF", command=select_file)
select_file_button.pack()


label = Label(window, text=f"{file_name}")
label.pack()

convert_button = Button(window, text="Convert PDF to Audiobook", command=text_to_speech)
convert_button.pack()




window.mainloop()


