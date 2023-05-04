# Xquizlet
[Quizlet](https://quizlet.com)の`マッチ`を、高速にクリアするために作られたツールです。
## How to use it?
### 環境構築
1. [Python](https://python.org)をインストールします。
2. [Poetry](https://github.com/python-poetry/poetry)をインストールします。
3. `poetry install`を実行します
### セッティング
#### `xquizlet.csv`
XquizletのConfig fileです。
まず、`xquizlet.csv`を作成しましょう。
このファイルは、キーと値から構成されています。
```csv
__id__,1
する,do
食べる,eat
```
Danderで囲まれたものは、コンフィグで、そうでないものは、単語です。
#### `cookie.json`
EditThisCookieのExport機能をつかって、ExportしたCookieを記載します。
### いざ、実行
```shell
python main.py
```
うまくいかない場合は、`--no-headress`を試してはいかが?
```shell
python main.pt --no-headress
```