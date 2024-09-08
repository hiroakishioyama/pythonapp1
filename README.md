# FastAPI User Management System

このプロジェクトは、FastAPIを使用してユーザーの作成、読み取り、更新、削除を行う基本的なAPIを提供します。以下の手順に従って、APIをセットアップし、ローカル環境で実行してください。

### 必要条件

Python 3.8 以上
FastAPI
Uvicorn（ASGIサーバー）
セットアップ方法

必要なライブラリをインストールします。
pip install fastapi[all] uvicorn

プロジェクトフォルダ内に main.py ファイルを作成し、APIのコードをコピーします。
コマンドラインまたはターミナルから以下のコマンドを実行して、APIサーバーを起動します。
uvicorn main:app --reload
--reload オプションは開発中にコードの変更がリアルタイムで反映されるようにするためのものです。

### API エンドポイント
POST /users/: 新しいユーザーを作成します。

GET /users/{user_id}: 指定したIDのユーザーを取得します。

PUT /users/{user_id}: 指定したIDのユーザーの情報を更新します。

DELETE /users/{user_id}: 指定したIDのユーザーを削除します。

### 使用例
以下は、curl コマンドを使用した各APIエンドポイントの使用例です。

- ユーザーを作成する

curl -X POST http://127.0.0.1:8000/users/ -H "Content-Type: application/json" -d '{"id": 1, "name": "John Doe", "email": "example@example.com"}'

- ユーザー情報を取得する

curl -X GET http://127.0.0.1:8000/users/1

- ユーザー情報を更新する

curl -X PUT http://127.0.0.1:8000/users/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "example_new@example.com"}'

- ユーザーを削除する

curl -X DELETE http://127.0.0.1:8000/users/1

### 注意事項
APIのテストや開発の際には、適切なデータ管理を行ってください。このシステムは簡単なデモ用途に適しており、本番環境での使用前にはセキュリティやデータ永続化の実装が必要です。