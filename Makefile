run: collect sort

collect:
	python -m pytest -s

sort:
	python sort_best_keywords.py
