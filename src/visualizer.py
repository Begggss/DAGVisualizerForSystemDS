import plotly.express as px
import plotly.graph_objects as go
import parser

def visualize_tree(path):
    names, parents = parser.add_tree_nodes(path)

    fig = px.treemap(names=names,
                     parents=parents)
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def visualize_sankey(path):
    labels, source, target, value = parser.tree_to_sankey(path)
    title =  path.split('/').pop()
    fig = go.Figure(go.Sankey(
        arrangement='freeform',
        node=dict(
            pad=100,
            thickness=30,
            line=dict(color="black", width=0.5),
            label= labels,
        ),
        link=dict(
            arrowlen=15,
            source=source,  # indices correspond to labels, eg A1, A2, A1, B1, ...
            target=target,
            value=value
        )))

    fig.update_layout(title_text= title, font_size=15)
    fig.show()


def visualize_operations(path, node):
    label, source, target, value = parser.create_sankey_nodes(path, node)
    fig = go.Figure(go.Sankey(
        arrangement='freeform',
        node=dict(
            pad=100,
            thickness=30,
            line=dict(color="black", width=0.5),
            label=label,

        ),
        link=dict(
            arrowlen=1000,
            source=source,
            target=target,
            value=value
        )))

    fig.update_layout(title_text= node, font_size=15)

    fig.show()
