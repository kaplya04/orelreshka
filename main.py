import random #библиотека
pod = 0 # подбрасывает
orel = 0 # орёл
reshka = 0 # решка

while pod < 50: # подбрасывает много раз
    s = random.randint(0, 1) # 0 - орёл, 1 - решка
    pod += 1
    if s > 0:
        orel += 1
    elif s < 1:
        reshka += 1
print("Монета подброшена раз", pod)
print("Орел ", orel)
print("Решка", reshka)