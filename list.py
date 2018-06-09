a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
a1 = [100,200,300]
a2 = [25,35,45,65]

b1 = a[5] #mengkases list
b2 = a[:5] #memotong list
b3 = a[5:] #memotong list
b4 = a[5:10] 
b5 = a1+a2 #penjumlahan list
b6 = a1[:] #mengkopy list ke variable baru
b6[0] = 129 #merubah isi list
b6[1:2] = [11,12] #merubah isi list dengan slicing

c1 = [a1,a2] #multi dimensi list 
c2 = c1[0][2] #mengakses list multimensi [list pertama] [index list ke dari list pertama]
c3 = c1[0][:2] #mengakses list multimensi [list pertama] [index list ke dari list pertama]

#method list
d1 = a1[:]
d1.append(999)

#fungsi list
d2 =  len(a1)

print (b1) 
print (b2)
print (b3)
print (b4)
print (b5)
print (b6)
print (a1) #nilai a1 tetap
print (b6)

print (c1)
print (c2)
print (c3)
print (d1)
print (d2)