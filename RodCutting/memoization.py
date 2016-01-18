#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def getMaxPrice(p,n,memo):
  if(n==0):
    return 0
  if(memo[n]!=-1):
    return memo[n]
  else:
    q=-10
    for i in range(1,n+1):
      q = max(q,p[i]+getMaxPrice(p,n-i,memo))
    memo[n]=q
    return q

# Gather our code in a main() function
def main():
  p=[0,1,5,8,9,10,17,17,20,24,30]
  n = int(raw_input())
  memo = [-1]*11
  print getMaxPrice(p,n,memo)
  

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()