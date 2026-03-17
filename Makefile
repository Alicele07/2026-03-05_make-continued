all : reports/reports.html

data/data.csv : scripts/01_generate_data.py
	python scripts/01_generate_data.py

results/plot.png : data/data.csv scripts/02_plot_data.py
	python scripts/02_plot_data.py

reports/reports.html : data/data.csv reports/reports.qmd results/plot.png
	quarto render reports/reports.qmd