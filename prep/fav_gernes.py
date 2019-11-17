def fav_gernes(userSongs, songGenres):
    dic = {}
    for key in songGenres:
        for song in songGenres[key]:
            dic[song] = key

    res = collections.defaultdict(list)
    for key in userSongs:
        count = collections.defaultdict(int)
        for song in userSongs[key]:
            if song in dic:
                count[dic[song]] += 1
        if count:
            most = max(count.values())
            for key2 in count:
                if count[key2] == most:
                    res[key].append(key2)
        else:
            res[key] = []

    return res
