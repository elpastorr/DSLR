SRCS =	srcs/describe.py		\
		srcs/histogram.py		\
		srcs/logreg_predict.py	\
		srcs/logreg_train.py	\
		srcs/pair_plot.py		\
		srcs/scatter_plot.py

SRC_MAIN = srcs/main.py
SRC_TRAIN = srcs/logreg_train.py
SRC_PREDICT = srcs/logreg_predict.py
DATASET_GUESS = houses.csv
DATASET_TRUTH = datasets/dataset_truth.csv
DATASET_TRAIN = datasets/dataset_train.csv

all: train predict main

train : $(SRCS)
	python3 $(SRC_TRAIN)

predict : $(SRCS)
	python3 $(SRC_PREDICT)

main: $(SRCS)
	python3 $(SRC_MAIN) $(DATASET_GUESS) $(DATASET_TRUTH)

describe: $(SRCS)
	python3 srcs/describe.py $(DATASET_TRAIN)

histogram: $(SRCS)
	python3 srcs/histogram.py $(DATASET_TRAIN)

pair_plot: $(SRCS)
	python3 srcs/pair_plot.py $(DATASET_TRAIN)

scatter_plot: $(SRCS)
	python3 srcs/scatter_plot.py $(DATASET_TRAIN)

install:
	sh install/install.sh

clean:
	dune clean

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all install clean fclean re