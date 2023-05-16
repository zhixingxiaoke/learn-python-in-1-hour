# def say_hello():
#     print("hello")
#
# say_hello()

# def say_hello_to(name="python"):
#     print("hello, {}".format(name))
#
# say_hello_to()
# say_hello_to("知行小课")

# def sum_num(num1, num2):
#     return num1 + num2
# print(sum_num(1, 2))
# print(sum_num(4, 5))

def sum_num(num1, num2):
    print("num1: {}, num2: {}".format(num1, num2))
    return num1 + num2

sum_num(1, 2)
sum_num(num2=1, num1=2)