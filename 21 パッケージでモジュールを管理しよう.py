# さて、続きをやっていきましょう。
# 前回見たモジュールなのですが、数が増えてくるとフォルダにまとめて分類したくなるはずです。
# では例を見ていきましょう。
# では今回、単純にこちらの user モジュールをフォルダに入れてみます。
# モジュールを入れるフォルダをパッケージというので、今回 mypackage というフォルダにしてあげましょう。
# では user.py を移動させてあげます。
# パッケージを Python で認識させるには、そのフォルダの中に特殊なファイルが必要です。
# ファイル名は決まっていて、__init__.py としてあげてください。
# いろいろな設定が書けたりするのですが、とりあえず空で OK です。
# そこまでできたら、myapp.py のほうから読み込んでみましょう。
# 使い方なのですが、「パッケージはフォルダがモジュール化されたもの」と考えるとわかりやすいかと思います。
# したがって、モジュールと同じように使っていけば OK です。
# では「import mypackage」（import モジュール名、つまりパッケージ名）としてあげて、mypackage の下の階層のモジュールを呼び出すには、ドットでモジュール名を書いてあげれば OK です（import mypackage.user）。
# その後にクラスを使うには、パッケージから書いていけばいいので…、mypackage.user.AdminUser() とすれば OK です。
# では実行してあげると…こうですね、うまくいっているのがわかるかと思います。
# もしくは、こちらの名前がちょっと長いという場合には別名をつけることができて、その場合は as で別名を付けてあげましょう。
# では「mymodule」としてあげます。
# そうすると、こちらの方はもっと短く「mymodule」と書くことができます。
# これも実行してうまくいくか確かめてみましょう…、こうですね、うまくいっています。
# それから、モジュールの時に見たように別の書き方もできて、どうするかというと「from」から始めてあげれば OK ですね。
# 「from mypackage.user import AdminUser」とすると、AdminUser クラスだけを読み込んでくれます。
# その場合はもっと単純に AdminUser だけにすればいいので「bob = AdminUser("bob", 23)」で OK です。
# これもうまくいったか確かめてみましょう…、こうですね、うまくいっています。
# クラスや関数が多くなってくると、このようにモジュールやパッケージを使って管理していくので慣れておくようにしてください。

# package

import mypackage.user
import mypackage.user as mymodule # as で別名をつけられる
from mypackage.user import AdminUser # from パッケージ名.モジュール名 import クラス名orメソッド名でそのクラスorメソッドのみをインポートする
# カンマ区切りで複数インポート可能

# bob = mypackage.user.AdminUser("bob", 23) # パッケージ名.モジュール名で読み込んだ場合
# bob = mymodule.AdminUser("bob", 23) # 別名で読み込んだ場合
bob = AdminUser("bob", 23) # メソッドをfromで読み込んだ場合、パッケージ名、モジュール名は不要


print(bob.name)
bob.say_hi()
bob.say_hello()
