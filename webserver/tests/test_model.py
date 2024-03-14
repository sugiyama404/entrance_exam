import pytest
from unittest.mock import patch
from unittest.mock import Mock
from models.dao import AiAnalysisLog
from models.base import insert_data


"""
Sessionモック
"""
@pytest.fixture
def mock_session():
  session = Mock()
  session.add.return_value = None
  session.commit.return_value = None
  return session

dummy_data_success = AiAnalysisLog(
    image_path='/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg',
    success='true',
    message='success',
    class_=3,
    confidence=0.95,
    request_timestamp=1678751200,
    response_timestamp=1678751230,
)

dummy_data_failure = AiAnalysisLog(
    image_path='/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg',
    success='true',
    message='success',
    class_=None,
    confidence=None,
    request_timestamp=1678751200,
    response_timestamp=1678751230,
)

"""
成功判定データを入れた場合の関数が正常に動作することをテストする
insert_data() 関数のテスト
Args:
    mock_session: Sessionモック
"""
def test_insert_data_success(mock_session):
    insert_data(dummy_data_success)
    # セッションに追加されたデータの検証
    assert mock_session.add.called_once
    # コミットされたデータの検証
    assert mock_session.commit.called_once

"""
失敗判定データを入れた場合の関数が正常に動作することをテストする
insert_data() 関数のテスト
Args:
    mock_session: Sessionモック
"""
def test_insert_data_failure(mock_session):
    insert_data(dummy_data_failure)
    assert mock_session.add.called_once
    assert mock_session.commit.called_once
