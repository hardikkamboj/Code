cleaned_lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', text))]
