def solution(participant, completion):
    d = {}
    for part in participant:
        d[part] = d.get(part, 0) + 1

    for comp in completion:
        d[comp] -= 1

    return ''.join([name for name, cnt in d.items() if cnt > 0])