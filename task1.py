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

def coin_set_parameters(coin_set):
    s=0
    for i,val in coin_set.items():
        s+=val
    return len(coin_set), s


def find_min_coins(coins,val):
    n=len(coins)
    K = [[{"sum":0,"coinSet":{},"coinNumber":0} for s in range(val + 1)] for i in range(n+1)]
    for s in range(val):   
        for i in range(n):
            if coins[i]<=s:
                val_temp=coins[i] + K[i][val - coins[i]]["sum"]
                if val_temp>K[s+1][i]["sum"]:
                    K[s+1][i+1]["sum"]= coins[i] + K[val - coins[s+1]][i]["sum"]
                    K[s+1][i+1]["coinSet"][coins[i]]+=1
                    K[s+1][i+1]["coinNumber"]+=1
                else:
                    K[s+1][i+1]= K[s+1][i]
    return K[n][val]




def knapSack(W, wt, val, n):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгоруё
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# виклик функції
print(knapSack(capacity, weight, value, n))  # 220


