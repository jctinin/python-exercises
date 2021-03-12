s1 = {1, 2, 3, 4, 5}  # não tem índice, mas podemos iterar

s2 = set()  # também pode retirar elementos duplicados

s2.add(("Julio"))

s2.update([1, 2, 3, 4, 5], {5, 6, 7, 8}, "Diego")

print(s2)

s2 = list(s2)

print(s2[-1])


s3 = {
    1,
    2,
    3,
    4,
    5,
    6,
    25
}
s4 = {
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    12
}
s5 = s3 | s4  # função union
s6 = s3 & s4  #  função intersection
s7 = s4 - s3  # difference - sempre o primeiro pelo segundo
s8 = (
    s3 ^ s4
)  # synmetric_difference ^ (elementos estão nos 2 sets, mas não em ambos)


print(s5)
print(s6)
print(s7)
print(s8)
