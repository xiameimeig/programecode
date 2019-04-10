class MyIterator:
    def __init__(self,items):
        self.items = items
        self.current_index = 0

    def __iter__(self):
        '''iter()'''
        pass

    def __next__(self):
        '''next（）'''
        """在当前的方法里面，实现记录位置和值"""
        if self.current_index <len(self.items):
            value = self.items[self.current_index] # list_new[2]
            self.current_index += 1
            return value
        else:
            raise  StopIteration

iter()
next()