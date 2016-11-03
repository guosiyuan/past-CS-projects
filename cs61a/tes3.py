
nil = "Troog" 
class Link:
    def __init__(self, first, rest=nil): 
        self.first = first
        self.rest = rest
class Tree:
    def __init__(self, entry, branches=nil):
        self.entry = entry 
        self.branches = branches





def wheres_groot(gtree):
    if gtree.entry=='Groot':
        return 'Groot'
    children=gtree.branches
    while children!=nil:
        if wheres_groot(children.first)=='Groot':
            return 'Groot'
        children=children.rest
    return 'Nowhere'

evil = Tree("Ronan", Link(Tree("Nebula"), Link(Tree("Korath"))))
good = Tree("Gamora", Link(Tree("Rocket", Link(Tree("Groot")))))










