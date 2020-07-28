# -*- coding: UTF-8 -*-

from flask import render_template, request, jsonify
import logging
from Dance import app

@app.route("/")
def init_config_page():
    return render_template("index.html", **locals())


@app.route("/Request01")
def request01():
    try:
        return jsonify(dict(err=0, msg="Y R U so diao", data={"a": 111}))
    except Exception as e:
        strLog = "[views]ERROR in Request01: %s" % e.__str__()
        logging.error(strLog)

        return jsonify(dict(err=1, msg="获取失败", data={}))


@app.route("/Request02", methods=["POST"])
def request02():
    try:
        rcv = request.get_json()
        param01 = str(rcv.get("param01")) if rcv.get("param01") is not None else None
        param02 = str(rcv.get("param02")) if rcv.get("param02") is not None else None

        if not param01:
            return jsonify(dict(err=1, msg="param01 不能为空", data=False))
        if not param02:
            return jsonify(dict(err=1, msg="param02 不能为空", data=False))

        return jsonify(dict(err=0, msg="Y R U so diao", data={"a": 111}))

    except Exception as e:
        strLog = "[views]ERROR in Requst02: %s" % e.__str__()
        logging.error(strLog)
        return jsonify(dict(err=1, msg="获取失败", data=False))

