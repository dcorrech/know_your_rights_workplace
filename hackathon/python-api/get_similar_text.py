from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
from nltk.data import find
import nltk
import numpy as np
import pandas as pd
import csv
import gensim

nltk.download("word2vec_sample")
nltk.download('stopwords')
nltk.download('punkt')


word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)


class get_most_similar_text():
    def __init__(self, input_csv, input_user_id, stopwords = stopwords, word2vec_model = word2vec_model):
        self.input_csv = input_csv
        input_df = pd.read_csv(input_csv) #'KYR_data.csv'
        self.archive_df = input_df[input_df["Unique ID"] != input_user_id] 
        self.input_text = input_df[input_df["Unique ID"] == input_user_id].loc[:,"Details"][0]
        keys = self.archive_df['Unique ID'].iloc[1:] # this needs to be diff dor diff input_user
        vals = self.archive_df['Details'].iloc[1:]# this needs to be diff dor diff input_user
        self.archive_dict  =  dict(zip(keys, vals))
        self.stopwords = set(stopwords.words('english')) 
        self.word2vec_model = word2vec_model

    def preprocess(self, text):
        '''tokenize text into list of lists, sents and words, remove stopwords'''
        sents = sent_tokenize(text)
        result = []
        for sent in sents:
            word_tokenized = word_tokenize(sent)
            result.append([w for w in word_tokenized if not w in self.stopwords] )
        return result

    def get_text_embedding(self, sents): # k = len(sents)
        
        ''' returns an word embeddings of len(sents), produced by summing the embeddings of words 
        in each sentences
        ---------------------
        sents - list, word tokenized
        word_vectors - word2vec model'''
        
        sents_vec = [] #one embedding per sentence
        for sent in sents:
            sent_vec = []
            for word in sent:
                if word in self.word2vec_model:
                    word_vec = self.word2vec_model.wv[word]
                    sent_vec.append(word_vec) # add each word embedding per sent
            sents_vec.append(np.sum(sent_vec, axis = 0)) # sum over columns
    
        result = np.sum(sents_vec, axis = 0)
        
        return result.flatten()

    def get_tokenized_docs(self):
        ''' Given all documented user cases dict, return dict of doc_id to word-tokenized sents
        ------------
        all_inputs_archive: dictionary where key = user_id, value = raw text'''
        result = dict()
        for doc, text in self.archive_dict.items():
            if(type(text)) == str:
                result[doc] = self.preprocess(text)
        return result

    def get_similarities(self, input_text_vec, archive_processed):
        ''' Takes in embedding of input text (dense matrix) and preprocessed dictionary of user_id: tokenized_text.
        Returns dictionary of cosine similaries where key is user_id, output is cosine similarity between archive text and input text'''
        text_similarities = dict()
        for usr_id, text in archive_processed.items():
            text_vec = self.get_text_embedding(text)
            text_similarities[usr_id] = 1 - cosine(input_text_vec, text_vec)
        return text_similarities


    def output_most_similar_text(self, similarities_dict):
        '''Given dictionary mapping similarities to cosine_similarity
        and data frame of full archive text, return csv file with original fields and similarity for most similar text.
        -------------------
        similarities_dict: dict, user_id:cos_similarity
        archive_df: pandas DataFrame of archive data'''
        max_sim = 0
        best_usr = ""
        for key, val in similarities_dict.items():
            if val > max_sim:
                max_sim = val
                best_usr = key
        result = self.archive_df[self.archive_df["Unique ID"] == best_usr]
        result["similarity"] = max_sim
        
        return result.to_csv(r'./results.csv')
    
    def forward(self):
        sents_input = self.preprocess(self.input_text)
        input_vec = self.get_text_embedding(sents_input)
        archive_processed = self.get_tokenized_docs()
        similarities_dict = self.get_similarities(input_text_vec=input_vec, archive_processed=archive_processed)
        return self.output_most_similar_text(similarities_dict)
