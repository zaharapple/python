spisok1=["asd", "gff", "trujyu", "hrjjuye"]
spisok2=["ASD", "UIO", "RDTYCG", "JFHYWFAS"]
def lower(num1):
    num1=num1.lower()
    return num1

def upper(num1):
    num1=num1.upper()
    return num1

new_map=list(map(upper, spisok1))
new_map2=list(map(lower, spisok2))

print(new_map)
print(new_map2)


