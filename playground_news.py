from AgentBasedModel import Simulator, Broker, Random, Fundamentalist, Chartist, ExchangeAgent
import numpy as np
import matplotlib.pyplot as plt

xg = [ExchangeAgent()]
traders = []
traders += [Fundamentalist(xg, cash=1000) for i in range(100)]
traders += [Fundamentalist(xg, cash=1000, access=5) for i in range(100)]
traders += [Fundamentalist(xg, cash=1000, access=10) for i in range(100)]

sim = Simulator(exchanges=xg, traders=traders)

sim.simulate(1000)

#np.std(np.array(sim.info[0].returns))

sum_returns = [0 for i in range(len(traders))]
for tr_id in range(len(traders)):
    for iter_dict in sim.info[0].returns:
        sum_returns[tr_id] += iter_dict[tr_id]

plt.plot(np.array(sum_returns))
plt.savefig('./tmp/out.png')