# Есть словарь песен группы Depeche Mode violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection':
# 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of
# Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, } Выведите общее время звучания всех песен. Создайте список
# песен, время звучаниях которых больше 5 минут Создайте новый словарь тех песен, в название которых состоит из
# одного слова
violator_songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
                      'Waiting for the Night': 6.07,
                      'Enjoy the Silence': 4.6, "Policy of Truth": 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}


def songs():
    total = 0
    list_of_songs = []
    list_of_keys = []
    list_of_values = []
    dict_of_songs = {}
    for value in violator_songsdict.values():
        total += value
    for key, value in violator_songsdict.items():
        if value > 5:
            list_of_songs.append(key)
        if len(key.split()) == 1:
            list_of_keys.append(key)
            list_of_values.append(value)
        dict_of_songs = dict(zip(list_of_keys, list_of_values))

    return print(f'Общая продолжительность песен равна - {total}\nПесни больше пяти минут - {list_of_songs}\nПесни '
                 f'состоящие из одного слова - {dict_of_songs}')


songs()
