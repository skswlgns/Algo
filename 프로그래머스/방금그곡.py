def solution(m, musicinfos):
    m = m.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('F#', 'f').replace('G#',
                                                                                                                 'g').replace(
        'A#', 'a')

    result = []
    for i in musicinfos:
        start, end, title, sound = i.split(',')
        sound = sound.replace('C#', 'c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('F#',
                                                                                                          'f').replace(
            'G#', 'g').replace('A#', 'a')
        temp_start = []
        temp_end = []
        for time in start.split(':'):
            temp_start.append(int(time))
        for time_end in end.split(':'):
            temp_end.append(int(time_end))
        real_time = (temp_end[0] - temp_start[0]) * 60 + (temp_end[1] - temp_start[1])
        repeat = real_time // len(sound)
        mod = real_time % len(sound)
        sound = sound * repeat + sound[0:mod]
        if m in sound:
            temp = [title, len(sound)]
            result.append(temp)
    max_value = 0
    if len(result) == 0:
        answer = "(None)"
    else:
        for z in result:
            if max_value < z[1]:
                max_value = z[1]
                answer = z[0]

    return answer