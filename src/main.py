import visualizer
import blockParser



#path for log file
path = '../log-files/AucTest.log'

#name of the node for operators graph
node = 'GENERIC 2'



#visualize the tree graph for generic and logic blocks
visualizer.visualize_tree(path)


#visualize  the sankey diagram for generic and logic blocks
visualizer.visualize_sankey(path)





#visualize the operations graph
visualizer.visualize_operations(path, node)


#add variable type
#if your execution plan contains a variable type that is not given in list 'types' in the beginnig of blockParser.py,
#you can use function below

#blockParser.add_type(' ')










