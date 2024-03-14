from dataclasses import dataclass
from typing import Union

"""
AI分析結果のログ
Attributes:
  image_path: 画像ファイルパス
  success: 分析成功フラグ
  message: 分析結果メッセージ
  class_: 分類結果 (数値)
  confidence: 分類信頼度
  request_timestamp: リクエスト送信時刻
  response_timestamp: レスポンス受信時刻
"""

@dataclass
class AiAnalysisLog:
  image_path: Union[str, None]
  success: Union[str, None]
  message: Union[str, None]
  class_: Union[int, None]
  confidence: Union[float, None]
  request_timestamp: Union[int, None]
  response_timestamp: Union[int, None]
