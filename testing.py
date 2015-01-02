__author__ = 'Thomaz'
import python_linked_list


linkl = python_linked_list.LinkedList()
for i in xrange(0, 5):
    linkl.insert(i)
# linkl.append(5)
# linkl.insert(4)

print 'Linked List', linkl.get_all_raw()

# linkl.swap(0, 1)
linkl.bubble_sort()
# linkl.reverse()
print 'bubble sorted'

print 'Linked List', linkl.get_all_raw()