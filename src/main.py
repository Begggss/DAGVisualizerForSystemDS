import visualizer



#path for log file
path = '../log-files/AucTest.log'

#name of the node for operators graph
node = ''



#visualize the tree graph for generic and logic blocks
visualizer.visualize_tree(path)


#visualize  the sankey diagram for generic and logic blocks
visualizer.visualize_sankey(path)





#visualize the operations graph
visualizer.visualize_operations(path, node)











