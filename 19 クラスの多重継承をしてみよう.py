# さて、次はクラスの多重継承について見ていきましょう。
# 前回見た継承なのですが、実は親クラスを複数持つことができます。
# 少しこのあたりはややこしいので、あらかじめいくつかクラスを用意しておきました。
# ではクラス A、B があったとして、それらを継承した C を作ってみましょう。
# A、B を継承するには、こちらにカンマ区切りで書いてあげれば OK です。
# では class C(A, B) としてあげます。
# とりあえず中身は空にしてあげたいと思います。
# あとはちゃんと継承できているか確認してみましょう。
# C のインスタンスを作ってあげて、c.say_a()、c.say_b() を実行してみたいと思います。
# そうしてあげると…こうですね、想定通りになっています。
# ただ、多重継承で問題になるのが、クラス A、B で同じメソッドがあった場合です。
# 例えば両方に say_hi() があったとして、どのように実行されるか試してみましょう。
# では単に print("hi! from A")、そして B のほうからは print("hi! from B") という処理を書いてあげたいと思います。
# では、こちらで c.say_hi() を呼び出してみましょう。
# 実行するとどうなるかというと…、hi! from A になっているのがわかるかと思います。
# これは継承を指定するときの順番が影響していて、同じメソッドがあった場合は、先に指定したほうのメソッドが優先されます。
# したがって、こちらを A, B ではなくて、継承順を逆にしてあげて B, A とすると、今度は hi! from B が表示されるはずです。
# こうですね、うまくいっています。
# 多重継承はもっと奥が深いのですが、まずは基本としてこのあたりをおさえておいてください。

# クラスの多重継承
# A,B -> C

class A:
    def say_a(self):
        print("A!")
    def say_hi(self):   # AとBで同じメソッドがある
        print("hi! from A")
class B:
    def say_b(self):
        print("B!")
    def say_hi(self):   # AとBで同じメソッドがある
        print("hi! from B")
class C(B, A):   # 同じメソッド(say_hiを読んだ場合、先に読み込んだほうを実行する)
    pass

c = C()
# c.say_a()
# c.say_b()
c.say_hi()
