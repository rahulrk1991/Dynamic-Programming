#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def getMaxPriceHelper(p,n,memo):
    for i in range(1,n+1):
        q=-10
        for j in range(1,i+1):
            q=max(q,p[j]+memo[i-j])
        memo[i]=q
    return memo[n]

def getMaxPrice(p,n):
  memo = [-1]*11
  memo[0]=0
  return getMaxPriceHelper(p,n,memo)

# Gather our code in a main() function
def main():
  p=[0,1,5,8,9,10,17,17,20,24,30]
  n = int(raw_input())
  print getMaxPrice(p,n)
  

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()