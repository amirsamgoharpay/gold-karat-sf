#how much dust i need for gold making
print("possible karats : 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 20 , 22 , 24")
karatg = int(input("which karat do you want to make ? \n"))
gold = int(input("how much gold do you want to make? \n"))
if karatg%2 == 1 :
  print("i think this is a wrong number!")
 else :
  dust = ((karatg-2)//2)*gold
  print(f"you need {dust} gold dust")
