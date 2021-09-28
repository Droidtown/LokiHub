# from search_engine.doc_tfidf_search import doc_vectorizer
from numpy.lib.function_base import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import pandas as pd
import re
import numpy as np

class HippoChamber:
    
    def __init__(self, user_name = "", articut_key = "", loki_key = ""):
        """
        file_dir = ""   #預搜尋文本內容
        
        """
        self.user_name = user_name
        self.articut_key = articut_key
        self.loki_key = loki_key
        self.doc_vec = None
        self.documents = []
        self.source_doc = []
        self.vectorizer = None

        try:
            with open("./account.info", "r") as f:
                user_dict = json.loads(f.read())
            self.username = user_dict["email"]
            self.apikey = user_dict["apikey"]
        except:
            self.username = user_name
            self.apikey = articut_key

    
    def vectorize(self, dir_path = ""):
        try:
            with open("./dataset/ioh_sample.json") as f:
                content = json.load(f)
        except:
            print("error")
            with open(dir_path) as f:
                content = json.load(f)

        self.vectorizer = TfidfVectorizer()
        
#         print(content)

        for doc in content:
            try:
                source = doc['result_segmentation']
                sents = source
                sents = sents.replace("/", " ").replace("（", "").replace("／", "").replace("）", "").replace("」", "").replace("「", "")
                sents = re.sub(r'[0-9]', '', sents)
                self.documents.append(sents)
                ref = doc['ref']
                res = (doc['title'], ref)
                self.source_doc.append(res)
            except Exception as e:
                pass
        
        documents = self.documents

        X = self.vectorizer.fit_transform(documents).T.toarray()
        #print(X)
        df = pd.DataFrame(X, index=self.vectorizer.get_feature_names())
        #display(df)

        self.doc_vec = df

    def get_similar_articles(self, query = ""):
        q = [query]
        df = self.doc_vec
        q_vec = self.vectorizer.transform(q).toarray().reshape(df.shape[0],)
        sim = {}
        # Calculate the similarity
        lens = df.shape[1]
        for i in range(lens):
            sim[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)

        # Sort the values 
        sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
        return sim_sorted