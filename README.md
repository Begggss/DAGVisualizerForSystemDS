# DAG Visualizer For SystemDS

## About The Projects

DAG Visualizer for SystemDS  is a visualization tool designed to enhance understanding of execution plans  in SystemDS. This tool implements clear  representation of how machine learning algorithms are executed  making it easier  to optimize implementation.

Data scientist often use high-level programming languages to develop machine learning algorithms, which work for small sets of data. SystemDS optimizes and scales these algorithms to large sets set of data, that requires a low-level, complex implementation, making it easier to deal with large sets of data.

As a result of this process, SystemDS detailed execution plains in plain text form.Understanding these execution plans is crucial to identify performance issues. However, comprehending these plans can be challenging and time consuming in plain text form.

This issue led to creation of DAG Visualizer for SystemDS.

## Getting Started
<ul>
  <li>Begin by cloning this repository to your local machine.</li>
  <li>Install plotly </li>
  <li>Configure the log path in "main.py" to ensure that the Parse Module can retrieve execution plans correctly.</li>
</ul>

<img src="img/path.png" width="300"/>
<ul>
  <li>Specify the name of the node in "main.py" for operations graph
</ul>

<img src="img/node.png" width="300"/>

## Example Visualization
As a demonstration, we will use the  BuiltinAucTest. After passing the path of the log file containing the execution plan, the program will generate 3 graphs 

The first graph is Treemap, an interactive blocks graph. This graph contains line numbers in the blocks and allows user to trace graph with clickevents, making specially easier to trace big graphs.
<img src="./img/tree.png" width="500">

Here is the example of a bigger graph. Clicking allows user to go deeper into desired node, at the same time provide the path to the current node from 'MAIN' on top of the graph 
<img src="./img/tree3.png" width="500"> 

The second graph is a sankey diagram, allowing user to interact with the graph by moving the nodes around. This function is especially useful for dealing with large execution plans
<img src="./img/sankey.png" width="500"> 
   
The last graph is another sankey diagram, that contains the operations executing in the specified node.
<img src="./img/operations.png" width="500"> 

Hover label function in the operations graph gives the location of where each operation is executing. 

<img src="./img/hower.png" width="200"> 



### Future Improvements:

- At the moment we don't support sourcing from other files function.
- Please make sure to pass one execution plan at a time 
