# Lug’atlar mavzusiga oid masalalar

# 1)  Mevalar lug’atini tuzing  va  kamida  5 ta qiymat bo’lsin
mevalar={
    "apple":"olma",
    "banana":"banan",
    "coconut":"cacos",
    "apilsin":"apilsin",
    "grapes":"orange"
}
# 2)  tuzgan  Lug’atingizdan eng katta qiymatni toping

eng_katta=max(mevalar)
print(eng_katta)

# 3 )  Tuzgan lug’atingizdagi elementlar sonini hisoblang

print(len(mevalar))

# For sikliga  mavzusiga oid masalalar
# 1) Masala: 1 dan 10 gacha bo'lgan sonlarni ekranga chiqaring.

son=list(range(1,11))
for son in son:
    print(son)

# 2)  Masala: 1 dan 10 gacha bo'lgan sonlarning kvadratlarini ekranga chiqaring.

son=list(range(1,11))
for son in son:
    print(son**2)


# 4) Masala: 1 dan 10 gacha bo'lgan sonlarning juftlarini ekranga chiqaring.


son=list(range(1,11))
for son in son:
    if son%2==0:
        print(son)


# 5)  Masala: 1 dan 10 gacha bo'lgan sonlarning toq sonlarini ekranga chiqaring.


son=list(range(1,11))
for son in son:
    if son%3==0:
        print(son)


# 6) Masala: 1 dan 10 gacha bo'lgan sonlarning kvadratlarini lug'atga joylashtiring.













