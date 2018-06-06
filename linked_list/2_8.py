from one_way_linked_list import *
import doctest
from collections import defaultdict

def loop():
    a, b, c, d, e = [ Node(i) for i in ['a', 'b', 'c', 'd', 'e']]
    list = LinkedList([])
    for i in [a,b,c,d,e,b]:
        list.push(i)
    slow = list.head
    fast = list.head
    # /*Находим первую точку встречи LOOP_SIZE-k шагов по связному списку.*/
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

	# /* Ошибка - нет точки встречи, следовательно, нет петли */
    if not fast or not fast.next:
        return False

    #  Перемещаем медленный бегунок в начало списка (Head). Быстрый остается
    # в точке встречи.
    # *Каждые k шагов от Loop Start. Если указатели продолжат
    # движение с той же скоростью, то
    # встретятся в точке Loop Start
    slow = list.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast.data

print(loop())
