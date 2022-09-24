def pre(root):
    print(root, end = "")
    if tree[root][0] != '.':
        pre(tree[root][0])
    if tree[root][1] != '.':        
        pre(tree[root][1])

def inorder(root):
    if tree[root][0] != '.':
        inorder(tree[root][0])
    print(root, end = "")
    if tree[root][1] != '.':        
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0] != '.':
        postorder(tree[root][0])
    if tree[root][1] != '.':
        postorder(tree[root][1])
    print(root, end = "")

N = int(input())
tree = dict()
for _ in range(N):
    root, sub1, sub2 = input().split()
    tree[root] = (sub1, sub2)
pre('A')
print()
inorder('A')
print()
postorder('A')