import re
import parser
from node import Node
import plotly.express as px
from operators import Operator
import plotly.graph_objects as go

path = '/Users/begum/PycharmProjects/workspace/ldevisualizer/src/decisionTree.log'
node = 'GENERIC 1'
words, dashCount = parser.extract_words(path)
parser.adapt_node_label(words,dashCount)

labelscp=[]
dashCountTree=[]
labelscp, dashCountTree = parser.extract_tree_labels(words, dashCount)



names=[]
parents=[]

names, parents = parser.add_tree_nodes(labelscp, dashCountTree)

fig = px.treemap(names = names,
                 parents = parents)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

start, end = parser.sankey_index(words, dashCount, node)

sankeylines = parser.extract_sankey_lines(path,start,end)

cp, spark = parser.sankey_versions(sankeylines)


operatorscp = parser.create_operations(cp)
labelscp, sourcecp, targetcp, valuecp = parser.create_sankey_nodes(operatorscp)

fig = go.Figure(go.Sankey(
    arrangement= 'freeform',
    node = dict(
      pad = 100,
      thickness = 30,
      line = dict(color = "black", width = 0.5),
      label = labelscp,

    ),
    link = dict(
      arrowlen = 15,
      source = sourcecp, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = targetcp,
      value = valuecp
  )))

fig.update_layout(title_text= "CP - " + node, font_size=10)

fig.show()



operatorspark = parser.create_operations(spark)
labelspark, sourcespark,targetspark, valuespark = parser.create_sankey_nodes(operatorspark)
fig = go.Figure(go.Sankey(
    arrangement= 'freeform',
    node = dict(
      pad = 100,
      thickness = 30,
      line = dict(color = "black", width = 0.5),
      label = labelspark,

    ),
    link = dict(
      arrowlen = 15,
      source = sourcespark, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = targetspark,
      value = valuespark
  )))

fig.update_layout(title_text= "SPARK - " + node, font_size=10)

fig.show()

