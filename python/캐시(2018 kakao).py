# LRU 알고리즘 - 캐시 교체 알고리즘
# LRU를 구현하기 위해서는 캐시가 가득 차서 더이상 공간이 없을 때, 가장 오랫동안 참조되지 않은 페이지를 찾아서 없애주는 작업이 필요하다.
# 즉, 참조하는 값이 캐시 안에 없다면 가장 오래 전에 참조한 값은 없애고 현재의 값을 캐시에 새로 넣어준다.
# 참조하는 값이 이미 캐시에 존재한다면 해당 값을 캐시의 가장 최근 위치로 넣어준다.
# -> deque 사용

from collections import deque

def solution(cacheSize, cities):
    buffer = deque(maxlen=cacheSize)
    total = 0

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()

        if city in buffer:
            total += 1
            buffer.remove(city)
            buffer.append(city)
        else:
            total += 5
            buffer.append(city)
    return total

