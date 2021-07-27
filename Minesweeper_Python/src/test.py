# w = [[-5 for i in range(8)] for j in range(8)]
# print(w[0][0])
# w[0][1] = 2
# print(w[0][1])
# def PowerSetsRecursive(items):
#   subsets = []
#   first_elt = items[0] #first element
#   rest_list = items[1:] 
#   for partial_sebset in PowerSetsRecursive(rest_list):
#     subsets.append(partial_sebset)
#     next_subset = partial_sebset[:] +[first_elt]
#     subsets.append(next_subset)
#   return subsets

# def PowerSetsRecursive2(items):
#   result = [[]]
#   for x in items:
#     result.extend([subset + [x] for subset in result])
#   return result

# i = PowerSetsRecursive2([x for x in range(25)])
# print(i)
i = 5
g = 5/3
a = 5/3
b = 5/3
c = 5/3
x = g*3
f = a+b+c
print(g,x,f)
