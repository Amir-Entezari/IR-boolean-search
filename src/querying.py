class QueryProcessor:
    """
    In this class, I implement an information retrieval system which can search a query among documents.
    ...
    Attributes:
    -----------
    indexing_model: InvertedIndex
        an instance of InvertedIndex class which has been created by indexing documents.
    Methods
    -------
    Methods defined here:
        get_word_docs(self, word: str):
                this simple function gets a token and will return all index of documents that this token is appeared in.
                :param word:
                    a word that you want to search.
                :return:
                    list of indexes of documents.
        intersect(self, first_word, second_word):
                this function get two words, and find documents that both of these word has been occurred.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            union(self, first_word, second_word):
                this function get two words, and find documents that either each of these word has been occurred.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            not_in(self, word):
                this function get one word, and find documents that this word has been not occurred.
                :parameter
                word: str
                    the word you want to search
                :return
                    list of indexes of documents.
            near(self, first_word, second_word, length):
                this function get two words, and find documents that either each of these word has been occurred near by at most 3 words on left or right.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            search(self, query):
                this function get a query and recognize what kind of query is; then search the query.
                :parameter
                    query: str
                        the query that user wants to search
                :return
                    print list of indexes of documents in a pretty way.
    """
    def __init__(self, indexing_model):
        self.indexing_model = indexing_model

    def get_word_docs(self, word):
        t = self.indexing_model.get_token(word)
        result = set()
        for doc in t.docs:
            result.add(doc['doc_idx'])
        return result

    def intersect(self, first_word, second_word):
        docs1 = self.get_word_docs(first_word)
        docs2 = self.get_word_docs(second_word)
        return list(docs1 & docs2)

    def union(self, first_word, second_word):
        docs1 = self.get_word_docs(first_word)
        docs2 = self.get_word_docs(second_word)
        return list(docs1 | docs2)

    def not_in(self, word):
        all_docs = set(range(len(self.indexing_model.documents)))
        word_docs = self.get_word_docs(word)
        return list(all_docs - word_docs)

    def near(self, first_word, second_word, distance):
        result = set()
        t1 = self.indexing_model.get_token(first_word)
        t2 = self.indexing_model.get_token(second_word)
        for t in (t1, t2):
            for doc in t.docs:
                for idx in doc['indexes']:
                    if second_word in self.indexing_model.documents[doc["doc_idx"]][idx + 1:idx + 1 + distance]:
                        result.add(doc['doc_idx'])
        return list(result)

    def search(self, query):
        query_parts = query.lower().split()
        if 'and' in query_parts:
            return self.intersect(query_parts[0], query_parts[2])
        elif 'or' in query_parts:
            return self.union(query_parts[0], query_parts[2])
        elif 'not' in query_parts:
            return self.not_in(query_parts[1])
        elif 'near' in query:
            distance = int(query_parts[1].split('/')[1])
            return self.near(query_parts[0], query_parts[2], distance)
        else:
            return list(self.get_word_docs(query_parts[0]))