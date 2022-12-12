import os
import uuid
from pathlib import Path

from flask import request
from werkzeug.utils import secure_filename, send_from_directory

from app.configUtils import ConfigUtils

conf = ConfigUtils()
cf = conf.get_config()


def upload(file):
    f_filename = file.filename
    file_url = cf.get('file', 'UPLOAD_FOLDER') + '/' + f_filename
    file_path = Path(file_url)
    if file_path.exists() is False:
        file.save(os.path.join(cf.get('file', 'UPLOAD_FOLDER'), f_filename))
        obj = {"fileName": f_filename, "fileUrl": file_url}
        return obj
    else:
        i = 0
        while True:
            after = f_filename.split(".")[0]
            prefix = f_filename.split(".")[-1]
            after += "(" + str(i) + ")"
            file_name = after + "." + prefix
            file_path = Path(cf.get('file', 'UPLOAD_FOLDER') + '/' + file_name)
            if file_path.exists() is False:
                file.save(os.path.join(cf.get('file', 'UPLOAD_FOLDER'), file_name))
                break
            else:
                i += 1
    obj = {"fileName": file_name, "fileUrl": cf.get('file', 'UPLOAD_FOLDER') + '/' + file_name}
    return obj
