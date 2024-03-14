import random, string
import os
from datetime import datetime
import settings

"""
指定されたベースディレクトリ内に、指定された数個のランダムな名前のディレクトリを作成します。
Args:
    base_dir: ランダムディレクトリを作成するベースディレクトリのパス
    num_dirs: 作成するランダムディレクトリの数
Returns:
    作成されたディレクトリ名のリスト
Raises:
    OSError: ディレクトリ作成に失敗した場合
    FileExistsError: ベースディレクトリが存在しない場合
"""
def create_random_dir(base_dir: str, num_dirs: int = 2) -> list:
    created_dirs = []
    if not os.path.exists(base_dir):
        raise FileExistsError(f"ベースディレクトリが存在しません: {base_dir}")
    for i in range(num_dirs):
        while True:
            if i == 0:
                subdirname = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(20))
            else:
                subdirname = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
            try:
                if not os.path.exists(os.path.join(base_dir, subdirname)):
                    break
            except OSError as e:
                raise OSError(f"ディレクトリ存在確認に失敗しました: {os.path.join(base_dir, subdirname)}") from e
        try:
            os.mkdir(os.path.join(base_dir, subdirname))
        except OSError as e:
            raise OSError(f"ディレクトリ作成に失敗しました: {os.path.join(base_dir, subdirname)}") from e
        base_dir += '/' + str(subdirname)
        created_dirs.append(str(subdirname))
    return created_dirs

"""
指定されたディレクトリが存在しない場合は作成します。
Args:
    dir_path: 作成するディレクトリのパス
Returns:
    None
Raises:
    OSError: ディレクトリ作成に失敗した場合
"""
def make_dir(dir_path:str):
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
        except OSError as e:
            raise OSError(f"ディレクトリ作成に失敗しました: {dir_path}") from e

"""
現在時刻を取得し、10桁の数値に変換して返します。
Returns:
    現在時刻を10桁の数値に変換したもの (YYMMDDHHMM形式)
Raises:
    TypeError: datetimeオブジェクトから文字列への変換に失敗した場合
    ValueError: 文字列から数値への変換に失敗した場合
"""
def get_current_time()->int:
    try:
        now = datetime.now()
        str_now = now.strftime("%y%m%d%H%M")
        return int(str_now)
    except TypeError as e:
        raise TypeError(f"datetimeオブジェクトから文字列への変換に失敗しました: {now}") from e
    except ValueError as e:
        raise ValueError(f"文字列から数値への変換に失敗しました: {str_now}") from e

"""
拡張子が許可されているかどうかをチェックする関数
Args:
    extention: 拡張子 (例: '.jpg')
Returns:
    許可されている場合は True、許可されていない場合は False
Raises:
    TypeError: extention が str 型ではない場合
"""
def check_extention(extention:str)->bool:
    if not isinstance(extention, str):
        raise TypeError('extention は str 型である必要があります')
    if extention in settings.ALLOWED_EXTENSIONS:
        return True
    else:
        return False


