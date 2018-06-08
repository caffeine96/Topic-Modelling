import gensim
#To convert document into list of tokens
from gensim.utils import simple_preprocess
#For removing stop words
from gensim.parsing.preprocessing import STOPWORDS
#For Lemmatizing - changing tenses to present, third person to first
#For Stemming - converting to root words. ran -> run
from nltk.stem import WordNetLemmatizer, PorterStemmer

stemmer = PorterStemmer()
#Function to return lemmatized and stemmed text
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

#Function for preprocessing
def preprocess(text):
    result = []
    #Tokenization done through simple_preprocess
    for token in gensim.utils.simple_preprocess(text):
    	#Only words not in stopwords and greater than 3 in length are carried forward
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

#Lets test
if __name__ == "__main__":
	original = "Cat runs to save days"
	words=[]
	for word in original.split(' '):
		words.append(word)
	print "Original: " + str(words)
	print "Lemm and Stemm: " + str(preprocess(original))