"""
Poker hands
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

# Dirty code from internet
if __name__ == '__main__':

    import sys
    t,q,e,u='--23456789TJQKA','SDCH',enumerate,len
    _=lambda c,i=0:chr(97+c[i])
    def j(s):
     v,g,l=[0]*15,[0]*4,''
     for c in s:
      r,s=c[0],c[1];v[t.find(r)]+=1;g[q.find(s)]+=1
     c,h,k,m,f=0,0,[0,0,[],[],[]],0,0
     for x,i in e(v):
      for b in[2,3,4]:
       if i==b:k[b]+=[x]
     v[1]=v[14]
     for x,i in e(v):
      if i:
       c+=1
       if c==5:m,h=1,x
       if i==1:l+=_([x])
      else:c=0
     f,l,d=max(g)//5*2,l[::-1],'';z=f+m
     if z==3:d='z'+l
     if k[4]:d='y'+_(k[4])+l
     if k[2] and k[3]:d='x'+_(k[3])+_(k[2])
     if z==2:d='w'+l
     if z==1:d='v'+_([h])
     if k[3]:d='u'+_(k[3])+l
     if u(k[2])>1:d='t'+_(k[2],1)+_(k[2])+l
     if u(k[2])==1>u(k[3]):d='s'+_(k[2])+l
     return d or l

    res = 0
    with open('p054_poker.txt') as f:
        for line in f:
            hands = [x.strip('\n') for x in line.split(' ')]
            if j(hands[:5]) > j(hands[5:]):
                res += 1
    print(res)
