from translate import Translator
translator=Translator(to_lang="fr")

with open('your_file.txt','r+')as fileread:
    text=fileread.read()
    translator=translator.translate(text)
print(translator)