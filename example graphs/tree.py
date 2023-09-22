import plotly.express as px
fig = px.treemap(
    names = ["MAIN","func:m_decisionTree 1",'GENERIC 2','GENERIC 3', "func:findBestSplit 1.1",
             "func:computeLeafLabel 1.2", "IF 1.3",'IF 1.4','IF 1.5','GENERIC 1.6','GENERIC 1.7', 'GENERIC 1.8',
             'GENERIC 1.9','WHILE 1.10', 'GENERIC 1.11','GENERIC 1.1.1','GENERIC 1.1.2','PARFOR 1.1.3', 'GENERIC 1.1.4',
             'IF 1.1.5','ELSE 1.1.6','GENERIC 1.2.1','GENERIC 1.3.1','GENERIC 1.4.1','GENERIC 1.5.1','GENERIC 1.10.1',
             'GENERIC 1.10.2','IF 1.10.3','GENERIC 1.10.4','GENERIC 1.10.5','IF 1.10.6','ELSE 1.10.7','GENERIC 1.10.8',
             'GENERIC 1.10.9'],
    parents = ["", "MAIN",'MAIN','MAIN', "func:m_decisionTree 1","func:m_decisionTree 1","func:m_decisionTree 1",
               'func:m_decisionTree 1','func:m_decisionTree 1','func:m_decisionTree 1','func:m_decisionTree 1',
               'func:m_decisionTree 1','func:m_decisionTree 1','func:m_decisionTree 1','func:m_decisionTree 1',
               "func:findBestSplit 1.1","func:findBestSplit 1.1" ,"func:findBestSplit 1.1","func:findBestSplit 1.1",
               "func:findBestSplit 1.1","func:findBestSplit 1.1","func:computeLeafLabel 1.2",'IF 1.3','IF 1.4','IF 1.5',
               'WHILE 1.10','WHILE 1.10','WHILE 1.10','WHILE 1.10','WHILE 1.10','WHILE 1.10','WHILE 1.10','WHILE 1.10',
               'WHILE 1.10']
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
