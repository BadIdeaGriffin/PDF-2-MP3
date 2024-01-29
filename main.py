#Convert PDF to MP3
import pdfplumber
import pyttsx3
speaker = pyttsx3.init()
reader = pdfplumber

#PDF extraction
language = 'en'
text = ""
#Extract text. will need to replace pdf for each new PDF
with reader.open('DICOM_CookBook.pdf') as pdf:
    with reader.askopenfilename() as pdf:
        for page in pdf.pages:
            text += page.extract_text()
        print(text)
pdf.close()

#conversion of text to mp3.
#will need to replace MP3 for each new job
"""speaker.save_to_file(text, 'DICOM_CookBook.mp3')
speaker.runAndWait()
speaker.stop()
print("WORK DONE")"""

"""proposed upgrades: Speed of reader, voices, ui"""