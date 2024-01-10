import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray', 'brown', 'aqua']
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-10)?", 5, 1, 10) )
for x in range(100):
    t.pencolor(colors[x%sides%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font=("Arial", int( (x*2 + 4) / 4), "bold") )
    t.left(360/sides+2)




















# class Solution:
#     # def twoSum(self, nums: List[int], target: int) -> List[int]:
#     def __init__(self):
#         pass
#     def twoSum(self):
#         n = input("Enter your number: ")
#         d = n.split(",")
#         l = []
#         target = 6
#         for i in range(len(d)):
#             l.append(int(d[i]))
#         print(l)
#         for j in range(1, len(l)):
#             if l[j-1] + l[j] == target:
#                 print([j-1, j])
# obj = Solution()
# obj.twoSum()