class Node:
    def __init__(self, id, value=None, *args):
        self.id = id
        self.children = args
        self.value = value
        self.alpha = None
        self.beta = None
    def __str__(self):
        return f'Id: {self.id} value: {self.value} alpha: {self.alpha} beta: {self.alpha} children: {len(self.children)}'
INFINITY = 99999
def minimax(node, depth, isMax, alpha, beta, parent = 0):
    
    if len(node.children) == 0:
        print(f'nút {node.id} trả về {node.value} cho nút {parent} tại nút {node.id} alpha={alpha} beta={beta}')
        return node.value
    
    if isMax:
        bestVal = -INFINITY
        for child in node.children:
            print(f'nút {node.id } gọi đệ quy xuống nút {child.id}')
            value = minimax(child, depth+1, False, alpha, beta, node.id)
            bestVal = max(bestVal, value)
            if (bestVal > alpha):
                print(f'nút {node.id} gán alpha {bestVal}' )
            alpha = max(alpha, bestVal)

            node.alpha = alpha
            node.beta = beta
            
            if beta <= alpha:
                print(f' lúc này nút {node.id} có alpha={alpha} >= beta={beta} => nhánh lại của nút {node.id} bị cắt')
                break
        print(f'nút {node.id } trả về {bestVal} cho nút {parent}  tại nút {node.id} alpha={alpha} beta={beta}')
        return bestVal
    else:
        bestVal = INFINITY
        for child in node.children:
            print(f'node {node.id } gọi đệ quy xuống nút {child.id}')
            value = minimax(child, depth+1, True, alpha, beta, node.id)
            bestVal = min(bestVal, value)
            if (bestVal < beta):
                print(f'nút {node.id} gán beta {bestVal}' )
            beta = min(beta, bestVal)
            node.alpha = alpha
            node.beta = beta
            
            if beta <= alpha:
                print(f'lúc này tại nút ({node.id}) alpha={alpha} >= beta{beta} nên nhánh còn lại của nút {node.id} bị cắt' )
                break
        print(f'nút {node.id } trả về  {bestVal} cho nút {parent} tại nút {node.id} alpha={alpha} beta={beta}')
        return bestVal

number_values = [5,6,4,7,7, 6,1,-9, 1,0,0, -4, 4, -1, 2, -3]
values = [None for _ in range(15)] + number_values
print(len(values))
nodes = [Node(i, value)  for i, value in enumerate(values)]

for i in range(len(nodes) - 15):
    if 2*i + 2 < len(nodes):
        nodes[i].children = [nodes[2*i+1], nodes[2*i+2]]

print(minimax(nodes[0], 0, True, -INFINITY, INFINITY))

# for node in nodes:
#     print(node)



