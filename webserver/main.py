from flask import Flask, render_template, request, url_for
from flask_cors import CORS
import requests

import settings
import utils
from models import base, dao

app = Flask(__name__)
CORS(app)

"""
ファイルアップロード処理と分析結果表示処理
主な処理は以下の通り。
・ファイル取得処理
・画像保存処理
・API通信処理
・DB登録処理
・画面表示処理
"""
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # ファイル取得処理
        try:
            file = request.files['file']
        except KeyError:
            # ファイルが存在しない場合
            return render_template('index.html', message='ファイルがありません。')
        filename = file.filename
        # 拡張子チェック
        if not utils.helper.check_extention(filename.split('.')[-1]):
            return render_template('index.html', message='許可されていないファイル形式です。')

        # 画像保存処理
        try:
            dir_list = utils.helper.create_random_dir('static/'+settings.img_dir_name, 2)
            file_relative_path = settings.img_dir_name + '/' + dir_list[0] +'/'+ dir_list[1] + '/' + filename
            api_url = settings.api_base_url + '/' + file_relative_path
            file_path ='static/' + file_relative_path
            with open(file_path, "wb") as f:
                f.write(file.read())
        except Exception as e:
            # 画像保存処理でエラーが発生した場合
            return render_template('index.html', message='ファイルの保存に失敗しました。')

        # API通信処理
        try:
            request_time = utils.helper.get_current_time()
            response = requests.post(
                api_url,
                files=file,
            )
            response_time = utils.helper.get_current_time()
            res_json = response.json()
        except Exception as e:
            # API通信処理でエラーが発生した場合
            return render_template('index.html', message='API通信に失敗しました。')

        # DB登録処理
        try:
            data = dao.AiAnalysisLog(
                file_path,
                res_json['success'],
                res_json['message'],
                res_json['estimated_data'].get('class', None),
                res_json['estimated_data'].get('confidence', None),
                request_time,
                response_time
                )
            base.insert_data(data)
        except Exception as e:
            # DB登録処理でエラーが発生した場合
            return render_template('index.html', message='DB登録に失敗しました。')

        # 画面表示処理
        image_path = url_for('static', filename=file_relative_path)
        if res_json['success'] == 'true':
            return render_template('index.html', message='ファイルの保存が成功しました。',
                                   result=True, name=filename, image_path=image_path,
                                   dclass=res_json['estimated_data']['class'], dcof=res_json['estimated_data']['confidence'])
        else:
            return render_template('index.html', message='分析が失敗しました。もう一度やり直してください。',
                                   result = False, name=filename, image_path=image_path,
                                   dclass='-', dcof='-')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=settings.web_port)
