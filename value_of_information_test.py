from AgentBasedModel import Simulator, Broker, Random, Fundamentalist, Chartist, ExchangeAgent
import numpy as np
import matplotlib.pyplot as plt

traders_num = 3
sessions_num = 100
iterations_num = 100

mean_overall_return = [0 for i in range(traders_num)]
for session in range(sessions_num):
    xg = [ExchangeAgent()]
    traders = [Random(xg, cash=1000) for i in range(1)]
    traders += [Fundamentalist(xg, cash=1000, access=5) for i in range(1)]
    traders += [Fundamentalist(xg, cash=1000, access=10) for i in range(1)]
    # traders += [Fundamentalist(xg, cash=1000, access=i) for i in range(1, traders_num)]

    sim = Simulator(exchanges=xg, traders=traders)
    sim.simulate(iterations_num)
    for tr_id in range(traders_num):
        start_equity = sim.info[0].equities[0][tr_id + session * traders_num]
        finish_equity = sim.info[0].equities[-1][tr_id + session * traders_num]
        mean_overall_return[tr_id] = (finish_equity - start_equity) / start_equity
        # for iter_dict in sim.info[0].returns:
        #     mean_overall_return[tr_id] += iter_dict[tr_id + session * traders_num]

    print(sim.info[0].equities)
    # print(sim.info[0].cash)
    # print(sim.info[0].assets)


mean_overall_return = [mean_overall_return[i] / sessions_num for i in range(traders_num)]

#np.std(np.array(sim.info[0].returns))

# sum_returns = [0 for i in range(len(traders))]
# for tr_id in range(len(traders)):
#     for iter_dict in sim.info[0].returns:
#         sum_returns[tr_id] += iter_dict[tr_id]

plt.plot(np.array(mean_overall_return))
plt.legend(title="Mean overall returns for 100 simulations")
plt.xlabel('trader_id')
plt.ylabel('return in percentage')
plt.savefig(f'./tmp/{sessions_num}_sessions_{traders_num}_info_levels_6.png')

