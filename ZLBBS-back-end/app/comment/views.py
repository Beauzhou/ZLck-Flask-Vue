import traceback
from app.util.Jsonify import Jsonify
from flask import jsonify, request
from app.util.pymysql import mysql
from ..comment import detail
from datetime import datetime


# return 500 error
@detail.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


@detail.route("/search/<id>", methods=['GET'])
def search(id):
    sql = "SELECT m.id, m.title, m.content, m.create_time, m.`name`, u.username FROM (SELECT p.id, p.title, p.content, p.create_time, p.author_id, b.`name` FROM `post` p INNER JOIN board b on b.id = p.board_id) m INNER JOIN `user` u on u.id = m.author_id where m.id = %s limit 1"
    dict = mysql.get_one(sql, id)
    sql1 = "SELECT c.id, c.content,c.create_time,u.username from `comment` c INNER JOIN `user` u on c.author_id = u.id WHERE post_id = %s"
    list1 = mysql.get_list(sql1, id)
    dict["comment"] = list1
    return Jsonify.query_all(dict)


@detail.route("/searchComment", methods=['GET'])
def searchComment():
    sql = "select m.id, u.username,  m.content, m.create_time, m.post_content from (select c.id, c.content, c.create_time, c.author_id, p.content as post_content from comment c INNER JOIN post p on p.id = c.post_id) m inner join `user` u on u.id = m.author_id limit %s, %s"
    sql1 = "select count(*) from comment"
    page = request.args.get("page")
    size = request.args.get("size")
    list1 = mysql.get_list(sql, (int(page) - 1, int(size)))
    total = mysql.get_one(sql1)
    return Jsonify.query_all(list1, total["count(*)"])


@detail.route("/addComment", methods=['POST'])
def add():
    sql = "insert into comment (content,post_id,author_id,create_time) values (%s,%s,%s,%s) "
    js = request.get_json()
    content = js.get("content")
    post_id = js.get("post_id")
    author_id = js.get("author_id")
    mysql.create(sql, (content, post_id, author_id, datetime.now()))
    return Jsonify.insert()


@detail.route("/countDay", methods=['GET'])
def count_day():
    sql = "select date_format(create_time,'%Y-%m-%d') as data, count(1) as count from comment where create_time >= date(now()) - interval 7 day group by day(create_time);"
    return Jsonify.query_all(mysql.get_list(sql))


@detail.route("/delete/<id>", methods=['delete'])
def delete(id):
    sql = "delete from comment where id = %s"
    mysql.delete(sql, id)
    return Jsonify.delete()
