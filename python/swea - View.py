for i in range(1, 11):
    N = int(input())
    building_height_arr = list(map(int, input().split()))
    cnt = 0
    for j in range(2, len(building_height_arr)-1):
        left_max_value = max(building_height_arr[j-2:j])
        right_max_vaule = max( building_height_arr[j+1:j+3])
        max_value = max(left_max_value, right_max_vaule)
        if building_height_arr[j] > max_value:
            cnt += building_height_arr[j] - max_value
    print(cnt)