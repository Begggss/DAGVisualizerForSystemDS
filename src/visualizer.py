import plotly.express as px
import plotly.graph_objects as go
import blockParser

def visualize_tree(path):
    names, parents, numbers = blockParser.add_tree_nodes(path)


    fig = go.Figure(go.Treemap(
        labels= names,
        parents=parents,
        text = numbers,
        textinfo= "label+text",
        root_color="lightgrey"
    ))
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def visualize_sankey(path):
    labels, source, target, value, linenumbers = blockParser.tree_to_sankey(path)
    title =  path.split('/').pop()
    fig = go.Figure(go.Sankey(
        arrangement='freeform',
        node=dict(
            pad=100,
            thickness=30,
            line=dict(color="black", width=0.5),
            label= labels,
            customdata=linenumbers,
            hovertemplate='%{customdata}<extra></extra>'
        ),
        link=dict(
            arrowlen=15,
            source=source,
            target=target,
            value=value,
            hovertemplate='Link to %{target.customdata}<extra></extra>'
        )))

    fig.update_layout(title_text= title, font_size=15)                       #Comment out this line and uncomment line 41 to turn off hoverlabel
    #fig.update_layout(title_text=title, font_size=15, hovermode = False)
    fig.show()


# def visualize_operations(path, node):
#     labels, source, target, value, hover_label = blockParser.create_sankey_nodes(path, node)
#     fig = go.Figure(go.Sankey(
#         arrangement='freeform',
#         node=dict(
#             pad=100,
#             thickness=30,
#             line=dict(color="black", width=0.5),
#             label=labels,
#             customdata = hover_label,
#             hovertemplate='%{customdata}<extra></extra>',
#
#         ),
#         link=dict(
#             arrowlen=50,
#             source=source,
#             target=target,
#             value=value,
#             hovertemplate = 'Link from  %{source.customdata}<br />' +
#                     'to %{target.customdata}<br />' +
#                     '<br /><extra></extra>',
#         )))
#
#     fig.update_layout(title_text= node, font_size=15)
#     fig.show()



def visualize_operations(path, node):
    if node == None or node == " ":
        print("Please give the name of the node you would like to visualize")
    else:
        labels, source, target, value, hover_label = blockParser.create_sankey_nodes(path, node)
        fig = go.Figure(go.Sankey(
            arrangement='freeform',
            node=dict(
                pad=100,
                thickness=30,
                line=dict(color="black", width=0.5),
                label=labels,
                customdata=hover_label,
                hovertemplate='%{customdata}<extra></extra>',

            ),
            link=dict(
                arrowlen=50,
                source=source,
                target=target,
                value=value,
                hovertemplate='Link from  %{source.customdata}<br />' +
                              'to %{target.customdata}<br />' +
                              '<br /><extra></extra>',
            )))

        fig.update_layout(title_text=node, font_size=15)
        fig.show()

