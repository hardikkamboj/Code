# libraries required
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


# clearning corpus, which contains words only. 
cleaned_lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', text))]



# clearning sentences from df 
df['cleaned_text'] = df['text'].apply(lambda x : ' '.join([lemmatizer.lemmatize(word.lower()) \
    for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', str(x))) if word.lower() not in stop_words]))

# clearning sentences from df and removing alpha numeric words 
df['cleaned_text'] = df['Text'].apply(lambda x : ' '.join([lemmatizer.lemmatize(word.lower()) \
    for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', str(x))) if (word.lower() not in stop_words) 
                                                           and word.isalpha() ]))

