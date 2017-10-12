import numpy as np
import pandas as pd
import cPickle as pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics


data = pd.read_csv('text.csv',names=["text","category"])


print (data.category.value_counts()/data.shape[0])*100

X =data.text
Y= data.category

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print X_train.shape
print X_test.shape
print Y_train.shape
print Y_test.shape



text_clf = Pipeline([('vect', CountVectorizer(stop_words='english',ngram_range=(1,1))),
                      ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
 ])







# text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
#                       ('tfidf', TfidfTransformer()),
#                      ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',
#                                            alpha=1e-3, n_iter=5, random_state=42)),
# ])





text_clf = text_clf.fit(X_train, Y_train)
predict = text_clf.predict(X_test)
print metrics.accuracy_score(Y_test, predict)



print metrics.classification_report(Y_test,predict,digits=2)