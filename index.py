""" 
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""
def flattenListGenerator(lists_of_lists):
    if type(lists_of_lists) is list:
        for i in lists_of_lists:
            yield from flattenListGenerator(i)
    else:
        yield lists_of_lists

def flatten(lists_of_lists):
    return list(flattenListGenerator(lists_of_lists))

# print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
def reverseLists(lists):
    return [(reverseLists(x) if isinstance(x, list) else x)
                             for x in reversed(lists)]


arr1 = reverseLists([[1, 2], [3, 4], [5, 6, 7]])
print(arr1)