import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

text = "Este es un texto de prueba, escrito por Daniel F. Puliche durante la clase de Talento Tech en el desarrollo de unos retos o talleres"
tokens = word_tokenize(text)
print("Tokens:", tokens)
