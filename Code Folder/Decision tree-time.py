from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from sklearn import metrics
import time
import pandas as pd

df = pd.read_csv('Nazariodataset.csv')

def remove_stopwords(Body):
    nopunch = [char for char in Body if char not in string.punctuation]
    nopunch = ''.join(nopunch)
    clean_words = [word for word in nopunch.split() if word.lower() not in stopwords.words('english')]

    return clean_words


# Convert a collection of text to a matrix of tokens
messages_bow = CountVectorizer(analyzer=remove_stopwords).fit_transform(df['body'])

#Split the data into 80% traning and the rest being testing


X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['body'] ,test_size=0.20, random_state=0)



#creating the descsion tree classififer

clf = DecisionTreeClassifier()

start = time.time()
clf.fit(X_train, y_train)
stop = time.time()


y_pred = clf.predict(X_test)


#Model accuary


print(f"Training Time: {stop-start}s")
