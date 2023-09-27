# DAG Visualizer For SystemDS

## About Repository

In this repository, we implemented a visualizer to visualize the execution plans of a Apache SystemDS script. The programm takes an execution plan log created by Apache SystemDS as an input and creates various graphs as an output. 

Repository's contributers are Begum Cajias and Barkin Karadeniz.

## Motivation

Apache SystemDS compiles a high-level script into hybrid execution plans of local, distributed and GPU operations. Understanding these plans is absolutely necessary to implement features in
the compilation and runtime stacks. So this project is developed, aiming to produce visual structures for the execution plans of high-level scripts compiled by Apache SystemDS.

## How to Use

If you run an Apache SystemDS script with an additional "-explain" argument, you would see that Apache SystemDS printed an detailed execution plan to your debug console. You have to take that log and add that log to "log-files" on your clone of this repository as a file. Then go to "src/main.py" and change the "path" variable on line 4 accordingly.

If you know the "Generic Block" that you would like to inspect already, you can alter the variable "node" on line 7 accordingly. If you don't, you can leave the assigned value as "GENERIC 1" since any instance we tested already had a node named "GENERIC 1".

This would create 3 visuals. An example is shown below for "ALStest.log".

<img src="./img/3.png" width="800">

<img src="./img/1.png" width="800">

<img src="./img/2.png" width="800">

After receiving the visuals, you can change the "node" variable however you need or want.

## Limitations

### You should be aware of the following limitations:
- Your log file has to include only one execution plan. For example, if your log file has several <p style="text-align: center; margin: 0"># EXPLAIN (RUNTIME): </p> as a line that means that your log file has several execution plans bundled together. A known exception is "<a href="https://github.com/apache/systemds/blob/main/src/test/java/org/apache/sysds/test/functions/builtin/part1/BuiltinArimaTest.java">BuiltinArimaTest.java</a>" from Apache SystemDS's original<a href="https://github.com/apache/systemds"> open source repository</a>.
- We don't support special operators such as sourcing from other files by default. But you can extend the code for your own operations. See the "[Extensibility](#extensibilty)" section to for details.
- We do only support compile time plans and no runtime plans.

## Extensibilty

While we were working on the project, we tried to include as many operators as we can. In addition to this we are aware that there are more operators that is legal to use in an Apache SystemDS script. We designed the code accordingly, so that you can add a new operation on your own to the DAGVisualizerForSystemDS. 

There are two functions called "group_operators" and "get_input_output" in the file "blockParser.py". In "get_input_output", the operators are grouped according to how many inputs and outputs they have. Please have a look at the code and then add your operation to the corresponding array in the "group_operators" function.