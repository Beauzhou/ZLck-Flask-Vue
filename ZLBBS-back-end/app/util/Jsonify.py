from flask import jsonify


class Jsonify(object):
    @staticmethod
    def query(data, page, size, total):
        return jsonify(
            {"data": {"records": data, "page": page, "size": size, "total": total}, "code": "200", "msg": "查询成功"})

    @staticmethod
    def query_all(data, total=None):
        if total is None:
            total = len(data)
        return jsonify({"data": data, "code": "200", "msg": "查询成功", "total": total})

    @staticmethod
    def success(data):
        return jsonify({"code": "200", "msg": data})

    @staticmethod
    def error(data):
        return jsonify({"code": "200", "msg": data}), 500

    @staticmethod
    def insert():
        return jsonify({"code": "200", "msg": "添加成功"})

    @staticmethod
    def update():
        return jsonify({"code": "200", "msg": "更新成功"})

    @staticmethod
    def delete():
        return jsonify({"code": "200", "msg": "删除成功"})

    @staticmethod
    def parameter_error(error):
        return jsonify(error), 400

    @staticmethod
    def error(error):
        return jsonify(error), 500


Jsonify = Jsonify()
