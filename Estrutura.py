from circularlist.dupla.DCircularList import DCircularList
from circularlist.dupla.DNode import DNode

total_pessoas = int(input("Insira o total de pessoas: "))
jump = int(input("Insira o intervalo entre tiros: "))

my_list = DCircularList()

for i in range(total_pessoas, 0, -1):
    my_list.add(DNode("Pessoa "+str(i)))

cont = 1
jump = jump - 1
my_list.advance()
print(str(my_list)+"\n")

while my_list.size > 1:
    if cont == jump:
        dead = my_list.remove()
        print(dead.element + " morreu...")
        cont = 0
    print(my_list)
    my_list.advance()
    cont = cont + 1

print("O sobrevivente foi: " + my_list.cursor.element)
