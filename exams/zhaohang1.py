import sys
class Graph(object):

    def __init__(self, *args, **kwargs):
        self.node_neh = {}
        self.visited = {}
    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)
    
    def add_node(self, node):
        if not node in self.node_neh:
            self.node_neh[node] = []
    
    def add_edge(self, edge):
        u, v = edge
        if (v not in self.node_neh[u]) and (u not in self.node_neh[v]):
            self.node_neh[u].append(v)
        if u!=v:
            self.node_neh[v].append(u)
    
    def nodes(self):
        return self.node_neh.keys()

    def findDangerousUser(self,root=None):
        od = []
        self.visited = {}
        def dfs(node):
            self.visited[node] = True
            od.append(node)
            for n in self.node_neh[node]:
                if not n in self.visited:
                    dfs(n)
        if root:
            dfs(root)
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        # print(od)
        return od

g = Graph()
fst_line = sys.stdin.readline()
n = int(fst_line.split()[0])
m = int(fst_line.split()[1])
g.add_nodes([i for i in range(1,n+1)])
for i in range(m):
    line = sys.stdin.readline()
    s = int(line.split(',')[0])
    e = int(line.split(',')[1])
    g.add_edge((s, e))
safe_users = []
for n in g.nodes():
    if not g.node_neh[n]:
        safe_users.append(n)
if n <=0:
    print(None)
# else:
#     print(g.findDangerousUser(1))