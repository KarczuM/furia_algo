dzien = ["wolne"]
for x in range(0, 33):
    dzien.append("wolne")
# samo odpalenie gry i zablokowanie budynku

czas_trwania_gry=3
optymalny_odstep=7
dzien[16] = "start"

#blokowanie czasu gry, chyba git:
for y in range(0, 33):
    if dzien[y] == "start":
        for z in range(y + 1, y + czas_trwania_gry):
            dzien[z] = "zajete"

# proponowanie gry od razu po zakonczeniu poprzedniej
#chujowe, bo nie liczy odstepu przed nastepna

# for y in range(0, 33):
#     if (dzien[y] == "zajete"):
#         if (dzien[y + 1] == "wolne"):
#             dzien[y + 1] = "proponowane"
#


#proponowanie gry ktora zmiesci sie PRZED nastepna
#juz nie wiem czy rekurencja potrzebna
def f1( x, list):
    for z in range(x, 0, -1):
            if ( list[z] !="wolne"):
                for y in range(z - 1, z - optymalny_odstep, -1):
                    if list[y] != "wolne" or y<0:
                        break
                    else:
                        if z - optymalny_odstep > 0 and z - optymalny_odstep < 33:
                            list[z - optymalny_odstep] = "proponowane"
                            f1(z - optymalny_odstep, list)


f1(33, dzien)

#proponowanie gier PO innych
#proponowanie gier PO innych
def f2(x, list):
    for z in range(x, 33):
            if ( list[z] !="wolne") :
                for y in range(z+1 , z + optymalny_odstep):
                    if list[y] != "wolne" or y>32:
                        break

                    else:
                        if z + optymalny_odstep > 0 and z + optymalny_odstep < 33:
                            list[z + optymalny_odstep] = "proponowane"
                            f2(z + optymalny_odstep, list)


f2(0, dzien)


#if z - 7 > 0 & z - 7 < 33:
   #             list[z - 7] = "proponowane"
   #             f1(z-7, list)




for x in range(0, 33):
    print 8 + 0.5 * x, dzien[x]
