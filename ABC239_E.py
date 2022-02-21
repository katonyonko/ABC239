from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="239"
#問題
problem="e"

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
  #オイラーツアー
  def EulerTour(G, s):
      depth=[-1]*len(G)
      depth[s]=0
      done = [0]*len(G)
      Q = [~s, s] # 根をスタックに追加
      parent=[-1]*len(G)
      ET = []
      left=[-1]*len(G)
      while Q:
          i = Q.pop()
          if i >= 0: # 行きがけの処理
              done[i] = 1
              if left[i]==-1: left[i]=len(ET)
              ET.append(i)
              for a in G[i][::-1]:
                  if done[a]: continue
                  depth[a]=depth[i]+1
                  parent[a]=i
                  Q.append(~a) # 帰りがけの処理をスタックに追加
                  Q.append(a) # 行きがけの処理をスタックに追加
          else: # 帰りがけの処理
              ET.append(parent[~i])
      return ET[:-1], left, depth, parent
  N,Q=map(int,input().split())
  X=list(map(int,input().split()))
  G=[[] for _ in range(N)]
  for i in range(N-1):
    A,B=map(int,input().split())
    A-=1; B-=1
    G[A].append(B)
    G[B].append(A)
  query=[[] for _ in range(N)]
  ans=[-1]*Q
  for i in range(Q):
    V,K=map(int,input().split())
    V-=1
    ET, left, depth, parent=query[V].append((K,i))
  EulerTour(G,0)
  """ここから上にコードを記述"""

  print(test_case[__+1])