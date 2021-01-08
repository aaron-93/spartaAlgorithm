genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 장르별 총 재생된 횟수
    genre_total_play_dict = {}
    n = len(genre_array)
    # 장르별 각 곡의 재생된 횟수
    genre_idx_play_array_dict = {}
    # 장르 별(key) 재생된 횟수(value)
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        # 초기 dict은 None이기 때문에 dict에 장르를 추가해 줌
        if genre not in genre_total_play_dict:
            # {장르 : 총 재생 횟수} 설정
            genre_total_play_dict[genre] = play
            # 장르별 각 곡(classic1,2,3, pop 1,2)의 인덱스 i 와 재생된 횟수를 추가해줌
            genre_idx_play_array_dict[genre] = [[i,play]]
        else:
            # 장르가 이미 기록되어 있다면 재생된 횟수를 더해줌
            genre_total_play_dict[genre] += play
            # 장르별 각 곡의 인덱스와 재생된 횟수를 추가해줌
            genre_idx_play_array_dict[genre].append([i,play])


    # {장르: 총 재생된 횟수} 를 내림차순으로 정렬
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1],reverse=True)



    # 결과값을 담을 배열
    result = []

    for genre, _value in sorted_genre_play_array:
        # 아래 식 = sorted_genre_play_array -> [[1], 600, [4, 2500]]

        index_play_array = genre_idx_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)


        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result

print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!