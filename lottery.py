from random import choices

loterry = ['8','20','15','22','7','96','42','5','88','33','S','M','K','G','T']
winner = choices(loterry, k=4)
print(f"la persona que tenga este numero de loteria {winner} es el ganador")