import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.lancaster import LancasterStemmer

# nltk.download()

from nltk.book import *

text1.concordance("montrous")
text2.concordance("montrous")


text2.similar("montrous")

text2.common_contexts(['monstrous', 'very'])
text4.dispersion_plot(['citizens', 'democracy', 'duties', 'America'])
text1.dispersion_plot(['happy', 'sad'])

text="You have to ask yourself one question: Do I feel lucky? Well do ya, punk?"
sents=sent_tokenize(text)
print(sents)


# In[ ]:

words=[word_tokenize(sent) for sent in sents]

customStopWords=set(stopwords.words('english')+list(punctuation))

wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)


text2="this is the end of the world as we know it, and I feel fine!!!."

st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text2)]
print(stemmedWords)

nltk.pos_tag(word_tokenize(text2))
