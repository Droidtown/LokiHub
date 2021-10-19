import discord
import json
import pandas as pd
import numpy as np
import pandasql as ps
from datapuller import DataPuller
from nba_search import *

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())


info_fields = {'season': None,
                'team': None,
                'player': None,
                'stat': None,
                'level': None} 

statDICT = {'pts':['得分'], 
            'reb':['籃板', '搶籃板'], 'ast':['助攻'], 
            'blk':['阻攻', '火鍋', '蓋火鍋','搧帽', '蓋帽'], 
            'stl':['抄截']}


msg = '2018賽季 Aaron Gordon 單場最高籃板'
#msg = '2020球季魔術隊單場籃板最多是誰'
#msg = '2019公牛隊平均得分最多的球員'
print(msg)
            


df = pd.read_csv('./media/data.csv')

msg, info_fields = get_playername(msg, info_fields)
msg, info_fields = get_season(msg, info_fields)        


print(msg, 'msg')

filterLIST = []
resultDICT = runLoki([msg], filterLIST)   



if len(resultDICT['team']) > 0:
    info_fields['team'] = resultDICT['team'][0]
    team = resultDICT['team'][0]
else:
    team = ''
# try:
#     info_fields['team'] = resultDICT['team'][0]
# except:
#     pass
print(resultDICT)

info_fields['stat'] = resultDICT['stat'][0]
info_fields['level'] = resultDICT['level']

print(info_fields, "here")

if info_fields['player'] and info_fields['level'] == 'avg':
    qry = DataPuller.get_player_agg_stats(info_fields['stat'], 
                                          info_fields['player'], 
                                          info_fields['season'])

elif info_fields['player'] and info_fields['level'] == 'single':
    qry = DataPuller.get_player_single_game_stats(info_fields['stat'], 
                                                  info_fields['player'], 
                                                  info_fields['season'])
elif info_fields['team']:
    qry = DataPuller.get_team_best_player_stats(info_fields['stat'], 
                                                info_fields['team'], 
                                                info_fields['season'])

else:
    raise ValueError('invalid input') 

result = ps.sqldf(qry, locals())

print(result)

aa = statDICT[info_fields['stat']][0]
print(aa)

bb = result['target_stat'].iloc[0]
print(bb)

print(info_fields)



reply_message = str(info_fields['season']) + ' ' + team + ' ' + result['player_name'] + ' ' + info_fields['level'] + ' ' + statDICT[info_fields['stat']][0] + ' ' + str(round(result['target_stat'].iloc[0], 1))



print(reply_message)


















# df = pd.read_csv('./media/data.csv')

# for name in list(set(df['player_name'])):
#     if name in msg:
#         info_fields['player'] = name
#         msg = msg.replace(name, '').strip()
        
# for season_key in seasonDICT.keys():
#     for year in seasonDICT[season_key]:
#         if year in msg:
#             info_fields['season'] = season_key
#             msg = msg.replace(year, '').strip()

# filterLIST = []
# resultDICT = runLoki([msg], filterLIST)   

# print(resultDICT)


# try:
#     info_fields['team'] = resultDICT['team'][0]
# except:
#     pass

# info_fields['stat'] = resultDICT['stat'][0]
# info_fields['level'] = resultDICT['level']

# print(info_fields)

# if info_fields['player'] and info_fields['level'] == 'avg':
#     qry = DataPuller.get_player_agg_stats(info_fields['stat'], 
#                                           info_fields['player'], 
#                                           info_fields['season'])

# elif info_fields['player'] and info_fields['level'] == 'single':
#     qry = DataPuller.get_player_single_game_stats(info_fields['stat'], 
#                                                   info_fields['player'], 
#                                                   info_fields['season'])
# elif info_fields['team']:
#     qry = DataPuller.get_team_best_player_stats(info_fields['stat'], 
#                                                 info_fields['team'], 
#                                                 info_fields['season'])

# else:
#     raise ValueError('invalid input') 




# result = ps.sqldf(qry, locals())

# print(result)

# reply_message = info_fields['season'] + ' ' + result['team'].iloc[0] + ' ' + \
#                 info_fields['player'] + ' ' + info_fields['level'] + ' game ' + \
#                 statDICT[info_fields['stat']][0] + ' ' + str(round(result['target_stat'].iloc[0], 1))
#               #+ info_fields['level'] + ' ' \ #   + statDICT[info_fields['stat'][0]] + ': ' 

# print(reply_message)
    


