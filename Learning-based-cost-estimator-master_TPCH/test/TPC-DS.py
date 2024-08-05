import os
#去除文件夹data1g中的文件中每一列最后一行的 ‘|’
#讲去除后的内容写入文件夹 2data1g对应的文件中

for root in os.listdir(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\TPCDS_tbl'):
    print(root)
    f = open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\TPCDS_tbl'+ '\\' + root, 'r')
    w = open(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\TPCDS_tbl1'+ '\\' + root, 'w')
    for i in f:
        length = len(i) - 2
        if ('|' == i[length]):
            j = i[:length] + "\n"
            w.write(j)
    f.close()
    w.close()

