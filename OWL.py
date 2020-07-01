import pandas as pd
import numpy as np

teams=[
'/overwatch/Atlanta_Reign',
'/overwatch/Boston_Uprising',
'/overwatch/Chengdu_Hunters',
'/overwatch/Dallas_Fuel',
'/overwatch/Florida_Mayhem',
'/overwatch/Guangzhou_Charge',
'/overwatch/Hangzhou_Spark',
'/overwatch/Houston_Outlaws',
'/overwatch/London_Spitfire',
'/overwatch/Los_Angeles_Gladiators',
'/overwatch/Los_Angeles_Valiant',
'/overwatch/New_York_Excelsior',
'/overwatch/Paris_Eternal',
'/overwatch/Philadelphia_Fusion',
'/overwatch/San_Francisco_Shock',
'/overwatch/Seoul_Dynasty',
'/overwatch/Shanghai_Dragons',
'/overwatch/Toronto_Defiant',
'/overwatch/Vancouver_Titans',
'/overwatch/Washington_Justice'
]

def player_hero_stats_per_10(player,hero,map_name,year,stage):
    player=str(player)
    hero=str(hero)
    map_name=str(map_name)
    year=int(year)
    if year in [2018,2019,2020]:
        if year==2020:
            phs=pd.read_csv(f'..\..\OWL\OWL_{year}\phs_{year}_1.csv')
        else:
            phs=pd.read_csv(f'..\..\OWL\OWL_{year}\phs_{year}_stage_{stage}.csv')
    else:
        phs=pd.read_csv(f'..\..\OWL\OWL_2020\phs_2020_stage_1.csv')
    if map_name.lower()=='all':
        all_maps=True
    else:
        all_maps=False
    stats=phs.loc[np.where(phs['player_name'].str.contains(player,case=False),True,False)]
    if not all_maps:
        stats=stats.loc[np.where(stats['map_name'].str.contains(map_name,case=False),True,False)]
    stats=stats.loc[np.where(stats['hero_name'].str.contains(hero,case=False),True,False)]
    time_played=stats.query("stat_name == 'Time Played'")['stat_amount'].sum()
    dumb_stats=['time','average','efficiency','accuracy','percent','rate']
    for i in dumb_stats:
        stats=stats.loc[np.where(stats['stat_name'].str.contains(i,case=False),False,True)]

    stat_names=stats.stat_name.unique()
    stat_sum=[0]*len(stat_names)

    for i in stat_names:
        stat_sum[np.where(stat_names==i)[0][0]]=round((stats.query("stat_name == '{}'".format(i))['stat_amount'].sum()*600/time_played),2)
    print(time_played)
    return stat_sum,stats,stat_names
	
[s,stats,names]=player_hero_stats_per_10('decay','Tracer','all',2020,1)
stats.to_csv('decay.csv',index=False)
