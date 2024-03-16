# 強力な画像分析AIで、画像を瞬時に分類！

<p align="center">
  <img src="resource/AI画像分析見本.gif" alt="animated" width="400">
</p>

![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?&logo=ubuntu&logoColor=white)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?logo=docker&logoColor=white)](https://www.docker.com/)
![Git](https://img.shields.io/badge/GIT-E44C30?logo=git&logoColor=white)
![gitignore](https://img.shields.io/badge/gitignore%20io-204ECF?logo=gitignoredotio&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?logo=githubactions&logoColor=white)
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

## 概要
このアプリケーションは、AIが画像の分析と評価を行い、画像を分類します。

## 機能一覧
+ 画像保存機能
+ API通信機能
+ DB登録機能
+ 画面表示機能

## インストール

1. 以下のコマンドを実行して、開発サーバーを起動します。

```bash
docker compose up
```

2. アプリケーションにアクセスします。

http://localhost:8080 にアクセスすると、Flaskアプリケーションが起動していることを確認できます。

## ディレクトリ構成

```text
.
├── README.md
├── apserver
├── dbserver
├── docker-compose.yml
├── resource
└── webserver
    ├── Dockerfile
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   ├── base.py
    │   └── dao.py
    ├── requirements.txt
    ├── settings.ini
    ├── settings.py
    ├── static
    │   ├── bootstrap.min.css
    │   ├── bootstrap.min.js
    │   ├── image
    │   └── jquery-3.7.1.min.js
    ├── templates
    │   └── index.html
    ├── tests
    │   ├── __init__.py
    │   ├── test_main.py
    │   └── test_model.py
    └── utils
        ├── __init__.py
        └── helper.py
```

#### apserver
アプリケーションサーバー関連ファイルなどが置かれます。

#### dbserver
データベースサーバー関連の設定ファイルなどが置かれます。具体的には、データベースの種類、接続情報、スキーマ定義ファイルなどです。

#### resource
Readme.mdで使用される静的ファイルなどのリソースが置かれます。

#### webserver
Webアプリケーション本体が置かれています。

## 設定ファイル

#### docker-compose.yml
Docker Compose の設定ファイルです。このファイルには、アプリケーションを構成するコンテナとその設定情報が定義されています。

#### settings.ini
設定ファイル (INI形式)です。アプリケーションの設定情報などを記述します。

#### settings.py
設定ファイル (Python形式)です。settings.ini と同様に、アプリケーションの設定情報などを記述します。

## テスト

このプロジェクトは、pytest を使用してテストされています。

### テストディレクトリ構成

```text
webserver
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   └── test_model.py
```

+ init.py: テストディレクトリ初期化ファイルです。
+ test_main.py: main.py のテストコードです。
+ test_model.py: models ディレクトリ内のモデルのテストコードです。

実行方法
以下のコマンドでテストを実行できます。

```bash
docker compose exec web pytest tests/ -v
```

#### テスト対象
以下の項目がテスト対象となります。

+ main.py の関数
+ models ディレクトリ内のモデル

#### テスト項目
以下の項目がテスト項目となります。

##### main.py の関数
+ GETメソッドによるアクセステスト
+ POSTメソッドによる正常処理テスト
+ POSTメソッドによるファイルエラーテスト
+ POSTメソッドによるAPIエラーテスト
+ POSTメソッドによるDBエラーテスト

##### models ディレクトリ内のモデル
+ 成功判定データを入れた場合の正常処理テスト
+ 失敗判定データを入れた場合の正常処理テスト

#### テスト結果

<p align="center">
  <img src="resource/テスト結果.png" alt="animated">
</p>














