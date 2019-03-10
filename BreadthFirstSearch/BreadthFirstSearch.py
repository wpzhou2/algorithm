#这个算法是使用广度优先算法来
#判断A能不能到达B，而且若找到路径，该路径同时也是最短路径（无权）

from collections import deque

graph={} #字典，底层实现为哈希表，在这里代表图
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

def search(name):
    #广度优先算法，是一层一层向外查询，
    #第一层的人先放入一个队列中，然后弹出队列第一个人出来检查是否要找的人
    #若不是，则将其人的邻居都后插到队列中，并将其记录为检查过的人
    #继续弹出队列的人继续检查...

    #广度优先算法第一要将每个人的邻居都要检查一遍，而人与人之间的邻居关系靠“边”来判断，故有O(E)
    #其次，BFS还要检查每个人是否已经检查过了的，这个最多消耗O（V）
    #故其运行时间为O(E+V)

    search_queue = deque()
    search_queue += graph[name]
    searched=[] #记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_want(person):
                print("要找的人找到了")
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False

#判断是否为要找的人的算法
def person_is_want(name):
    return name[-1]=='m'


search("you")