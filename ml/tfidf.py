import numpy as np
from collections import Counter


class TFIDF:
    def __init__(self):
        self.vocab = None
        self.idf = None

    def fit(self, documents):
        # documents: list[list[str]]
        words = sorted(set(
            word
            for doc in documents
            for word in doc
        ))

        self.vocab = {word: i for i, word in enumerate(words)}

        N = len(documents)
        V = len(self.vocab)

        df = np.zeros(V)

        for doc in documents:
            for word in set(doc):
                df[self.vocab[word]] += 1

        self.idf = np.log(N / df)

        return self

    def transform(self, documents):
        N = len(documents)
        V = len(self.vocab)

        tf = np.zeros((N, V))

        for i, doc in enumerate(documents):
            counts = Counter(doc)

            for word, count in counts.items():
                if word in self.vocab:
                    tf[i, self.vocab[word]] = count

        return tf * self.idf

    def fit_transform(self, documents):
        self.fit(documents)
        return self.transform(documents)