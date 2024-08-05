import unittest
from src.feature_extraction.extract_features import *
from src.training.train_and_test import *
import torch
class TestFeatureExtraction(unittest.TestCase):
    def test(self):
        dataset = load_dataset(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\csv_file')
        print(dataset)
        print(dataset['item'].keys())
        column2pos, indexes_id, tables_id, columns_id, physic_ops_id, compare_ops_id, bool_ops_id, table_names = prepare_dataset(dataset)
        print('column2pos: ', column2pos)
        print('indexes_id: ', indexes_id)
        print('tables_id: ', tables_id)
        print('columns_id: ', columns_id)
        print('physic_ops_id: ', physic_ops_id)

        # sample_num = 1000
        # sample = prepare_samples(dataset, sample_num, table_names)
        # print(sample)
        feature_extractor(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\queryplan1.json', r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\query_output1.json')
        # add_sample_bitmap('/home/sunji/cost_estimation/test_files_open_source/plans_seq.json', '/home/sunji/cost_estimation/test_files_open_source/plans_seq_sample.json', dataset, sample, sample_num)

if __name__ == '__main__':
    unittest.main()