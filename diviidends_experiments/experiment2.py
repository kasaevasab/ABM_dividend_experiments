from AgentBasedModel import Simulator, Random, Fundamentalist, Universalist, ExchangeAgent, FundamentalPriceShock, \
    MarketMaker
from AgentBasedModel import plot_price, plot_price_fundamental, plot_dividend
from AgentBasedModel import dunn_test, general_states


def simulate(mode, args, iterations_num=300):
    xg = [ExchangeAgent(dividend_generation_mode=mode, dividend_generation_args=args)]
    traders = []
    traders += [Random(xg, cash=1000) for _ in range(7)]
    traders += [Fundamentalist(xg, cash=1000, access=10) for _ in range(5)]
    traders += [Universalist(xg, cash=1000, access=3) for _ in range(3)]
    traders += [MarketMaker(xg, cash=1000) for _ in range(3)]

    events = [FundamentalPriceShock(it=50, price_change=-20)]

    sim = Simulator(exchanges=xg, traders=traders, events=events)
    sim.simulate(iterations_num)
    return sim


labels = ['lognormal', 'uniform']
args = [[5e-3], [0.97, 1.03]]
groups_num = len(labels)

simulations_num = 30
shock_it = 50

metrics = ['dropdown', 'time_to_recover']
data = {key: [[0 for _ in range(simulations_num)] for _ in range(len(labels))] for key in metrics}

for group in range(groups_num):
    for sim_num in range(simulations_num):
        sim = simulate(labels[group], args[group])
        states = general_states(sim.info[0], size=20)[:3]
        try:
            i = min(states.index('trend'), states.index('stable'))
            stabilization = (i + 1) * 20
        except:
            stabilization = 299
        data[metrics[0]][group][sim_num] = sim.info[0].prices[stabilization] - sim.info[0].prices[shock_it]
        data[metrics[1]][group][sim_num] = stabilization

        if sim_num == simulations_num - 1:
            plot_price_fundamental(sim.info[0])
            plot_price(sim.info[0])
            plot_dividend(sim.info[0])

for it in data:
    print(dunn_test(data[it], labels))
