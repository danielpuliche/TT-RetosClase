import nltk
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Descargar los recursos necesarios
nltk.download('wordnet')
nltk.download('punkt_tab')

# Crear el objeto lematizador
lemmatizer = WordNetLemmatizer()

# Texto de ejemplo
texto = "The cats are playing with the toys while the children played outside. They were running quickly, but one of them stopped when they saw a dog. The dog was barking loudly, and the children decided to go back inside. Meanwhile, the toys were scattered all over the room."

# Tokenizar el texto
tokenized_words = word_tokenize(texto)

# Aplicar lematización a cada palabra
lemmatized_words = [lemmatizer.lemmatize(palabra, pos='v') for palabra in tokenized_words]

word_freq = pd.Series(lemmatized_words).value_counts()
print("Frecuencia de palabras:\n", word_freq)
