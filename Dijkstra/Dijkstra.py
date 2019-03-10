#先把图画出来
graph={}

graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2

graph["a"]={}
graph["a"]["fin"]=1

graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5

graph["fin"]={}

#记录每个节点的开销。
#每个节点都有开销。开销指的是从起点前往该节点需要多长时间
#创建开销表
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity


#存储父节点的散列表
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None

#记录处理过的节点，对于同一条节点，不用处理多次
processed=[]


#找出开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node


#具体算法
node=find_lowest_cost_node(costs) #先找出开销最低的节点
while node is not None: #所有节点都遍历完退出while
    cost = costs[node] #查出目前从起点到该节点的开销
    neighbors=graph[node] #查出该节点的邻居
    # 遍历该节点的邻居，计算这些邻居的开销，如果新计算的开销小于开销表的值，则修改之
    # 计算最低节点的邻居的开销公式：起点到开销最低节点的开销+最低节点到邻居的开销
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    processed.append(node)  #处理该节点就标记一下
    node=find_lowest_cost_node(costs) #继续查找下一个最低开销的节点

print(costs["fin"])