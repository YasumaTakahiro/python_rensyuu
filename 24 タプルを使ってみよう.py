# さて、次はタプルについて見ていきましょう。
# タプルもリストと同じく、順序のあるデータを管理するためのものなのですが、値の変更ができないという点が異なっています。
# 例を見ていきましょう。
# では、今回 items という変数でタプルを作っていきます。
# タプルは () の中に値を , 区切りで入れていけば OK です。
# リストでは同種のデータを扱うことが多いのですが、タプルでは違う種類のデータを含めることが多いですね。
# 例えば整数、文字列、浮動小数点数といった具合です。
# ちなみに、リストでも違う種類のデータを含めることは可能です。
# それぞれの要素へのアクセスですが、リストと同じように print(items[]) で [] の中に数字としていきます。
# ただ値を書き換えることはできないので、これはエラーになるはずです。
# 見てあげましょう…こうですね、タプルでは書き換えられません、と出ています。
# それから、タプルとリストは相互に変換することができたりします。
# タプルをリストにするには list() で囲ってあげれば OK です。
# () の中に print(list((1, 3, 5))) のように書いていきましょう。
# 逆に、リストをタプルにするには tuple([]) としてあげて、[] の中にリストの要素を書いていけば OK ですね。
# 実行してみると…こうですね、上の方は [] でリストになっていて、下の方は () でタプルになっているのがわかるかと思います。
# タプルは一度作ると変更ができないので、プログラム中で変わってほしくないデータを取り回すのによく使われます。
# このあたりにも慣れておきましょう。


# リスト型とタプル
# 集合型
# 辞書型

# タプル

# items = (50, "apple", 32.5)
# print(items[1])
# # items[1] = "pen" #タプルは書き換え不能

print(list((1, 3, 5)))
print(tuple([1, 3, 5]))



