import nltk
import string
from typing import List


class Token:
    def __init__(self, word: str):
        self.word = word
        self.docs = []

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.word


class InvertedIndex:
    """
    In this class, I implement an information retrieval system which can search a query among documents.
    ...
    Attributes:
    -----------
    documents: List
        list of documents in format of string.
    posting_list: List[Token]
        list of Token objects. Tokens store a string and document's indexes
    stop_word: set
        set of stop words to check when tokenizing
    case_sensitive: bool
        a boolean to determine whether we want to distinguish between lowercase and uppercase form.

    Methods
    -------
    Methods defined here:
        __init__(self, documents: List, case_sensitive=False):
            Constructor will set initial attributes like documents and case_sensitive. NOTE that documents should be
            list of strings at first.
            :parameter
            ---------
            documents:List
                list of strings at first. but then chagnes to list of lists of strings
            :return
                None
        add_document(self, doc_idx, doc):
            this function will add a document to the posting list. it will loop over all tokens in the document and
            add them to the posting list.
            :param doc_idx:
                index of the document in the documents list
            :param doc:
                list of tokens in the document
            :return:
                None
        create_posting_list(self):
            calling this function, will create posting list of all occurred words cross all documents.
            :parameter
                None
            :return
                None
        get_token_index(self, x):
            this function find index of a word in posting list using binary search algorithm.
            :parameter
                x:str
                    the word you want to find its index
            :return
                int: index of the word in posting_list
        get_token(self, token):
                This function will return the token object that contains docs informations. if the given token is not in the
                posting_list, it return the spell corrected token.
                :param token:
                    token you want to fetch it from posting list
                :return:
                    return the instance of token from posting list
    """

    def __init__(self, documents: List, case_sensitive=False):
        """
        Constructor will set initial attributes like documents and case_sensitive. NOTE that documents should be
            list of strings at first.
            :parameter
            ---------
            documents:List
                list of strings at first. but then chagnes to list of lists of strings
            :return
                None
        """
        self.documents = documents
        self.posting_list: List[Token] = []
        self.stop_words: set = set(nltk.corpus.stopwords.words('english') + list(string.punctuation))
        self.case_sensitive = case_sensitive


    def add_document(self, doc_idx, doc):
        for token_idx, token in enumerate(doc):
            if len(self.posting_list) == 0:
                self.posting_list.append(Token(token))
                self.posting_list[0].docs.append({'doc_idx': doc_idx, 'indexes': [token_idx]})
                continue
            i = 0
            while i < len(self.posting_list) and token > self.posting_list[i].word:
                i += 1
            if i == len(self.posting_list):
                self.posting_list.append(Token(token))
                # self.posting_list[i].post_idx.append(post_idx)
            elif token != self.posting_list[i].word:
                self.posting_list.insert(i, Token(token))

            if doc_idx not in [elem['doc_idx'] for elem in self.posting_list[i].docs]:
                self.posting_list[i].docs.append({'doc_idx': doc_idx, 'indexes': [token_idx]})
            else:
                self.posting_list[i].docs[-1]['indexes'].append(token_idx)

    def create_posting_list(self):
        """
        calling this function, will create posting list of all occurred words cross all documents. in this function, we
        loop over all documents, then inside this loop, we loop over all the tokens that are in the current document.
        the we check if the length of posting_list is zero, then we add this token as first word. else if the length of
        posting_list is more than 0, we find the correct index of the token in posting_list alphabetically. then we check
        if this token, has been already in posting_list, we just add the current document index in tokens.docs, else, we
        add this token in the posting_list, then add the current document index.
            :parameter
                None
            :return
                None
        :return:
        """
        for doc_idx, doc in enumerate(self.documents):
            self.add_document(doc_idx=doc_idx, doc=doc)

    def get_token_index(self, x):
        """
        this function find index of a word in posting list using binary search algorithm.
            :parameter
                x:str
                    the word you want to find its index
            :return
                int: index of the word in posting_list
        """
        low = 0
        high = len(self.posting_list) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.posting_list[mid].word < x:
                low = mid + 1
            elif self.posting_list[mid].word > x:
                high = mid - 1
            else:
                return mid
        return -1

    def get_token(self, token):
        """
        This function will return the token object that contains docs informations. if the given token is not in the
        posting_list, it return the spell corrected token.
        :param token:
            token you want to fetch it from posting list
        :return:
            return the instance of token from posting list
        """
        p = self.get_token_index(token)
        if p == -1:
            null_token = Token('token')
            null_token.docs = []
            return null_token
        return self.posting_list[p]





nltk.download('punkt')
nltk.download('stopwords')
