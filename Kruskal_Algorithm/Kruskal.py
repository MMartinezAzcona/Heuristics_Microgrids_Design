#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:57:47 2019

@author: mariomartinez
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:14:26 2019

@author: mariomartinez
"""

#DEFINICION ARCOS
class Edge():
    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex
    
    def __lt__(self, other):
        """
        Ordenar arcos en funcion del peso (de menor a mayor)
        :param other:
        :return:
        """
        selfpriority = self.weight
        otherpriority = other.weight
        return selfpriority < otherpriority

    
#DEFINICION VERTICES
class Vertex():
    def __init__(self, name):
        self.name=name

    def __str__(self):
        return '{name}'.format(self=self)

    def __rpr__(self):
        return '{name}'.format(self=self)
        
#DEFINICIÓN NODOS
class Node():
    def __init__(self, height, nodeid, parentnode):
        self.height = height
        self.nodeid = nodeid
        self.parentnode = parentnode

 
#DISJOINT SET: Determina nodos separados, conectados y controla que no haya ciclos
class DisjointSet():
    def __init__(self, vertexlist):
        self.vertexlist = vertexlist
        self.rootnodes = []
        self.setcount = 0
        self.makesets(vertexlist)
        
    def makesets(self, vertexlist):
        """
        Conjunto de vertices pedientes de conexion
        :param vertexlist:
        """
        for v in vertexlist:
            self.makeset(v)
        
    def makeset(self, vertex):
        """
        Establece conexion entre
        :param vertex:
        :return:
        """
        node=Node(0, len(self.rootnodes), None)
        vertex.parentnode=node
        self.rootnodes.append(node)
        self.setcount +=1
        
    def find(self, node):
        """
        Busca el nodo padre del nodo dado de entrada.
        Si el propio nodo es un nodo raíz, se devuelve el propio nodo de entrada
        :param node
        :return: root.nodeid
        """
        currentnode = node
        while currentnode.parentnode is not None:
            currentnode = currentnode.parentnode
            
        root = currentnode
        
        while currentnode is not root:
            temp = currentnode.parentnode
            currentnode.parentnode = root
            currentnode = temp
        
        return root.nodeid
    
    
    def union(self, node1, node2):
        """
        Establece como nodo padre del otro nodo al cual cuya altura sea mayor
        :param node1
        :param node2
        """

        root1 = self.rootnodes[self.find(node1)]
        root2 = self.rootnodes[self.find(node2)]
        
        if root1.height < root2.height:
            root1.parentnode=root2
        elif root1.height > root2.height:
            root2.parentnode=root1
        else:
            root2.parentnode=root1
            root1.height +=1
        self.setcount -=1

#----------------------------------------------------------------------------

#ALGORITHM     
class algorithm():
    
    def constructSpanningTree(self, vertexlist, edgelist):
        """
        Construccion de un arbol parcial mínimo mediante el algoritmo de Kruskal
        :param vertexlist (Conjunto de vertices)
        :param edgelist (Conjunto de arcos)
        """
        
        disjointset=DisjointSet(vertexlist)
        spanningtree=[]
        
        edgelist.sort()
        
        for edge in edgelist:
            u=edge.startvertex
            v=edge.targetvertex
            if disjointset.find(u.parentnode) is not disjointset.find(v.parentnode):
                spanningtree.append(edge)
                disjointset.union(u.parentnode, v.parentnode)
        
        for edge in spanningtree:
            print(edge.startvertex.name,"-",edge.targetvertex.name)
