#
# class Stack:
#     def __init__(self):
#         self.list =[]
#
#
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return  "\n".join(values)
#
#
# # isEmpty
#
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#
# # push
#
#     def push(self,value):
#         s = self.list.append(value)
#         return "Value inserted successfully"
# # pop
#
#     def pop(self):
#         if self.isEmpty():
#             return 'list is empty'
#         else:
#             self.list.pop()
#             return 'value has been removed'
# #peek
#
#     def peek(self):
#         if self.isEmpty():
#             return 'list is empty'
#         else:
#             n = self.list[len(self.list)-1]
#             return n
#
# #delete
#
#     def delete(self):
#         self.list = None
#         return 'successfully deleted'
#
#
# v= Stack()
# #print(v.isEmpty())
# v.push(1)
# v.push(2)
# v.push(3)
#
# v.peek()
# v.pop()
# v.pop()
# print(v)
# v.delete()
#
# print(v.delete())

# print(v)
# s="vivek"
# f='graphic'
# print(s[0])
# conc= s+" "+f[1:7]
# print(conc)
# v= s.replace('v','o')
# print(v)

v='Graphic Era  '

print(v*4)
