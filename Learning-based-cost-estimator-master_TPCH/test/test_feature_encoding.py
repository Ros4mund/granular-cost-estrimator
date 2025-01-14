import unittest

from src.feature_extraction.database_loader import *
from src.training.train_and_test import *
from src.internal_parameters import *

class TestFeatureEncoding(unittest.TestCase):
    def test(self):
        # dataset = load_dataset('/home/sunji/cost_estimation/test_files_open_source/imdb_data_csv')
        dataset = load_dataset(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\csv_file')
        column2pos, indexes_id, tables_id, columns_id, physic_ops_id, compare_ops_id, bool_ops_id, table_names = prepare_dataset(dataset)
        # print('column id: ',columns_id)
        # print(column2pos)
        print ('data prepared')
        word_vectors = load_dictionary(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\wordvector\wordvectors.kv')
        print ('word_vectors loaded')
        # min_max_column = load_numeric_min_max('/home/sunji/cost_estimation/test_files_open_source/min_max_vals.json')
        # print ('min_max loaded')

        index_total_num = len(indexes_id)
        table_total_num = len(tables_id)
        column_total_num = len(columns_id)
        physic_op_total_num = len(physic_ops_id)
        compare_ops_total_num = len(compare_ops_id)
        bool_ops_total_num = len(bool_ops_id)
        condition_op_dim = bool_ops_total_num + compare_ops_total_num+column_total_num+1000

        plan_node_max_num, condition_max_num, cost_label_min, cost_label_max, card_label_min, card_label_max = obtain_upper_bound_query_size(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH\query_output1.json')
        plan_node_max_num_test, condition_max_num_test, cost_label_min_test, cost_label_max_test, card_label_min_test, card_label_max_test = obtain_upper_bound_query_size(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH\query_output1.json')
        cost_label_min = min(cost_label_min, cost_label_min_test)
        cost_label_max = max(cost_label_max, cost_label_max_test)
        card_label_min = min(card_label_min, card_label_min_test)
        card_label_max = max(card_label_max, card_label_max_test)
        print ('query upper size prepared')

        parameters = Parameters(condition_max_num, indexes_id, tables_id, columns_id, physic_ops_id, column_total_num,
                                table_total_num, index_total_num, physic_op_total_num, condition_op_dim, compare_ops_id, bool_ops_id,
                                bool_ops_total_num, compare_ops_total_num, dataset, word_vectors, cost_label_min,
                                cost_label_max, card_label_min, card_label_max)

        # print(parameters.columns_id)
        encode_train_plan_seq_save(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH\queryoutput.json', parameters, batch_size=8, directory=r'C:\Users\Jiahe Zhang\Desktop\CLEO project\encoding_output')

if __name__ == '__main__':
    unittest.main()