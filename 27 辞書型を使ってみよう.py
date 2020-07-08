# さて、次はキーと値でデータを管理していく辞書型について見ていきましょう。
# では例を見ていきたいのですが、sales というデータを作って、例えば taguchi くんの売り上げが 200 で、fkoji さんの売り上げが 400 だった場合は、 sales = とした後に {} をまずは書いてあげます。
# その後にキーと値を : で区切って書いていけば OK です。
# taguchi くんの売り上げがまずは 200、そして , で区切ってあげて fkoji さんの売り上げが 400 と表現してあげましょう。
# ここで、それぞれの要素にアクセスするには、キーを指定してあげれば OK です。
# 例えば taguchi さんの売り上げが知りたかったら、キーでこのように print(sales["taguchi"]) と指定してあげれば OK でしょう。
# もしくは値を書き換えたい場合は、 sales["taguchi"] = 300 とすると、200 ではなくて 300 に書き換えることができます。
# また、要素を追加するには単に新しいキーで値を追加すれば OK です。
# では dotinstall さんの売り上げが 500 だった場合は、 sales["dotinstall"] = 500 としてあげましょう。
# それから、要素の削除には del() が使えます。
# del() とした後に sales でキーを指定してあげましょう。
# では fkoji さんのデータが要らなかった場合は del(sales["fkoji"]) としてあげれば OK です。
# ではうまくいったかどうか、 print(sales) してあげましょう。
# ではこちらで見てあげると…こうですね、想定通りになっているのがわかるかと思います。
# それから辞書型に対してループを行う場合なのですが、items() という命令を使ってあげるとキーと値を同時に取り出すことができます。
# では見ていきましょう。
# では for とした後に key, value としてあげて、 in sales.items(): としてあげます。
# そうすると、キーと値が、key と value に入ってくるので、それを文字列の中で表示してあげましょう。
# では print("{0}: {1}".format(key, value)) としてあげます。
# 実行してあげると…こうですね、うまくいっています。
# このあたりの処理にも慣れておくようにしてください。


# リスト型とタプル
# 集合型
# 辞書型

sales = {"taguchi": 200, "fkoji": 400}
print(sales["taguchi"])
sales["taguchi"] = 300
sales["dotinstall"] = 500
del (sales["fkoji"])
print(sales)

# keysメソッド：辞書からキーのリストを表すdict_keysオブジェクトを返す
# valuesメソッド：辞書から値のリストを表すdict_valuesオブジェクトを返す
# itemsメソッド：辞書からキーと値のペアのリストを表すdict_itemsオブジェクトを返す
for key, value in sales.items():  # 上のitemsメソッドを使っている
    print("{0}は{1}です".format(key, value))
