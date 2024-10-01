import nltk 
from nltk.tokenize import word_tokenize 

nltk.download('punkt')
texto = "NLTK es una biblioteca de procesamiento del lenguaje natural. ¡Es genial!" 

tokens = word_tokenize(texto) 
print(tokens)