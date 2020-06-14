a = input('Cell 1 coordinates: ')
b = input()
print(a, b)
c = input('Cell 2 coordinates: ')
d = input()
print(c, d)
x1 = int(a + b)
x2 = int(c + d)

#Король

#if x1 - x2 > 2:
    #print('NO')
#elif x1 - x2 < -2:
   # print('NO') 
#else:
     #print('YES')    


#ладья

#if a == c or b == d:
 #   print('YES')   
#else:
  #  print('NO') 
# ферзь

if a == c or b == d:
    print('YES')
elif x1 == x2:
    print('YES')       
else:
    print('NO') 









