

a = 'abc'

b = 'cde'

dic1 = {}

dic2 = {}

for i in a:

    dic1[i]=a.count(i)

for j in b:

    dic2[j]=b.count(j)


#letras que estan en las dos palabras pero que pueden tener distinta frecuencia
a_b_sobran = sum([abs(dic1[i]-dic2[i]) for i in dic1.keys() if i in dic2.keys()])

#letras que estan en una palabra pero que no estan en la otra
sobra_a = len([i for i in a if i not in b])
sobra_b = len([i for i in b if i not in a])


resultado_final_sobran = a_b_sobran + sobra_a + sobra_b

print(resultado_final_sobran)

