def change(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = ''
    maxPlayTime = 0
    m = change(m)

    for i in musicinfos:
        startTime, endTime, title, melody = i.split(',')
        playTime = (int(endTime[:2]) * 60 + int(endTime[3:])) - (int(startTime[:2]) * 60 + int(startTime[3:]))
        melody = change(melody)

        if playTime <= len(melody):
            melody = melody[:playTime]
        else:
            while True:
                melody = melody * 2
                if playTime <= len(melody):
                    melody = melody[:playTime]
                    break

        if m in melody and playTime > maxPlayTime:
            maxPlayTime = playTime
            answer = title

    if answer == '':
        answer = "(None)"

    return answer
