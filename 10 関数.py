# 関数
# さて、次は複数の処理をまとめて、名前をつけることができる関数について見ていきましょう。
# では今回、単に hi と表示させるためだけの関数を作ってみます。
# 関数を作るには def としてあげて関数名をつけてあげます。
# 今回 say_hi() としましょう。
# 関数名には必ず () をつけてあげてください。
# その後に : をつけてあげて、この関数で実行したい処理を字下げして何行でも書くことができます。
# 今回 hi と表示させるだけなので print("hi") とすれば OK でしょう。
# この関数を実行するには関数名に () をつけて呼んであげれば OK です。
# では実行してあげましょう。
# ではこちらに行って実行すると…こうですね、想定通りになっています。
# それから似たような処理をしたいのですが、オプションを与えて少し結果を変えたいという場合もあります。
# その場合は実行時に、例えば名前と年齢を渡したいとして say_hi("tom", 23)、それから say_hi("bob", 21) とすれば、こちらで受け取ることができます。
# 受け取った値を name と age という変数で使いたい場合は def say_hi(name, age): としてあげて、処理の中で使うことができます。
# では、今回はこちらに print("hi {0} ({1})".format(name, age)) として渡してあげると、こちらでは tom (23)、こちらでは bob (21) と表示されるはずです。
# なお、このように関数に渡す値を引数と呼ぶので、用語として覚えておいてください。
# それから引数には初期値を与えることができます。
# 例えば、age に何も渡らなかったら 20 にしたい場合はこのようにしてあげて、うまくいくかどうか確かめてみましょう。
# こちらで、例えば say_hi("steve") としてあげて 2 つ目（の引数）を何も渡さなければ、これは steve (20) と表示されるはずです。
# もしくは、こちらの変数名を使って値を渡すことができます。
# その場合は順番は関係ないので、例えばということで say_hi(age = 18, name = "rick") としてあげると、rick (18) と表示されるはずです。
# ではこれを見てあげると…、こうですね、想定通りになっています。
# まずはこのあたりを押さえておくようにしましょう。



# def say_hi(仮引数):
#     print("hi")
#
# say_hi(実引数 )

def say_hi(name, age=20):
    print("hi {0}({1})".format(name, age))


say_hi("tom", 23)
say_hi("bob", 22)
say_hi("steve")
say_hi(age=23, name="rick")

