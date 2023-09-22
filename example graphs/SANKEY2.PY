import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 50,
      thickness = 10,
      line = dict(color = "black", width = 0.5),
      label = ["castdts", "mvvar", "seq", "cpvar", "rand", "cpvar"],
      color = "blue",
    ),
    link = dict(
      source = [0, 2, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [1, 3, 5],
      value = [0.5, 0.5, 0.5]
  ))])

fig.update_layout(title_text="GENERIC 1", font_size=10)
fig.show()
