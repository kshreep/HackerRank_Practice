import heapq

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(heapq.nlargest(2, set(arr))[1])
