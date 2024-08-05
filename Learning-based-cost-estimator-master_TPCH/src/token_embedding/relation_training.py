import logging  # Setting up the loggings to monitor gensim
import multiprocessing
import pickle
from time import time  # To time our operations

from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile

logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s", datefmt='%H:%M:%S', level=logging.INFO)
sentences = []

for path in ['customer.pkl', 'lineitem.pkl', 'nation.pkl', 'orders.pkl', 'part.pkl',
             'partsupp.pkl', 'region.pkl', 'supplier.pkl']:
    print(path)
    with open(r'C:/Users/Jiahe Zhang/Desktop/CLEO project/TPCH_table/string_words/'+path, 'rb') as f:
        content = f.read()
        sentences += pickle.loads(content)
        # print(sentences)
print('Token loading completely!')

cores = multiprocessing.cpu_count()
w2v_model = Word2Vec(min_count=1,
                     window=5,
                     vector_size=500)



t = time()
w2v_model.build_vocab(sentences, progress_per=10000)
print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

t = time()
w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))

w2v_model.save("word2vec.model")
print('model saved')

path = get_tmpfile("wordvectors.kv")
w2v_model.wv.save(path)
print('word saved')
'''
model.build_vocab(new_sentences, update=True)
model.train(new_sentences)
'''
