#primero mi manera

def es_anagrama (palabra1 , palabra2):
    if (palabra1 == palabra2):
        return False
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

#version mas facil
def es_anagrama1 (p1 , p2):
    return p1 != p2 and sorted(p1.lower()) == sorted(p2.lower())

print(es_anagrama("marte" , "EtraM"))
print(es_anagrama1("ana","naa"))