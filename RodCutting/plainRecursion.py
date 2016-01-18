#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def getMaxPrice(p,n):
  if(n==0):
    return 0
  else:
    #print n
    q=-10
    for i in range(1,n+1):
      q = max(q,p[i]+getMaxPrice(p,n-i))
    #print n,q
    return q

# Gather our code in a main() function
def main():
  p=[0,1,5,8,9,10,17,17,20,24,30]
  n = int(raw_input())
  print getMaxPrice(p,n)
  

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()