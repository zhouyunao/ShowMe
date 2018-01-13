

```python
import sqlite3
```


```python
import pandas as pd
import csv
import pandas.io.sql as psql
```


```python
dbname = '2017.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# cur.execute(""" CREATE TABLE Schedule_E  (日時 text, text曜日,対戦相手 text, playground text,start text,audience int,result text,
# get int,lost int,ab int,hit int, hr int,steal int,error int,offense int,inning int,hitted int,hred int,
# walkHBP int,ER int,HA int,cardNo int,ND int,Bye int)""")


```


```python
cur.execute(""" CREATE TABLE Schedule_E  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_Bs  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_C  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_D  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_DB  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_F  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_G  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_H  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_L  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_M  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_T  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")

cur.execute(""" CREATE TABLE Schedule_Ys  (日時 text,曜日 text,相手 text, 球場 text,開始 text,観衆 int,勝敗 text,
得 int,失 int,打数 int,安打 int,本塁 int,盗塁 int,失策 int,攻撃 int,回数 int,被安 int,被本 int,
四死球 int,自責 int,HA int,カ int,ナ int,サ int)""")
```




    <sqlite3.Cursor at 0x7f711f9392d0>




```python
import glob
```


```python
file_list = glob.glob('data_2017/*.csv')
# for fn in file_list:
#     print(fn[10:-4])
```

    Schedule_Bs_2017
    Schedule_C_2017
    Schedule_DB_2017
    Schedule_D_2017
    Schedule_F_2017
    Schedule_G_2017
    Schedule_H_2017
    Schedule_L_2017
    Schedule_M_2017
    Schedule_T_2017
    Schedule_Ys_2017



```python
for filename in file_list:
    df = pd.read_csv(filename,encoding='shift_jis')
    name = filename[10:-9]
    df.to_sql(name,conn,if_exists='append',index=None)
```


```python
# 1回 数字はダメっぽい``を付けました。
cur.execute(""" CREATE TABLE score_all (FLG text,日付 text,TM text,`1回` int,`2回` int,`3回` int,`4回` int,`5回` int,`6回` int,`7回` int,`8回` int,`9回` int,`10回` int,`11回` int,`12回` int,計 int,安 int,失 int)""")
```




    <sqlite3.Cursor at 0x7f711f939a40>




```python
cur.execute(""" CREATE TABLE batting_by_pitch (日付 text,球場 text,自TM text,打者 text,席 text,結果 text,相手TM text,投手 text,腕 text)""")
```




    <sqlite3.Cursor at 0x7f711f939a40>




```python
df1 = pd.read_csv('data_2017/score_all_2017.csv',encoding='shift_jis')
df1.to_sql('score_all',conn,if_exists='append',index=None)
```


```python
# UnicodeDecodeError: 'shift_jis' codec can't decode byte 0xfb in position 0: illegal multibyte sequence
import codecs
with codecs.open('data_2017/bt_all_by_pc_stat_all_2017.csv','rb','Shift_JIS','ignore') as file:
    df = pd.read_table(file,delimiter=",")
    df.to_sql('batting_by_pitch',conn,if_exists='append',index=None)
```


```python
with codecs.open('data_2017/fp_box_all_data_2017.csv','rb','Shift_JIS','ignore') as file:
    df = pd.read_table(file,delimiter=",")
    df.to_sql('full_play',conn,if_exists='append',index=None)
```


```python
with codecs.open('data_2017/bt_all_by_pc_stat_all_2017.csv','rb','Shift_JIS','ignore') as file:
    df = pd.read_table(file,delimiter=",")
    df.to_sql('batting_result',conn,if_exists='append',index=None)
```
