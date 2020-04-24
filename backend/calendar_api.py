from flask import jsonify, request, Blueprint, Response, Flask
from flask_app import app
from engine.get_info_from_db import get_mouth_info, get_day_info
import json
from flask_cors import CORS

CORS(app)


@app.route('/site_api/v1/month_data', methods=["GET"])
def month_data():
	"""
	月の動画情報の取得
	"""

	# リクエスパラメータを取得する
	year = request.args.get('year', '')
	month = request.args.get('month', '')

	# yearのチェック
	if not year:
		return jsonify(message='year(年)の指定をしてください'), 400
	elif not year.isdigit():
		return jsonify(message='year(年)は数字で指定してください!'), 400
	else:
		year = int(year)

	# monthのチェック
	if not month:
		return jsonify(message='month(月)の指定をしてください'), 400
	elif not month.isdigit():
		return jsonify(message='month(月)は数字で指定してください!'), 400
	else:
		month = int(month)

	# DB検索
	month_video_list = get_mouth_info(year, month)

	if not month_video_list:
		return jsonify(month_video_data=[]), 200
	else:
		return jsonify(month_video_data=month_video_list), 200


@app.route('/site_api/v1/day_data/<day>', methods=["GET"])
def day_data(day):
	"""
	日の動画情報の取得
	"""

	if not day.isdigit():
		return jsonify(message='日付は整数8桁(ex: 20200402)で指定してください!'), 400

	# DB検索
	day_video_list = get_day_info(day)

	if not day_video_list:
		return jsonify(day_video_datas=[]), 200
	else:
		return jsonify(day_video_datas=day_video_list), 200


app.run()
