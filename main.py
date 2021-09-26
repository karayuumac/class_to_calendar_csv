import datetime

import pandas as pd


# 時限と開始時間・終了時間の対応
def period_to_time(period: int):
  if period == 1:
    return {
      "Start Time": "9:00",
      "End Time": "10:30"
    }
  elif period == 2:
    return {
      "Start Time": "10:40",
      "End Time": "12:10"
    }
  elif period == 3:
    return {
      "Start Time": "13:10",
      "End Time": "14:40"
    }
  elif period == 4:
    return {
      "Start Time": "14:50",
      "End Time": "16:20"
    }
  elif period == 5:
    return {
      "Start Time": "16:30",
      "End Time": "18:00"
    }


curricula = [
  # 例
  {"Subject": "法学", "weekday": 0, "period": 1, "Location": "XX教室"}
  # period は時限を表す. weekday は0が月曜日,1が火曜日...6が日曜日を表す.
  # この例なら,月曜1限に法学がXX教室で行われることを意味する.
]

# 1科目あたり,何時間あるか
total_number_of_lessons = 15

# 授業のない日
exclude_date = [
  # 冬季休暇
  datetime.date(2021, 12, 26),
  datetime.date(2021, 12, 27),
  datetime.date(2021, 12, 28),
  datetime.date(2021, 12, 29),
  datetime.date(2021, 12, 30),
  datetime.date(2021, 12, 31),
  datetime.date(2022, 1, 1),
  datetime.date(2022, 1, 2),
  datetime.date(2022, 1, 3),
  datetime.date(2022, 1, 4),
  datetime.date(2022, 1, 5),
  datetime.date(2022, 1, 6),
  # 成人の日
  datetime.date(2022, 1, 10),
  # 共通テスト準備日
  datetime.date(2022, 1, 14),
  # 共通テスト
  datetime.date(2022, 1, 15),
  datetime.date(2022, 1, 16),
]

# 授業が始まる日
start_day = datetime.date(2021, 9, 27)

df = pd.DataFrame(columns=["Subject", "Start Date", "End Date", "Start Time", "End Time", "Location", "Private"])

for curriculum in curricula:
  diff_days = curriculum["weekday"] - start_day.weekday() if start_day.weekday() <= curriculum["weekday"] \
    else curriculum["weekday"] + 7 - start_day.weekday()

  diff = datetime.timedelta(days=diff_days)
  first_day = start_day + diff

  week = 1
  stopper = total_number_of_lessons
  while week <= stopper:
    day = first_day + datetime.timedelta(days=7 * (week - 1))
    if not day in exclude_date:
      day_str = day.strftime("%Y/%m/%d")
      time = period_to_time(curriculum["period"])
      row = pd.DataFrame(
        [[curriculum["subject"], day_str, day_str, time["Start Time"], time["End Time"], curriculum["location"],
          "TRUE"]],
        columns=df.columns
      )
      df = df.append(row, ignore_index=True)
    else:
      stopper += 1
    week += 1

df.to_csv("./curricula_schedule.csv", index=False)
