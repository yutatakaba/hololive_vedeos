from engine.info_db import db_info
import calendar
import datetime


def get_mouth_info(year, month):
  """
  月の動画データの取得
  :param year: 検索する年
  :param month: 検索する月
  :return: 日にちをkeyとして、その日の動画のリスト(中身は辞書)をvalueとした辞書(動画がない日はからのリスト)
  ex:
  [
    {
      videos: [
                {'video_owner': '星街すいせい', 'name_color': {color: 'blue'}},
                {'video_owner': '潤羽るしあ', 'name_color': 'font-color: greenyellow'}
              ],
      api_day: 20200401,
      day: 1
    },
    {},
    {
      videos: {'video_owner': '星街すいせい', 'name_color': 'font-color: blue'}
      day: 3
    }
    ...
  ]
  """
  day_list = []
  for i in range(calendar.monthlen(year, month)):
    owner_list = []
    day_video_list = []
    day = i + 1
    db_info.execute(
      "SELECT day, video_owner, name_color FROM video_data "
      "where year = {} and month = {} and day = {}".format(year, month, day)
    )
    month_data = db_info.fetchall()
    # print(month_data)
    for day_data in month_data:
      if day_data[1] in owner_list:
        continue
      else:
        video_dict = {
          "video_owner": day_data[1],
          "name_color": {
            "color": day_data[2]
          }
        }
        owner_list.append(day_data[1])
      day_video_list.append(video_dict)
    day_dict = {
      "video": day_video_list,
      "api_day": int(str(year) + str(month).zfill(2) + str(day).zfill(2)),
      "day": day
    }
    day_list.append(day_dict)

  return day_list


def get_day_info(day):
  """
  特定日の動画データの取得
  :param day: 検索する日
  :return: 日の動画データのリスト(リストの中身は辞書)
  ex:
  [
    {
       'title': '【あつ森】リスナーの島に凸して荒らす【ホロライブ / #夏街すいり】',
       'year': 2020,
       'month': 4,
       'day': 12,
       'url': 'https://i.ytimg.com/vi/vsJ5Q27M0fQ/hqdefault.jpg',
       'channel_name': 'Suisei Channel',
       'channel_url': 'https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A',
       'collaboration_flag': 0,
       'collaboration_member': '',
       'video_owner': '星街すいせい'
    },
    {
       'title': '【テトリス99】清楚でプレイすればスナイパーが動揺してVIP1位簡単に取れる説【ホロライブ / 星街すいせい】',
       'year': 2020,
       'month': 4,
       'day': 12,
       'url': 'https://i.ytimg.com/vi/j1Rrg4BnBjs/hqdefault.jpg',
       'channel_name': 'Suisei Channel',
       'channel_url': 'https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A',
       'collaboration_flag': 0,
       'collaboration_member': '',
       'video_owner': '星街すいせい'
    },
    {
       'title': '【公式】『星街すいせいのMUSIC SPACE』 #01 前半（2020年4月5日放送分）',
       'year': 2020,
       'month': 4,
       'day': 12,
       'url': 'https://i.ytimg.com/vi/zPRpfK7a2I0/hqdefault.jpg',
       'channel_name': 'Suisei Channel',
       'channel_url': 'https://www.youtube.com/channel/UC5CwaMl1eIgY8h02uZw7u8A',
       'collaboration_flag': 0,
       'collaboration_member': '',
       'video_owner': '星街すいせい'
    }
  ]
  """
  date_data = datetime.datetime.strptime(day, '%Y%m%d')
  day_video_list = []
  db_info.execute(
    "SELECT title, year, month, day, url, channel_name, channel_url, collaboration_flag, collaboration_member, "
    "video_owner FROM video_data where year = {} and month = {} and day = {}".format
    (date_data.year, date_data.month, date_data.day)
  )
  day_data = db_info.fetchall()
  for video_data in day_data:
    video_dict = {
      "title": video_data[0],
      "year": video_data[1],
      "month": video_data[2],
      "day": video_data[3],
      "url": video_data[4],
      "channel_name": video_data[5],
      "channel_url": video_data[6],
      "collaboration_flag": video_data[7],
      "collaboration_member": video_data[8],
      "video_owner": video_data[9]
    }
    day_video_list.append(video_dict)

  return day_video_list


if __name__ == "__main__":
  print(get_mouth_info(2020, 4))
