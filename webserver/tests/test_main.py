import pytest
from main import app
from unittest.mock import patch
from werkzeug.datastructures import FileStorage
from utils.helper import check_extention, create_random_dir
from models.dao import AiAnalysisLog
from models.base import insert_data
from io import BytesIO
from unittest import mock
import os


"""
GETメソッドによるアクセステスト
"""
def test_index_get():
  with app.test_client() as client:
    response = client.get('/')
    assert response.status_code == 200
    assert 'html' in response.data.decode('utf-8')
    assert 'AI画像分析' in response.data.decode('utf-8')

"""
POSTメソッドによる正常処理テスト
"""
@patch('utils.helper.check_extention')
def test_index_post_success(mock_check_extention):
  mock_check_extention.return_value = True

  with app.test_client() as client:
    response = client.post('/', data=dict(file=(BytesIO(b'cat'), 'cat.png')),
                           content_type="multipart/form-data")
    assert response.status_code == 200
    assert 'ファイルの保存が成功しました。' in response.data.decode('utf-8')

"""
POSTメソッドによるファイルエラーテスト
"""
@patch('utils.helper.check_extention')
def test_index_post_file_error(mock_check_extention):
  mock_check_extention.return_value = True

  with app.test_client() as client:
    response = client.post('/', data={})
    assert response.status_code == 200
    assert 'html' in response.data.decode('utf-8')
    assert 'ファイルがありません。' in response.data.decode('utf-8')

"""
POSTメソッドによるAPIエラーテスト
"""
@patch('utils.helper.check_extention')
@patch('utils.helper.create_random_dir')
@patch('requests.post')
def test_index_post_api_error(mock_requests, mock_create_random_dir, mock_check_extention):
  base_dir = "/root/opt/static/image"
  subdirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
  selected_subdir = subdirs[0]
  subsubdirs = [f for f in os.listdir(os.path.join(base_dir, selected_subdir))
                if os.path.isdir(os.path.join(base_dir, selected_subdir, f))]
  selected_suubsubdir = subsubdirs[0]

  mock_check_extention.return_value = True
  mock_create_random_dir.return_value = [selected_subdir,selected_suubsubdir]
  mock_requests.side_effect = Exception('APIエラー')

  with app.test_client() as client:
    response = client.post('/', data=dict(file=(BytesIO(b'cat'), 'cat.png')),
                           content_type="multipart/form-data")
    assert response.status_code == 200
    assert 'html' in response.data.decode('utf-8')
    assert 'API通信に失敗しました。' in response.data.decode('utf-8')

"""
POSTメソッドによるDBエラーテスト
"""
@patch('utils.helper.check_extention')
@patch('utils.helper.create_random_dir')
@patch('requests.post')
def test_index_post_db_error(mock_requests, mock_create_random_dir, mock_check_extention):
  base_dir = "/root/opt/static/image"
  subdirs = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
  selected_subdir = subdirs[0]
  subsubdirs = [f for f in os.listdir(os.path.join(base_dir, selected_subdir))
                if os.path.isdir(os.path.join(base_dir, selected_subdir, f))]
  selected_suubsubdir = subsubdirs[0]

  mock_check_extention.return_value = True
  mock_create_random_dir.return_value = [selected_subdir,selected_suubsubdir]
  mock_requests.post.return_value = mock.Mock(status_code=200,
                                              json={"success": "true","message":
                                                    "success","estimated_data": {"class": 3,"confidence": 0.8683}})
  insert_data.side_effect = Exception('DBエラー')

  with app.test_client() as client:
    response = client.post('/', data=dict(file=(BytesIO(b'cat'), 'cat.png')), content_type="multipart/form-data")
    assert response.status_code == 200
    assert 'html' in response.data.decode('utf-8')
    assert 'DB登録に失敗しました。' in response.data.decode('utf-8')
