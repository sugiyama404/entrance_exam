from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import settings
from models.dao import AiAnalysisLog

engine = create_engine(f'mysql+pymysql://{settings.dbuser}:{settings.dbpassword}@{settings.dbhost}/{settings.dbname}?charset=utf8')
Base = automap_base()
Base.prepare(engine)
Aitable = Base.classes.ai_analysis_log
"""
AiAnalysisLogオブジェクトのデータを`ai_analysis_log`テーブルに挿入します。
Args:
    data: AiAnalysisLogクラスのオブジェクト
"""
def insert_data(data: AiAnalysisLog):
    session = Session(engine)
    session.add(Aitable(
        image_path=data.image_path,
        success=data.success,
        message=data.message,
        **{
        "class": data.class_,
        },
        confidence=data.confidence,
        request_timestamp=data.request_timestamp,
        response_timestamp=data.response_timestamp,
    ))
    session.commit()
