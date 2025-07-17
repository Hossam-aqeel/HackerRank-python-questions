if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    av = 0
    for i in range(3):
        av = av + (student_marks[query_name][i])/3
    print(f"{av:.2f}")