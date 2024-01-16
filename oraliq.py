# Lugatlar ga oid masala yechish

#1
meva={
      "olma":"olma",
      "olcha":"olcha",
      "nok":"nok",
      "banan":"banan",
      "uzum":"uzum"
      }



print(max(meva))


print(len(meva))


# For sikliga  mavzusiga oid masalalar


son=list(range(1,11))
for son in son:
    print(son)



son=list(range(1,11))
for son in son:
    print(son**2)





son=list(range(1,11))
for son in son:
    if son%2==0:
        print(son)



son=list(range(1,11))
for son in son:
    if son%3==0:
        print(son)






son = [4, 2, 9, 5, 1, 7]
for son in son:
    if son==[4,2,9,5,1,7]:
        print(sum(son))




son = [3, 6, 2, 9, 5]
for son in son:
    if son*2:
        print(son)



#Funksiya mavzusiga oid masalalar

#1
def matn(matn):
    """matin qabul qilib teskariga o'girib beradi"""
    teskarisi=matn[::-1]
    print(teskarisi)


matn("ramiz")

#2
def maxim(kat):
    """ sonni qabul qilib eng katta elementni chiqaradi """
    katta=kat(max(kat))
    print(katta)

kat=[1,5,7,4,9,10]


#3

def juft(son):
    """ sonni qabul qilib uni faqat juft qibib beradigan funksiya"""
    if son%3==0:
        print(son)

    juft=[1,5,4,7,9,5]


#4
def text(matn):
    """ bu funksiya matn ni olib"""
    uzun=matn(max(matn))
    print(uzun)

matn("ramiz")



#String float va integer tipiga oid  masalalar

#1
matn=input("Biror matn kiriting::")
def teskari(matn):
    teskarisi=matn[::-1]
    print(teskarisi)

teskari('python')


#List  mavzusiga oid masalalar

#1
son = [5, 2, 8, 1, 9]
print(son[::-1])

#2
son = [3, 6, 2, 1, 7, 9]
uzunlik=len(son)
yigindi=sum(son)
print(yigindi/uzunlik)



#3
son = [4, 2, 7, 5, 9]
print(sum(son))


#4
son = [3, 8, 2, 6, 1, 9]
print(max(son))
print(min(son))



sonlar = [1, 5, 2, 8, 3, 7]
if son%2==0:
    print(son)

#7
son = [5, 3, 9, 1, 7]
print(son[::-1])

#8
son = [2, 7, 4, 9, 6, 1]
print(son.insert(0,4))