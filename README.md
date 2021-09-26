# class_to_calendar_csv

## 概要

大学の時間割からGoogle Calendarに読みこませるcsvファイルを作成するプログラム

## 動作保証環境

- Python 3.9
- pip 21.2.4

## 使用方法

1. 必要なパッケージのインストール
```shell
$ pip install -r requirements.txt
```

または,venvを用いても良い.
```shell
$ python3 -m venv <環境名>
$ source <環境名>/bin/activate
$ pip install -r requirements.txt
$ deactivate
```

2. `main.py`を必要に応じて書き換える

3. csvファイルを出力
```shell
$ python3 ./main.py
```

4. `main.py`と同じディレクトリに`curricula_schedule.csv`が作成されるので,これをGoogle Calendarに読み込ませる