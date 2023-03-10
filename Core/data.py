from functools import reduce

class Spreadsheet():
    slots = '__data', '__rowsCount', '__columnsCount'
    def __init__(self, data = None):
        self.__data = data or [['']]
        self.__rowsCount = len(self.__data)
        maxColumns = 0
        if self.__rowsCount > 0:
            maxColumns = len(self.__data[0])
        self.__columnsCount = maxColumns
        for row in self.__data:
            for _ in range(len(row), maxColumns):
                row.append('')
    
    # rows
    @property
    def rows(self):
        return self.__data
    
    @property
    def rowsCount(self):
        return self.__rowsCount

    def insertRow(self, index: int, data = None):
        self.__data.insert(index, data or [''] * self.__columnsCount)
        self.__rowsCount += 1
    
    def appendRow(self, data = None):
        self.__data.append(data or [''] * self.__columnsCount)
        self.__rowsCount += 1
    
    def removeRow(self, index: int):
        self.__data.pop(index)
        self.__rowsCount -= 1
    
    # columns
    @property
    def columns(self):
        return list(zip(*self.__data))
    
    @property
    def columnsCount(self):
        return self.__columnsCount
    
    def insertColumn(self, index: int, data = ''):
        for row in self.__data:
            row.insert(index, data)
        self.__columnsCount += 1
    
    def appendColumn(self, data = ''):
        for row in self.__data:
            row.append(data)
        self.__columnsCount += 1
    
    def removeColumn(self, index: int):
        for row in self.__data:
            row.pop(index)
        self.__columnsCount -= 1

    # indexer
    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self.__data[key[0]][key[1]]
        return self.__data[key]
    
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            self.__data[key[0]][key[1]] = value
        else:
            self.__data[key] = value

    def __delitem__(self):
        print("Deleting keys is not allowed on Spreadsheet type. Use RemoveRow/Column instead.")
        pass
    
    @staticmethod
    def from_csv(file, sep=',', encoding='utf-8') -> 'Spreadsheet':
        data = []
        with open(file, encoding = encoding) as f:
            for line in f:
                data.append(line.removesuffix('\n').split(sep))
        return Spreadsheet(data)
    
    def to_csv(self, file, sep=',', encoding='utf-8'):
        with open(file, mode = 'w', encoding = encoding) as f:
            for row in self.__data:
                f.write(sep.join(map(lambda value: str(value), row)))
