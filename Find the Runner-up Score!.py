if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_list = sorted(arr)
    set_arr = set(sorted_list)
    set_arr.pop()
    runner_up = max(set_arr)
    print(runner_up)