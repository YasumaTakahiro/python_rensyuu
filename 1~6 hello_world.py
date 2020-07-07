msg: str = "hello_world!!"
print(msg)
msg = "12"
print(msg)

# 定数は使えないが、大文字でかくことで定数として扱おうというマナー？がある
ADMIN_MAIL: str = "yasuma_takahiro"

# 文字列
s = "he\nllo\two\trld"
html = """<html>
<body></body>
</html>
"""
print(s)
print(html)

# test3
# 整数
i: int = 10

# 浮動小数点
f: float = 23.4

# 論理値
flag: bool = True  # or False

# 演算子
# + - * /  切り捨て除算 // あまり %  べき乗 **

x: int = 10
print(x / 3)  # 3.333...
print(x // 3)  # 3
print(x % 3)  # 1
print(x ** 2)  # 100

y: int = 4
# y = y + 12
# ↑と同じ
y +=12
print(y)  # 16

# and or not
print(True and False) # False
print(True or False) # True
print(not True) # False

# + *
print("Hello " + "world")
print("Hello " * 3)

name = "taguchi"
score: float = 52.8
# print("名前=%s, 点数=%f" % (name,score))
# print("名前=%-10s, 点数=%10.2f" % (name,score))
# print("名前={0}, 点数={1}" .format(name,score))
print("名前={0:>10s}, 点数={1:<10.2f}".format(name, score))
