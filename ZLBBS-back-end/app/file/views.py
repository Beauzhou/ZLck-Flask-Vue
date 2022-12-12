import os
import traceback
from flask import request, jsonify, send_from_directory
from ..file import file
from app.util import fileUtil
from app.configUtils import ConfigUtils

conf = ConfigUtils()
cf = conf.get_config()


@file.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


@file.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    return fileUtil.upload(f)


@file.route('/download/<filename>', methods=['GET'])
def download(filename):
    path = os.path.isfile(os.path.join(cf.get('file', 'UPLOAD_FOLDER'), filename))
    if path:
        return send_from_directory(cf.get('file', 'UPLOAD_FOLDER'), filename)
