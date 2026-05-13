Grade = [5, 5, 5]

def average(Grade):

    shuma = 0

    for nota in Grade:
        shuma = shuma + nota

    mesatarja = shuma / len(Grade)

    return mesatarja


rezultati = average(Grade)

print("Nota mesatare eshte:", rezultati)