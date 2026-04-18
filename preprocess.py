import re
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)

    tokens = word_tokenize(text)

    # ❌ set → remove
    # ✅ list use பண்ணு
    tokens = [token for token in tokens if token not in stop_words]

    lemmatizer_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return " ".join(lemmatizer_tokens)

