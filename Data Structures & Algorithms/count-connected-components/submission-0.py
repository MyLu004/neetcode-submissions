class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))


        def find(x): 
            if parent[x] == x:
                return x
            return find(parent[x])
        
        def union(x,y):
            x_rep = find(x)
            y_rep = find(y)

            if(x_rep == y_rep):
                return False
            parent[y_rep] = x_rep
            return True
        
        components = n
        for u,v in edges:
            if union(u,v):
                components -= 1
        
        return components
    