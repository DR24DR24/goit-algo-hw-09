def find_coins_greedy(coins, sum):
    coinSet={}
    i=0
    while i<len(coins):
        if coins[i]<=sum:
            coinSet[coins[i]]= coinSet[coins[i]]+1 if coins[i] in coinSet else 1
            sum-=coins[i]
        else:
            i+=1
    return sum, coinSet 

coins=[7, 6]    

print(find_coins_greedy(coins,12))

# def coin_set_parameters(coin_set):
#     s=0
#     for i,val in coin_set.items():
#         s+=val
#     return len(coin_set), s



def find_min_coins(coins,val):
    """ The algorithm is designed for an infinite number of coins of each denomination.
 The algorithm is designed, among other things, 
 for situations when not any sum can be composed of existing coin denominations
Table K is one-dimensional
The main idea of ​​the algorithm is that starting with the smallest sum,
 we try to find the optimal combination of coins at each step (in a cycle by sum).
We try to add all of the existing coin denominations in turn. When we add another coin, 
we add the coin to the set of coins that are in the cell of table k 
under the number "current sum subtract denominations of the coin in question" 
As an alternative to this, it is proposed to simply take the data 
from the previous cell of table k.
When we compare which situation is better, we take into account two factors.
 First, the sum of coins should be as large as possible and the second factor is that
   the number of coins should be as small as possible.
This algorithm gives the correct answer in the case when the greedy algorithm fails. 
I even got the impression that this algorithm gives no worse results 
than the exhaustive search algorithm.
Perhaps this algorithm can be accelerated in the spirit of trying 
to add a new coin starting with the largest one. 
And as soon as we get the result that the sum of coins is equal to the current sum,
 then for the remaining coins in this cycle, 
 the remaining coins are not checked by the sum
"""
    n=len(coins)
    K = [{"sum":0,"coinNumber":0,"coinSet":{coins[i]:0 for i in range(n)}}\
           for s in range(val + 1)\
        ]
    for s in range(1,val+1):
            options=[(K[s - coins[i]]["sum"       ]+coins[i],\
                      K[s - coins[i]]["coinNumber"]-1,\
                      i\
                     ) \
                     for i in range(n) if coins[i]<=s]
            maxOption=max(options,default=\
                          (K[s - 1]["sum"       ],\
                           K[s - 1]["coinNumber"],\
                           n\
                          ) \
                         )
            K[s]["sum"       ]=maxOption[0]
            K[s]["coinNumber"]=maxOption[1]
            if maxOption[2]<n:
                 K[s]["coinSet"   ]=K[s-coins[maxOption[2]]]["coinSet"   ].copy()
                 K[s]["coinSet"   ][coins[maxOption[2]]]+=1
            else:
                 K[s]["coinSet"   ]=K[s-1]["coinSet"   ].copy()
                 

    K[val]["coinNumber"]*=-1#-K[val]["coinNumber"]
    return K[val]

val_coins=[(15, [7, 6]),\
    (14, [7, 6]),\
    (13, [7, 6]),\
    (12, [7, 6]),\
    (11, [7, 6]),\
    (117, [7, 6,2])\
          ]
for item in val_coins:
    res=find_min_coins(item[1],item[0])
    print(f"sum: {item[0]}, gap: {item[0]-res["sum"]}, find_min_coins {res}")





