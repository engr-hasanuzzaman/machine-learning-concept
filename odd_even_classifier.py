from sklearn.naive_bayes import GaussianNB

training_data = [[i, i] for i in range(1, 1000)]
training_label = ['even' if i[0] % 2 == 0 else 'odd' for i in training_data]
classifier = GaussianNB()
classifier.fit(training_data, training_label)
# print(training_label)
print(classifier.predict([[25, 25]]))