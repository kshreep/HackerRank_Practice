if __name__ == "__main__":
  N = input()
  s = set(map(int, input().split()))
  for _ in range(int(input())):
    args = input().split()
    sec_set = set(map(int, input().split()))
    if args[0] == "intersection_update":
      s.intersection_update(sec_set)
    if args[0] == "update":
      s.update(sec_set)
    if args[0] == "symmetric_difference_update":
      s.symmetric_difference_update(sec_set)
    if args[0] == "difference_update":
      s.difference_update(sec_set)
  
  print(sum(s))

"""
-------------------------------------------
if __name__ == '__main__':
    (_, A) = (int(input()),set(map(int, input().split())))
    B = int(input())
    for _ in range(B):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        getattr(A, command)(newSet)

    print (sum(A))
-------------------------------------------

