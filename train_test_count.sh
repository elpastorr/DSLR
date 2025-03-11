# Description: This script is used to run logreg_train.py and logreg_predict.py, then calculate the accuracy of the prediction.
python3 logreg_train.py datasets/dataset_train.csv
python3 logreg_predict.py datasets/dataset_test.csv
i=$(diff houses.csv datasets/dataset_truth.csv | wc -l)
result=$(echo "scale=2;100-$i/16" | bc -l)
echo $result