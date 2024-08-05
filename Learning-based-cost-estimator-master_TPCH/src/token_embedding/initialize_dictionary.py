import pickle
import re

from src.feature_extraction.database_loader import *




data = load_dataset(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\csv_file')
# print(data)
nation_tokens = []
for idx, row in data["nation"].iterrows():
    print(row['n_nationkey'])
    if idx % 100 == 0:
        print('nation', idx, '/', len(data["nation"]))
    sentence = []
    sentence.append('n_nationkey_' + str(row['n_nationkey']))
    n_name = str(row['n_name'])
    if len(n_name) > 0:
        sentence.append('n_name_' + n_name)

    sentence.append('n_regionkey_' + str(row['n_regionkey']))
    n_commnet = str(row['n_comment'])
    print(n_commnet)
    if len(n_commnet) > 0:
        sentence.append('n_comment_' + n_commnet)
    nation_tokens.append(sentence)
print('nation generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\nation.pkl', 'wb') as f:
    pickle.dump(nation_tokens, f)
print('nation')



customer_tokens = []
for idx, row in data["customer"].iterrows():
    if idx % 100 == 0:
        print('c_custkey', idx, '/', len(data["customer"]))
    sentence = []
    sentence.append('c_custkey_' + str(row['c_custkey']))
    c_name = str(row['c_name'])
    if len(c_name) > 0:
        sentence.append('c_name_' + c_name)
    c_address = str(row['c_address'])
    if len(c_address) > 0:
        sentence.append('c_address_' + c_address)
    sentence.append('c_nationkey_' + str(row['c_nationkey']))
    sentence.append('c_phone_' + str(row['c_phone']))
    sentence.append('c_acctbal_' + str(row['c_acctbal']))
    c_mktsegment = str(row['c_mktsegment'])
    if len(c_mktsegment) > 0:
        sentence.append('c_mktsegment_' + str(row['c_mktsegment']))
    c_comment = str(row['c_comment'])
    if len(c_comment) > 0:
        sentence.append('c_comment_' + str(row['c_comment']))
    customer_tokens.append(sentence)
print('customer generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\customer.pkl', 'wb') as f:
    pickle.dump(customer_tokens, f)
print('customer')


lineitem_tokens = []
for idx, row in data["lineitem"].iterrows():
    if idx % 100 == 0:
        print('lineitem', idx, '/', len(data["lineitem"]))
    sentence = []
    sentence.append('l_orderkey_' + str(row['l_orderkey']))
    sentence.append('l_partkey_' + str(row['l_partkey']))
    sentence.append('l_suppkey_' + str(row['l_suppkey']))
    sentence.append('l_linenumber_' + str(row['l_linenumber']))
    sentence.append('l_quantity_' + str(row['l_quantity']))
    sentence.append('l_extendedprice_' + str(row['l_extendedprice']))
    sentence.append('l_discount_' + str(row['l_discount']))
    sentence.append('l_tax_' + str(row['l_tax']))
    sentence.append('l_returnflag_' + str(row['l_returnflag']))
    sentence.append('l_linestatus_' + str(row['l_linestatus']))
    sentence.append('l_shipdate_' + str(row['l_shipdate']))
    sentence.append('l_commitdate_' + str(row['l_commitdate']))
    sentence.append('l_receiptdate_' + str(row['l_receiptdate']))
    sentence.append('l_shipinstruct_' + str(row['l_shipinstruct']))
    sentence.append('l_shipmode_' + str(row['l_shipmode']))
    sentence.append('l_comment_' + str(row['l_comment']))

    lineitem_tokens.append(sentence)
print('movie_link generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\lineitem.pkl', 'wb') as f:
    pickle.dump(lineitem_tokens, f)
print('movie_link')


orders_tokens = []
for idx, row in data['orders'].iterrows():
    if idx % 100 == 0:
        print('orders', idx, '/', len(data['orders']))
    sentence = []
    sentence.append('o_orderkey_' + str(row['o_orderkey']))
    sentence.append('o_custkey_' + str(row['o_custkey']))
    sentence.append('o_orderstatus_' + str(row['o_orderstatus']))
    sentence.append('o_totalprice_' + str(row['o_totalprice']))
    sentence.append('o_orderdate_' + str(row['o_orderdate']))
    sentence.append('o_orderpriority_' + str(row['o_orderpriority']))
    sentence.append('o_clerk_' + str(row['o_clerk']))
    sentence.append('o_shippriority_' + str(row['o_shippriority']))
    sentence.append('o_comment_' + str(row['o_comment']))

    orders_tokens.append(sentence)
print('orders generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\orders.pkl', 'wb') as f:
    pickle.dump(orders_tokens, f)
print('orders')


part_tokens = []
for idx, row in data["part"].iterrows():
    if idx % 100 == 0:
        print('part', idx, '/', len(data["part"]))
    sentence = []
    sentence.append('p_partkey_' + str(row['p_partkey']))
    sentence.append('p_name_' + str(row['p_name']))
    sentence.append('p_mfgr_' + str(row['p_mfgr']))
    sentence.append('p_brand_' + str(row['p_brand']))
    sentence.append('p_type_' + str(row['p_type']))
    sentence.append('p_size_' + str(row['p_size']))
    sentence.append('p_container_' + str(row['p_container']))
    sentence.append('p_retailprice_' + str(row['p_retailprice']))
    sentence.append('p_comment_' + str(row['p_comment']))
    part_tokens.append(sentence)
print('part generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\part.pkl', 'wb') as f:
    pickle.dump(part_tokens, f)
print('part')


partsupp_tokens = []
for idx, row in data["partsupp"].iterrows():
    if idx % 100 == 0:
        print('partsupp', idx, '/', len(data["partsupp"]))
    sentence = []
    sentence.append('ps_partkey_' + str(row['ps_partkey']))
    sentence.append('ps_suppkey_' + str(row['ps_suppkey']))
    sentence.append('ps_availqty_' + str(row['ps_availqty']))
    sentence.append('ps_supplycost_' + str(row['ps_supplycost']))
    sentence.append('ps_comment_' + str(row['ps_comment']))


    partsupp_tokens.append(sentence)
print('partsupp generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\partsupp.pkl', 'wb') as f:
    pickle.dump(partsupp_tokens, f)
print('partsupp')


region_tokens = []
for idx, row in data["region"].iterrows():
    if idx % 100 == 0:
        print('region', idx, '/', len(data["region"]))
    sentence = []
    sentence.append('r_regionkey_' + str(row['r_regionkey']))
    sentence.append('r_name_' + str(row['r_name']))
    sentence.append('r_comment_' + str(row['r_comment']))
    region_tokens.append(sentence)
print('region generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\region.pkl', 'wb') as f:
    pickle.dump(region_tokens, f)
print('region')

supplier_tokens = []
for idx, row in data["supplier"].iterrows():
    if idx % 100 == 0:
        print('supplier', idx, '/', len(data["supplier"]))
    sentence = []
    sentence.append('s_suppkey_' + str(row['s_suppkey']))
    sentence.append('s_name_' + str(row['s_name']))
    sentence.append('s_address_' + str(row['s_address']))
    sentence.append('s_nationkey_' + str(row['s_nationkey']))
    sentence.append('s_phone_' + str(row['s_phone']))
    sentence.append('s_acctbal_' + str(row['s_acctbal']))
    sentence.append('s_comment_' + str(row['s_comment']))

    supplier_tokens.append(sentence)
print('supplier generated')
with open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCH_table\string_words\supplier.pkl', 'wb') as f:
    pickle.dump(supplier_tokens, f)
print('supplier')

#

