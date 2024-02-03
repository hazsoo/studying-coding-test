def solution(bandage, health, attacks):
    max_h = health
    end_time = attacks[-1][0]
    attacks = {attack[0]:attack[1] for attack in attacks}
    healing = 1

    for i in range(1,end_time+1):
        if i in attacks:
            healing = 1
            health -= attacks[i]
            if health <= 0:
                return -1
        else:
            health = min(max_h, health+bandage[1])
            if healing == bandage[0]:
                healing = 1
                health = min(max_h, health+bandage[2])
            else:
                healing += 1
    return health