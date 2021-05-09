import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire

###################################################################################################################

def basic_clean(original):
    '''
    This function will take in a string of text and begin basic cleaning
    - will make all characters lowercase
    - will normalize unicode
    - will remove special characters
    - will return edited text
    '''
    
    article = original.lower()
    # make all characters lowercase
    
    article = unicodedata.normalize('NFKD', article)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    # normalize unicode
    
    article = re.sub(r"[^a-z0-9'\s]", '', article)
    # remove any special characters
    
    return article

###################################################################################################################

def tokenize(article):
    '''
    This function will take in a string and run a ToktokTokenizer object
    - will return a string of the token words
    - expected to be used after basic_clean function
    '''
    
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # make tokenizer object
    
    token_article = tokenizer.tokenize(article, return_str=True)
    # run tokenizer, return as str
    
    return token_article

###################################################################################################################

def stem(article):
    '''
    This function will take in a string and run a PorterStemmer object
    - will return a string of all the stems of the words in the article
    '''
    
    # Create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()
    
    stems = [ps.stem(word) for word in article.split()]
    # run stemmer object on article to create stems
    
    article_stemmed = ' '.join(stems)
    # create stemmed article by joining stems
    
    return article_stemmed

###################################################################################################################

def lemmatize(article):
    '''
    This functions will take in a string and run a WordNetLemmatizer object
    - will return a string of lemmatized words from the article
    '''
    
    wnl = nltk.stem.WordNetLemmatizer()
    # create lemmatizer object
    
    lemmas = [wnl.lemmatize(word) for word in article.split()]
    ## run lemmatizer object on article
    
    article_lemmatized = ' '.join(lemmas)
    # create lemmatized article by joining lemmatized words together
    
    return article_lemmatized

###################################################################################################################

def remove_stopwords(article):
    '''
    This function will take in a string in the form of an article and remove standard English stop words
    - will return a string of remaining words once all desired stop words have been removed 
    '''
    
    stopword_list = stopwords.words('english')
    # create standard English stop words list
    
    words = article.split()
    # split article into individual words
    
    filtered_words = [w for w in words if w not in stopword_list]
    # filter for words in stop words
    
    article_without_stopwords = ' '.join(filtered_words)
    # recreate article out of remaining words
    
    return article_without_stopwords

###################################################################################################################


def prepare_microsoft(content):
    '''
    This function will prepare data from from the microsoft_github.csv so that it can be used in NLP
    models and exploration
    - will take in a string a clean it
        -lowercase
        -remove accented and special characters
    - will tokenize the string and return the seperated words
    - will lemmatize the content
    - will remove standard English stopwords
        - you can append or remove stopwords using external lists, if desired
    '''
    
    # run cleaning function
    clean_content = basic_clean(content)
    
    # run tokenize function
    tokenized_content = prepare.tokenize(clean_content)
    
    # lemmatize content
    lemmatized_content = lemmatize(tokenized_content)
    
    # remove stopwords
    final_content = remove_stopwords(lemmatized_content, append_stopword, append_stopword)
    
    return final_content

###################################################################################################################

