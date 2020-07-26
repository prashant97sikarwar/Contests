class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def Serialize(root,arr):
    if root is None:
        arr.append(-1)
        return
    else:
        arr.append(root.data)
        Serialize(root.left,arr)
        Serialize(root.right,arr)
        
def Deserialize(arr):
    index = 0
    if index == len(arr):
        return None
    val = arr[index]
    index += 1
    if arr[index] == -1:
        return None
    node = Node(val)
    node.left = Deserialize(arr)
    node.right = Deserialize(arr)
    return node
    
    