from collections import defaultdict
from typing import List, Tuple

def recommend_friends(listens: List[Tuple[int, int, str]], friendships: List[Tuple[int, int]]):
    listens = set(listens)
    song_users = defaultdict(list)

    for user_id, song_id, day in listens:
        song_users[(day, song_id)].append(user_id)

    # (user1, user2, day) -> number of common songs
    common_count = defaultdict(int)

    for (day, song_id), users in song_users.items():
        users = list(set(users))

        for i in range(len(users)):
            for j in range(len(users)):
                if i == j:
                    continue

                u = users[i]
                v = users[j]

                common_count[(u, v, day)] += 1

    friends = {
        (min(u,v), max(u,v)) for u, v in friendships
    }

    result = set()

    for (u,v, day), count in common_count.items():
        if count >= 3:
            if (min(u,v), max(u,v)) not in friends:
                result.add((u, v))

    return list(result)

listens = [
    (1, 10, "2026-01-01"),
    (1, 20, "2026-01-01"),
    (1, 30, "2026-01-01"),

    (2, 10, "2026-01-01"),
    (2, 20, "2026-01-01"),
    (2, 30, "2026-01-01"),

    (3, 10, "2026-01-01"),
    (3, 20, "2026-01-01"),
    (3, 30, "2026-01-01"),
]

friendships = [
    (1, 3)
]

print(recommend_friends(listens, friendships))