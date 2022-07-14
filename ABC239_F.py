from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="239"
#問題
problem="f"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import deque
  def bfs(G,s,k):
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      used[x]=k
      for y in G[x]:
        if used[y]==-1:
          dq.append(y)
  N,M=map(int,input().split())
  D=list(map(int,input().split()))
  G=[[] for i in range(N)]
  for i in range(M):
    A,B=map(lambda x: int(x)-1, input().split())
    G[A].append(B)
    G[B].append(A)
  D=[D[i]-len(G[i]) for i in range(N)]
  if min(D)<0: print(-1)
  else:
    used=[-1]*N
    k=0
    for i in range(N):
      if used[i]==-1:
        bfs(G,i,k)
        k+=1
    kouho=[[] for i in range(k)]
    for i in range(N):
      for j in range(D[i]):
        kouho[used[i]].append(i)
    kouho.sort(key=lambda x: -len(x))
    ans=[]
    r=kouho[0]
    flg=0
    for i in range(len(kouho)-1):
      if len(r)==0 or len(kouho[i+1])==0: flg=1; break
      ans.append((r.pop()+1,kouho[i+1].pop()+1))
      while kouho[i+1]:
        x=kouho[i+1].pop()
        r.append(x)
    if len(r)!=0 or flg==1:print(-1)
    else:
      for i in range(len(ans)):
        print(*ans[i])
  """ここから上にコードを記述"""

  print(test_case[__+1])