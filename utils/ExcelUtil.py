import os

import xlrd


# 自定义异常
class SheetTypeError:
    pass


class ExcelReader:
    # 1 验证

    def __init__(self, excel_file, sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在")

        # 2 读取方式
    def  data(self):
        # 如果存在self_data不读取
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [int, str]:
                raise SheetTypeError("请输入int或者str类型")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)
            # 3 读取内容
            # 获取首行信息
            title = sheet.row_values(0)
            # 遍历，过滤首行
            for col in range(1, sheet.nrows):
                # 拼接，与首行拼接成字典， 放在list中  使用zip函数：可以做到前半部分，后半部分用append方法添加进list中
                col_value = sheet.row_values(col)
                self._data.append(dict(zip(title, col_value)))
        return self._data


if __name__ == '__main__':
    reader = ExcelReader("../data/testdata.xlsx", "美多商城接口测试")
    print(reader.data())
