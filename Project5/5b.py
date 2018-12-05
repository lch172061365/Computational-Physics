import random
import matplotlib.pyplot as plt
import math

m0 = 1 #initial money
N = 500
agent_moneylist = [m0]*N #500 agents intial money list

#monte carlo algorithm, random agent and radom transaction index x
def trade(agent_moneylist):
    x = random.uniform(0,1) #random trading money percent
    trade_agent = random.sample(range(0,N),2) #random two agents
    ta1 = trade_agent[0]
    ta2 = trade_agent[1]
    money_ta1 = x*(agent_moneylist[ta1] + agent_moneylist[ta2])
    money_ta2 = (1-x)*(agent_moneylist[ta1] + agent_moneylist[ta2])
    agent_moneylist[ta1] = money_ta1
    agent_moneylist[ta2] = money_ta2
    #trade finish

def financial_engineering(agent_moneylist):
    for i in range(0,1000000):
        trade(agent_moneylist)
    return agent_moneylist

def data(agent_moneylist):
    agent_moneylist.sort()
    step = 0.4
    i = 1
    k = 1
    count = []
    money = []
    judgement = math.floor(agent_moneylist[0]*100)/100
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


#wm = number/N, as known as number/500, so log(wm)=log(number)-log(N)
def recognizing_distribution():
    count,money = data(agent_moneylist)
    print(count)
    logwm_list=[0]*len(count)
    for i in range(len(count)):
        logwm_list[i] = math.log(count[i])-math.log(N)
    print(logwm_list)
    x_values = money
    y_values = logwm_list
    plt.figure('Recognizing Distribution')
    plt.title('money distribution for financial engineering')
    plt.xlabel('money')
    plt.ylabel('log(wm)')
    plt.scatter(x_values, y_values, s=20, c="#ff1212", marker='o')
    plt.show()

if __name__ == '__main__':
    financial_engineering(agent_moneylist)
    recognizing_distribution()
