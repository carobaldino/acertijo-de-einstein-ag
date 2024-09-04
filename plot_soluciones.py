import plotly.express as px
from main import generations, log_book


figure = px.line(x = range(0,generations+1), y = log_book.select("max"), title = "Genetic algorithm results")
figure.show()