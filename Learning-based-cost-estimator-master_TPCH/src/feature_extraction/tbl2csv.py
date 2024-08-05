import pandas as pd
def converttbldatatocsvformat(filename, header):
    csv = open("".join([r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\csv_file\\', filename, ".csv"]), "w+")
    csv.write(header + "\n")
    tbl = open("".join([r'C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\tbl_file\\', filename, ".tbl"]), "r")
    lines = tbl.readlines()
    for line in lines:
        length = len(line)
        line = line[:length - 2] + line[length - 1:]
        line = line.replace(",", "N")
        line = line.replace("|", ",")
        csv.write(line)
    tbl.close()
    csv.close()
def deletecolumns():
    file = r"C:\Users\Jiahe Zhang\Desktop\CLEO project\TPCDS\csv_file\inventory.csv"

    keyword = 0

    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if line.strip("\n") != keyword:
                f.write(line)


if __name__ == '__main__':
    converttbldatatocsvformat('inventory', "")
    # deletecolumns()