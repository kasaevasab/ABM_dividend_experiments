from AgentBasedModel import Simulator, Broker, Random, Fundamentalist, Chartist, ExchangeAgent
import numpy as np
import matplotlib.pyplot as plt

traders_num = 10
sessions_num = 100
iterations_num = 10000

xg = [ExchangeAgent()]
traders = [Random(xg, cash=1000) for i in range(1)]
traders += [Fundamentalist(xg, cash=1000, access=i) for i in range(1, traders_num)]

sim = Simulator(exchanges=xg, traders=traders)
sim.simulate(iterations_num)

plt.plot(np.array(sim.info[0].prices))
plt.legend(title="Stock price dynamics")
plt.xlabel('time period')
plt.ylabel('price')
plt.savefig(f'./tmp/stock_price_dynamics_1.png')
