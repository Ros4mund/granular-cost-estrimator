import gensim
from gensim.models import KeyedVectors

word2vec_model_path = r'C:\Users\Jiahe Zhang\Desktop\CLEO project\wordvector\wordvectors.kv' ##词向量文件的位置
word2vec_model = KeyedVectors.load_word2vec_format(word2vec_model_path, binary=False,unicode_errors='ignore')

word2vec_dict = {}
for word, vector in zip(word2vec_model.vocab, word2vec_model.vectors):
    if '.bin' not in word2vec_model_path:
        word2vec_dict[word] = vector
    else:
        word2vec_dict[word] = vector /np.linalg.norm(vector)
for each in word2vec_dict:
    print (each,word2vec_dict[each])
