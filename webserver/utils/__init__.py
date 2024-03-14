from utils import helper
import os
import settings

curr_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.abspath(os.path.join(curr_dir, os.pardir)) + '/static'
dir_path = static_path + '/'+ settings.img_dir_name

helper.make_dir(dir_path)
