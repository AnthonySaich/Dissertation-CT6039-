from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.ensemble import RandomForestClassifier
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

# Convert a collection of text to a matrix
messages_bow = CountVectorizer(analyzer=remove_stopwords).fit_transform(df['body'])

#spilt the data into 80% training and the rest being testing

X_train, X_test, y_train,y_test = train_test_split(messages_bow,df["body"],test_size=0.20, random_state=0)


#creating random forest

clf = RandomForestClassifier(n_estimators=1000)
start = time.time()
clf.fit(X_train, y_train)
stop = time.time()

y_pred = clf.predict(X_test)

# Model Accuracy
print (f"Traning Time: {stop-start}s")
