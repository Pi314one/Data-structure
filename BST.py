"""在树很大的情况下画图可能是不现实的，作图只是为了演示，如果树非常大，最好不要随意调用BST的graph方法"""
from pyecharts.charts import Tree
class TreeNode:
    def __init__(self, val:int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __contains__(self, item):
        if item=='children':
            if self.left or self.right:
                return True
            return False
        else:
            return True

    def __getitem__(self, item):
        if item=='name':
            return str(self.val)
        else:
            left=self.left if self.left else {'name':'None'}
            right=self.right if self.right else {'name':'None'}
            return [left,right]

class BST:
    def __init__(self,iterable):
        self.root=None
        self.d=0
        if iterable:
            self.root=TreeNode(iterable[0])
        for i in range(1,len(iterable)):
            self.insert(iterable[i])

    def search(self, val:int):
        cur=self.root
        while cur:
            if val==cur.val:
                return cur
            elif val<cur.val:
                cur=cur.left
            else:
                cur=cur.right
        return None

    def insert(self, val:int):
        if self.search(val):
            print("value already exists")
        cur=self.root
        while True:
            if not cur:
                cur=TreeNode(val)
                break
            elif val<cur.val:
                if not cur.left:
                    cur.left=TreeNode(val)
                    break
                else:
                    cur=cur.left
            else:
                if not cur.right:
                    cur.right=TreeNode(val)
                    break
                else:
                    cur=cur.right

    def delete(self,val):
        node= self.search(val)
        if not node:
            print("value not found")
        else:
            if self.d==0:
                cur= node.left
                if not cur:
                    node.val=node.right.val
                    node.left=node.right.left
                    node.right=node.right.right
                elif not cur.right:
                    node.val=cur.val
                    node.left=cur.left
                else:
                    while cur.right.right:
                        cur=cur.right
                    node.val=cur.right.val
                    cur.right=None
                self.d=1
            else:
                cur=node.right
                if not cur:
                    node.val= node.left.val
                    node.left=cur.left
                    node.right=cur.right
                elif not cur.left:
                    node.val=cur.val
                    cur.right=cur.right
                else:
                    while cur.left.left:
                        cur=cur.left
                    node.val=cur.left.val
                    cur.left=None
                self.d=0

    def graph(self):
        if not self.root:
            return {'name':'None'}
        else:
            return self.cast(self.root)

    def cast(self, node):
        if node['name']=='None':
            return {'name':'None'}
        else:
            dic={'name':node['name']}
            if 'children' in node:
                dic['children']=[self.cast(node['children'][0]),self.cast(node['children'][1])]
            return dic

def draw(tree:BST):
    graph=Tree()
    graph.add('Binary Search Tree',[tree.graph()])
    graph.render("Binary Search Tree.html")

t=BST([50, 30, 70, 20, 40, 60, 80])
draw(t)