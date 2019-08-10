if __name__ == '__main__':
  N = int(input())
  res = []
  for i in range(N):
    ip = input()    
    if ip.startswith("insert"):
      res.insert(int(ip.split()[1]),int(ip.split()[2]))
    if ip.startswith("remove"):
      res.remove(int(ip.split()[1]))
    if ip.startswith("append"):
      res.append(int(ip.split()[1]))
    if ip.startswith("sort"):
      res.sort()
    if ip.startswith("reverse"):
      res.reverse()
    if ip.startswith("pop"):
      res.pop()
    if ip.startswith("print"):
      print(res)
  
"""
Other Solutions
--------------------------------------------------
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")" 
        eval("l."+cmd)
    else:
        print l

---------------------------------------------------
eval('arr.{0}{1}'.format(cmd,tuple(map(int,arg))))

"""