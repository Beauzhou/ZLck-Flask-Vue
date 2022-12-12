import threading
import traceback
from flask import request, jsonify
from app.util.Jsonify import Jsonify
from app.util.pymysql import mysql
from ..post import post
from datetime import datetime

lock = threading.Lock()


# return 500 error
@post.errorhandler(500)
def handler_exception(e):
    response = dict(message=traceback.format_exc())
    return jsonify(response), 500


@post.route('/search', methods=['GET'])
def search():
    sql = "select n.id, n.title, n.content, n.create_time, n.username, n.name, count(c.content) as number, n.board_id, n.avatar from (SELECT m.id, m.title, m.content, m.create_time, m.username, m.board_id, m.avatar, b.name from (SELECT p.id, p.title, p.content, p.create_time, u.username, u.avatar, p.board_id from post p INNER JOIN user u on u.id = p.author_id) m inner JOIN board b on b.id = m.board_id) n left join `comment` c on c.post_id = n.id "
    sql1 = "select count(*) from post "
    type = request.args.get('type')
    sort = request.args.get("sort")
    page = request.args.get("page")
    size = request.args.get("size")
    content = request.args.get("content")
    if content is not None:
        sql += ' where n.content like %s or n.title like %s '
        sql1 += ' where content like %s or title like %s '
    if type is not None:
        sql += " where board_id = %s "
        sql1 += " where board_id = %s "
    if sort == 'time' or sort is None:
        sql += " GROUP BY n.id ORDER BY n.create_time DESC"
    if sort == 'number':
        sql += " GROUP BY n.id ORDER BY number DESC"
    if type is None and content is None:
        sql += " limit %s, %s"
        total = mysql.get_one(sql1)
        list = mysql.get_list(sql, (int(page) - 1, int(size)))
    else:
        sql += " limit %s, %s"
        if content is None:
            total = mysql.get_one(sql1, type)
            list = mysql.get_list(sql, (type, int(page) - 1, int(size)))
        else:
            content = "%" + content + "%"
            total = mysql.get_one(sql1, (content, content))
            list = mysql.get_list(sql, (content, content, int(page) - 1, int(size)))
    return Jsonify.query_all(list, total['count(*)'])


@post.route("/add", methods=['POST'])
def add():
    sql = "insert into post (title,content,board_id,author_id,create_time) values (%s,%s,%s,%s,%s)"
    js = request.get_json()
    title = js.get("title")
    content = js.get("content")
    board_id = js.get("board_id")
    author_id = js.get("author_id")
    mysql.create(sql, (title, content, board_id, author_id, datetime.now()))
    return Jsonify.insert()


@post.route("/count", methods=['GET'])
def count():
    sql = "SELECT b.name, count(p.id) as count from post p right join board b on b.id = p.board_id GROUP BY b.name"
    return Jsonify.query_all(mysql.get_list(sql))


@post.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    sql = "delete from post where id = %s"
    sql1 = "select id from comment where post_id = %s"
    sql2 = "delete from comment where id = %s"
    list = mysql.get_list(sql1, id)
    for i in list:
        mysql.delete(sql2, i['id'])
    mysql.delete(sql, id)
    return Jsonify.delete()
