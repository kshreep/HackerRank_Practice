import collections
if __name__ == '__main__':
  (_, counts) = (input(), collections.Counter(input().split()))
  print(min(counts, key = counts.get))