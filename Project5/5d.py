import random
import matplotlib.pyplot as plt
import math

m0 = 1 #initial money
N = 1000
agent_moneylist = [m0]*N #1000 agents intial money list

dif = 0.004
a = 2
k = dif**a

def pij(mi,mj):
    pij = k/((abs(mi-mj)**a)+0.000001)
    #in case mi-mj=0, and 0.000001 is small enough to ignore the effect
    p = random.uniform(0,1)
    if p <= pij:
        return True  #Trasaction success
    else:
        return False #Transaction fail

#monte carlo algorithm, random agent and radom transaction index x
def trade(agent_moneylist):
    x = random.uniform(0,1) #random trading money percent
    trade_agent = random.sample(range(0,N),2) #random two agents
    ta1 = trade_agent[0]
    ta2 = trade_agent[1]
    mi = agent_moneylist[ta1]
    mj = agent_moneylist[ta2]
    if pij(mi,mj) == True:
        money_ta1 =x*(agent_moneylist[ta1] + agent_moneylist[ta2])
        money_ta2 =(1-x)*(agent_moneylist[ta1] + agent_moneylist[ta2])
        agent_moneylist[ta1] = money_ta1
        agent_moneylist[ta2] = money_ta2
    else:
        pass
    #trade finish

def financial_engineering(agent_moneylist):
    for i in range(0,1000000):
        trade(agent_moneylist)
    return agent_moneylist

def data(agent_moneylist):
    agent_moneylist.sort()
    step = 0.05
    i = 1
    k = 1
    count = []
    money = []
    judgement = round(agent_moneylist[0],2)
    while i < N :
        if agent_moneylist[i] < judgement + step:
            k += 1
            i += 1
        else:
            if k != 0:#ignore those k=0 to make the figure looks better
                count.append(k)
                money.append(judgement)
                judgement += step
                k = 0
            else:
                judgement += step
                k = 0
    return count,money

def plot_making():
    count,money = data(agent_moneylist)
    x_values = money
    y_values = count
    plt.figure('Results for money trade')
    plt.title('money distribution for financial engineering')
    plt.xlabel('money')
    plt.ylabel('number')
    plt.scatter(x_values, y_values, s=20, c="#ff1212", marker='o')
    plt.show()
    

if __name__ == '__main__':
    financial_engineering(agent_moneylist)
    plot_making()
