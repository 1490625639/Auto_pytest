import xlrd


def read_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    sheet = workbook.sheet_by_index(0)  # 假设数据在第一个工作表中

    data = []
    for row_index in range(sheet.nrows):
        row_data = sheet.row_values(row_index)
        # 将行首信息和其后的内容进行拼接，使用 ":" 分隔
        combined_data = "{}:{}".format(row_data[0], "".join(str(i) for i in row_data[1:]))
        data.append(combined_data)

    return data


if __name__ == '__main__':
    excel_file = "./testdata.xls"
    result = read_excel(excel_file)
    print(result)
