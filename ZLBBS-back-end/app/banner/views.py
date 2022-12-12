import traceback
from app.util.Jsonify import Jsonify
from flask import jsonify, request
from app.util.pymysql import mysql
from ..banner import banner
from datetime import datetime


# return 500 error
@banner.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


@banner.route("/search", methods=['GET'])
def search():
    sql = "SELECT * from banner ORDER BY priority asc"
    list = mysql.get_list(sql)
    return Jsonify.query_all(list)


@banner.route("/add", methods=['POST'])
def add():
    sql = "insert into banner (name,image_url,priority,create_time) values (%s,%s,%s,%s) "
    js = request.get_json()
    name = js.get("name")
    image_url = js.get("image_url")
    priority = js.get("priority")
    mysql.create(sql, (name, image_url, priority, datetime.now()))
    return Jsonify.insert()


# @detail.route("/searchComment", methods=['GET'])
# def searchComment():
#     sql = "select m.id, u.username,  m.content, m.create_time, m.post_content from (select c.id, c.content, c.create_time, c.author_id, p.content as post_content from comment c INNER JOIN post p on p.id = c.post_id) m inner join `user` u on u.id = m.author_id limit %s, %s"
#     sql1 = "select count(*) from comment"
#     page = request.args.get("page")
#     size = request.args.get("size")
#     list1 = mysql.get_list(sql, (int(page) - 1, int(size)))
#     total = mysql.get_one(sql1)
#     return Jsonify.query_all(list1, total["count(*)"])
#
#

#
#
# @detail.route("/countDay", methods=['GET'])
# def count_day():
#     sql = "select date_format(create_time,'%Y-%m-%d') as data, count(1) as count from comment where create_time >= date(now()) - interval 7 day group by day(create_time);"
#     return Jsonify.query_all(mysql.get_list(sql))
#
#
@banner.route("/delete/<id>", methods=['delete'])
def delete(id):
    sql = "delete from banner where id = %s"
    mysql.delete(sql, id)
    return Jsonify.delete()
