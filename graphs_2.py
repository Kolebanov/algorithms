infinity = float('inf')
processed = []

graph = {}
graph['a'] = {}
graph['a']['b'] = 10
graph['b'] = {}
graph['b']['c'] = 20
graph['c'] = {}
graph['c']['d'] = 1
graph['c']['fin'] = 30
graph['d'] = {}
graph['d']['b'] = 1
graph['fin'] = {}

costs = {}
costs['b'] = 10
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['b'] = 'a'
parents['c'] = None
parents['d'] = None
parents['fin'] = None


def lowest_node_price(costs):
    lowest_price = infinity
    lowest_price_node = None
    for node in costs:
        if costs[node] < lowest_price and node not in processed:
            lowest_price = costs[node]
            lowest_price_node = node
    return lowest_price_node


node = lowest_node_price(costs)
while node is not None:
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = costs[node] + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = lowest_node_price(costs)
print(costs)

