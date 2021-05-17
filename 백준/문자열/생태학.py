'''
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
'''
import sys
tree = dict()
n=0
while True:
    key = sys.stdin.readline().rstrip()
    if not key:
        break
    if key in tree:
        tree[key]+=1
    else:
        tree[key]=1
    n+=1

treeType = list(tree.keys())
treeType.sort()
for t in treeType:
    print("%s %.4f" % (t,tree[t]/n*100))
