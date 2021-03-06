# さて、次はクラスについて見ていきましょう。
# クラスは複雑なデータ構造を作るための仕組みなのですが、例を見ていきましょう。
# では何らかのアプリを作っていて、ユーザーに関するデータをまとめたかったとします。
# その時に user_name = "taguchi"、それから user_score = 10 といった具合に変数を作っていってもいいのですが、user に関するデータをまとめられたら便利です。
# そこで、クラスを作ってみましょう。
# クラスを作るには class とした後にクラス名をつけてあげます。
# 今回は User としましょう。
# なお、クラス名の最初は大文字にしてください。
# クラスでは、いろいろなことを定義できるのですが、とりあえず今回は空のクラスを作ってみましょう。
# 中身のないクラスを作るには、単に pass としてあげれば OK です。
# 今のところは空ではありますが、これでデータの構造、データの型ができました。
# このデータの型から実際のデータを作るには User() としてあげます。
# 今回、名前が tom であるデータを作りたいので tom という変数に入れてあげましょう。
# あとは tom に対してさまざまな属性を付け加えることができます。
# tom.name = "tom"、それから tom.score = 20といった具合ですね。
# このユーザー型からいくつでもデータを作ることができるので、例えばもう 1 つのデータとして bob = User() としてあげて、bob.name = "bob"、bob.level = 5 といった具合にデータを作っていくことができます。
# 属性は作るデータごとに好きに変えることもできるので、覚えておきましょう。
# ちなみにクラスから作られたこれらのデータを、そのクラスのインスタンスと呼ぶので、用語として覚えておきましょう。
# これらのデータの属性にアクセスするには、設定した時と同じように書いてあげればいいので、例えば print(tom.name) だとか、print(bob.level) といった具合に書いていくことができます。
# では実行してみましょう…こうですね、想定通りになっています。
# このようにクラスを使えば、複雑なデータ構造を簡単に作ることができます。
# では、続きは次回にしていきましょう。

# クラス

class User: # クラス名は頭文字大文字
    pass #とりあえずからのクラスを作った

tom = User() #インスタンス
tom.name ="tom"
tom.score =20

bob =User()
bob.name ="bob"
bob.level=5

print(tom.name)
print(bob.level)
