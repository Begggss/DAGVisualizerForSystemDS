import parser
import plotly.express as px
import plotly.graph_objects as go


#path for log file
path = 'builtinOutlier.log'

#name of the node for operators graph
node = 'GENERIC 1'

#initialize 2 arrays for the tree
words, dashCount = parser.extract_words(path)
parser.adapt_node_label(words,dashCount)
for word in words:
    print
labels, dashCountTree = parser.extract_tree_labels(words, dashCount)
names, parents = parser.add_tree_nodes(labels, dashCountTree)

# #visualization of the tree graph for generic and logic blocks
fig = px.treemap(names = names,
                 parents = parents)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

#visualization of the sankey diagram for generic and logic blocks
label,source, target, value = parser.tree_to_sankey(names, parents)
fig = go.Figure(go.Sankey(
    arrangement= 'freeform',
    node = dict(
      pad = 100,
      thickness = 30,
      line = dict(color = "black", width = 0.5),
      label = label,

    ),
    link = dict(
      arrowlen = 15,
      source = source, # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = target,
      value = value
  )))
fig.update_layout(title_text= path, font_size=10)

fig.show()




#extract lines for operators graph and initialize two arrays for cp and spark
start, end = parser.sankey_index(words, dashCount, node)
sankeylines = parser.extract_sankey_lines(path,start,end)
cp, spark = parser.sankey_versions(sankeylines)
for i in cp:
    print(i)

#create list of operations for cp and visualize the diagram
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
for i in spark:
    print(i)
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

