class User:  # クラス名は頭文字大文字
    def __init__(self, name):
        self.name = name

    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))


class AdminUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))


print("waoooooooooooo") #インポートしたタイミングで実行される