# 強力な画像分析AIで、画像を瞬時に分類！

<p align="center">
  <img src="resource/AI画像分析見本.gif" alt="animated" width="400">
</p>

![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?&logo=ubuntu&logoColor=white)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?logo=docker&logoColor=white)](https://www.docker.com/)
![Git](https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white)
![gitignore](https://img.shields.io/badge/gitignore%20io-204ECF?logo=gitignoredotio&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?logo=javascript&logoColor=F7DF1E)
[![Python](https://img.shields.io/badge/Python-3.8.8-blue.svg?logo=python&logoColor=blue)](https://www.python.org/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3-blue.svg)](https://docs.docker.com/compose/)
[![Flask](https://img.shields.io/badge/Flask-3.0.2-blue.svg?logo=flask&logoColor=white)](https://palletsprojects.com/p/flask/)
[![Pytest](https://img.shields.io/badge/pytest-8.1.1-blue.svg)](https://pytest.org/)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.28-blue.svg)
[![MySQL](https://img.shields.io/badge/MySQL-8.0.32-blue.svg?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![jQuery](https://img.shields.io/badge/jQuery-3.7.1-blue.svg?logo=jquery&logoColor=white)](https://jquery.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
![Commit Msg](https://img.shields.io/badge/Commit%20message-Eg-brightgreen.svg)
![Code Cmnt](https://img.shields.io/badge/code%20comment-Ja-brightgreen.svg)

# 概要
このアプリケーションは、AIが画像の分析と評価を行い、画像を分類します。

# 機能一覧
+ 画像保存機能
+ API通信機能
+ DB登録機能
+ 画面表示機能


要件
画像ファイルのパスを受け取る
架空のAPIにリクエストを投げる
レスポンスをデータベースに保存する
実装
画像ファイルのパスを受け取る
架空のAPIの仕様に基づいて、レスポンスを想定する
想定したレスポンスをデータベースに保存する
データベース
データベースには、以下のテーブルを作成します。

画像情報テーブル
画像ID (primary key)
画像ファイルパス
クラス名
信頼度
実行方法
Python 3.7以上をインストールする
requirements.txt に記載されているライブラリをインストールする
main.py を実行する
使用例
Python
python main.py /path/to/image.jpg
コードは注意してご使用ください。
テスト
tests ディレクトリにテストコードを用意しています。

Python
python -m unittest tests
コードは注意してご使用ください。
注意点
実際のAPIは存在しないため、想定されるレスポンスはあくまでも架空のものとなります。
データベースへの接続情報は、config.ini ファイルで設定する必要があります。
今後の課題
実際のAPIと連携できるようにする
画像ファイルのアップロード機能を追加する
Web UI を作成する
謝辞
本アプリケーションは、Hugging Face: https://huggingface.co/ のライブラリを使用しています。
ライセンス
MIT License

その他
本アプリケーションは、学習用サンプルとして提供しています。
本アプリケーションを利用したことによるいかなる損害も負いかねます。
Mock-up
APIの仕様に基づいて、想定されるレスポンスの例を以下に示します。

JSON
{
  "image_id": "1234567890",
  "class_name": "cat",
  "confidence": 0.95
}
コードは注意してご使用ください。
このレスポンスは、image_id が "1234567890" である画像が "cat" クラスに属し、その信頼度が 95% であることを示しています。

提出物
README.md
main.py
config.ini
requirements.txt
tests/




