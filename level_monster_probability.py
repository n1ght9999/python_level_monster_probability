import random

# 몬스터의 종류와 주요 등장 레벨
monster_data = {
    "Slime": {"main_level": 1},
    "Goblin": {"main_level": 3},
    "Orc": {"main_level": 5},
    "Troll": {"main_level": 8},
    "Dragon": {"main_level": 12}
}

# player_level, monster_data 기반으로 몬스터 별 등장점수 구하기
def spawn_probability(player_level):
    # 각각의 몬스터의 등장 점수
    scores = {}

    # name에는 몬스터 이름, value에는 이름이 각각 들어감
    for monster_name, monster_value in monster_data.items():

        # 몬스터 등장레벨과 플레이어 레벨의 차이값
        level_gap = abs(player_level - monster_value["main_level"])

        # 차이값이 적을 수록 높은 점수, 차이 4 이상은 점수 없음
        score = max(0, 4 - level_gap)

        # 현재 몬스터의 점수를 딕셔너리로 저장
        scores[monster_name] = score
    
    return scores

#  적용하기
def select_monster(player_level):

    # 등장 점수 가져오기
    scores = spawn_probability(player_level)

    # 몬스터의 이름 리스트
    monster_name = list(scores.keys())

    # 몬스터의 등장 점수 리스트 
    monster_weights = list(scores.values())

    # 점수를 기반으로 몬스터 랜덤 결정
    select_monster = random.choices(monster_name, weights = monster_weights, k = 1)[0]
    return select_monster

# 실행
level = 4
print(select_monster(level))