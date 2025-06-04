# numeros= int([1,65,1,1,16,5,6,8,6,4])
# temporal = []

# for i in numeros: 
#      if i> len(numeros[i]):
#          temporal.append(i)
         
# print(temporal)

# num=(1, 65, 1, 32, 16, 5, 6, 8, 6, 4)
# numeros_lideres = []
# for i in range(1,len(num)):
#     if num[i-1]<num[i]:
#         numeros_lideres.append(num[i])
# print(numeros_lideres)


num = [1, 65, 1, 32, 16, 5, 6, 8, 6, 4]
num_lideres = []
for i in range(len(num) ):
    es_lider = True 
    for j in range(i + 1, len(num)):
        if num[j] > num[i]:
            es_lider = False
    if es_lider== True:
        num_lideres.append(num[i])
num_lideres.append(num[-1])
print(num_lideres)
