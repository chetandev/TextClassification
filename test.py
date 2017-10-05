# import numpy as np
# import pandas as pd
# import cPickle as pickle
# import os
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import Pipeline
# from sklearn.linear_model import SGDClassifier
#
#
#
# data = pd.read_csv('text.csv',names=["text","category"])
#
# print data.category.value_counts()
#
#
#
#
#
# numpy_array = data.as_matrix()
# X = numpy_array[:, 0]
# Y = numpy_array[:, 1]
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
#
# count_vect = CountVectorizer()
#
# X_train_counts = count_vect.fit_transform(X_train)
#
# # print X_train_counts.toarray()
# # print pd.DataFrame(X_train_counts.toarray(),columns=count_vect.get_feature_names())
#
#
#

from logger import logger;

obj = {"userid":"512","devicekey":"4343","hash":'djfhdjfnj'}

logger.info('just testing',extra=obj)