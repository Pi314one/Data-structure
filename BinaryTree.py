#树
class TreeNode:
    def __init__(self, val:int|None=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, lst: list[int|None]):
        root = lst[0] if len(lst) > 0 else None
        self.root=TreeNode(root)
        self.load(lst,self.root,0)

    def load(self,vals,node:TreeNode,cur:int):
        if 2*cur+1<len(vals):
            if vals[2*cur+1]:
                node.left=TreeNode(vals[2*cur+1])
                self.load(vals,node.left,2*cur+1)
        if 2*cur+2<len(vals):
            if vals[2*cur+2] is not None:
                node.right=TreeNode(vals[2*cur+2])
                self.load(vals,node.right,2*cur+2)

    def __str__(self):
        queue=[self.root]
        string=''
        while queue:
            level_len=len(queue)
            for i in range(level_len):
                cur=queue.pop(0)
                string+=str(cur.val)+' '
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            string+='\n'
        return string

bt=BinaryTree([10, 5, 15, 3, 7, None, 20])
print(bt)




    