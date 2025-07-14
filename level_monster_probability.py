import random

# 몬스터의 종류와 주요 등장 레벨
monster_data = {
    "Slime": {"main_level": 1},
    "Goblin": {"main_level": 3},
    "Orc": {"main_level": 5},
    "Troll": {"main_level": 8},
    "Dragon": {"main_level": 12}
}

# player_level, monster_data 기반으로 몬스터 별 등장확률 구하기
def Spawn_probability(player_level):
    # 각각의 몬스터의 등장 점수
    scores = {}

    # 전체 몬스터의 등장 점수
    total_score = 0

    # 몬스터의 등장 비율
    prob = {}

    # name에는 몬스터 이름, value에는 이름이 각각 들어감
    for monster_name, monster_value in monster_data.items():
        # 몬스터 등장레벨과 플레이어 레벨의 차이값
        level_gap = abs(player_level - monster_value["main_level"])

        # 차이값이 적을 수록 높은 점수, 차이 4 이상은 점수 없음
        score = max(0, 4 - level_gap)

        # 현재 몬스터의 점수를 딕셔너리로 저장
        scores[monster_name] = score

        # 전체 몬스터 점수 총합을 저장
        total_score += score

    # 점수를 백분율로 환산
    for monster_name in scores:
        prob[monster_name] = round((scores[monster_name] / total_score) * 100)
    
    return prob

# 확률 적용하기
def Select_monster(player_level):

    # 등장 확률 가져오기
    prob = Spawn_probability(player_level)

    # 몬스터의 이름 리스트
    monster_name = list(prob.keys())

    # 몬스터의 등장 확률 리스트 
    monster_weights = list(prob.values())

    # 이름, 확률을 기반으로 몬스터 랜덤 결정
    select_monster = random.choices(monster_name, weights = monster_weights, k = 1)
    return select_monster

# 실행
level = 4
print(Select_monster(level))