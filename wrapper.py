# # L = [1, 2, 2, 7,6,8,7,9]
# # # def Mylist(L):
# # #     L2 = []
# # #     for x in L:
# # #         if x not in L2:
# # #             L2.append(x)
# # #     return L2

# # # print(Mylist(L))

# # #编程用sort进行排序，然后从最后一个元素开始判断

# # def Mysort(L):
# #     L.sort()
# #     print(L)
# #     N =len(L)
# #     for i in range(N):
# #         if L[N-1] < L[N-2]:
# #             print("wrong")
# #         else:
# #             print("%s is bigger than %s"%(L[N-1],L[N-2]))
# #         N = N-1
# #         if N == 1:
# #             break
# # Mysort(L)

# # def dic_updater(k, v, dic={}):
# #     dic[k] = v
# #     print(dic)

# # dic_updater("one",1)
# # dic_updater("two",2)
# # dic_updater("three",3,{})
# # dic_updater("four",4)

def say_hi(func):
    def wrapper(*args, **kwargs):
        print("hi")
        ret = func(*args, **kwargs)
        print("bye")
        return ret
    return wrapper

def say_yo(func):
    def wrapper(*args, **kwargs):
        print("yo")
        return func(*args, **kwargs)
    return wrapper

@say_hi
@say_yo
def func():
    print("ROCK & ROLL")

func()

def decorator_a(func):
    print ('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print ('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2

f(1)

# #函数后调用达到装饰器效果
# # @decorator_a
# # def f(x):
# #     print 'Get in f'
# #     return x * 2

# # # 相当于
# # def f(x):
# #     print 'Get in f'
# #     return x * 2

# # f = decorator_a(f)

