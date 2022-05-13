from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
import pandas as pd
import time
import string
import nltk
##nltk.download('stopwords')


df = pd.read_csv("Nazariodataset.csv")

def remove_stopwords(Body):
    nopunch = [char for char in Body if char not in string.punctuation]
    nopunch = ''.join(nopunch)

    clean_word = [word for word in nopunch.split() if word.lower() not in stopwords.words('english')]

    return clean_word

#df = df['body'].apply(remove_stopwords)

#THis line convets a collection of text to a matrix

messages_bow = CountVectorizer(analyzer=remove_stopwords).fit_transform(df['body'])

#THis splits the date into 80% traing and rest being testing


X_train, X_test, y_train,y_test = train_test_split(messages_bow,df['body'],test_size=0.20, random_state=0)

#Get the shape of message

print (messages_bow.shape)


#creats and train the naive bayes classifcation modele

start = time.time()

classifier = MultinomialNB().fit(X_train, y_train)

stop = time.time()

# Print prediction
print("Classifier predict XTrain")
print(classifier.predict(X_train))

print("Train Values") 
print(y_train.values)

# Evaluate the model on the training data set

print(f"Training Time: {stop - start}s")
