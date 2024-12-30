from graphviz import Source

dot_file = 'music-recommender.dot'
graph = Source.from_file(dot_file)
graph.render('music-recommender', format="png", cleanup=True)
graph.view()