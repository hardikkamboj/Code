# clearning corpus, which contains words only. 
cleaned_lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', text))]



# clearning sentences from df 
# stop_words = stopwords.words('english') # 179 elements

df['cleaned_text'] = df['text'].apply(lambda x : ' '.join([lemmatizer.lemmatize(word.lower()) \
    for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', str(x))) if word.lower() not in stop_words]))

