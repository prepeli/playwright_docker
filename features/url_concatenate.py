import urllib.parse

price_min = ''
price_max = '5000000'
deadline = '12'
age_min = ''
age_max = ''
skill_goalie_min = ''
skill_goalie_max = '5'
speed_min = ''
speed_max = ''
quality_min = ''
quality_max = ''
skill_defense_min = ''
skill_defense_max = ''
strength_min = ''
strength_max = ''
potential_min = '6'
potential_max = ''
skill_attack_min = ''
skill_attack_max = ''
selfcontrol_min = ''
selfcontrol_max = ''
experience_min = ''
experience_max = ''
skill_shot_min = ''
skill_shot_max = ''
passing_min = ''
passing_max = ''
aindex_min = '370'
aindex_max = ''
cat2 = '2'
nationality_id = ''

params = {
    'price_min': price_min,
    'price_max': price_max,
    'deadline': deadline,
    'age_min': age_min,
    'age_max': age_max,
    'skill_goalie_min': skill_goalie_min,
    'skill_goalie_max': skill_goalie_max,
    'speed_min': speed_min,
    'speed_max': speed_max,
    'quality_min': quality_min,
    'quality_max': quality_max,
    'skill_defense_min': skill_defense_min,
    'skill_defense_max': skill_defense_max,
    'strength_min': strength_min,
    'strength_max': strength_max,
    'potential_min': potential_min,
    'potential_max': potential_max,
    'skill_attack_min': skill_attack_min,
    'skill_attack_max': skill_attack_max,
    'selfcontrol_min': selfcontrol_min,
    'selfcontrol_max': selfcontrol_max,
    'experience_min': experience_min,
    'experience_max': experience_max,
    'skill_shot_min': skill_shot_min,
    'skill_shot_max': skill_shot_max,
    'passing_min': passing_min,
    'passing_max': passing_max,
    'aindex_min': aindex_min,
    'aindex_max': aindex_max,
    'cat2': cat2,
    'nationality_id': nationality_id
}

# Filter out empty parameters (if v = NULL it won't be added to the URL)
params = {k: v for k, v in params.items() if v}


query_string = urllib.parse.urlencode(params)
freeagent_url = f'https://www.hockeyarena.net/en/index.php?p=manager_player_market_sql.php&{query_string}'
#testprint
print(freeagent_url)
#await page.goto(url)

