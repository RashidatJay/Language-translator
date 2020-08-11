from translate import Translator
translator=Translator(to_lang="fr")

with open('your_file.txt','r+')as fileread:
    text=fileread.read()
    translator=translator.translate(text)
    with open('translated.txt', 'w')as translated_text:
        translated_text.write(translator)

print(translator)