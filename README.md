# generate-model-graph
This program is used to generate graphs based on our output files from the model.

### Input Files
Currently our model output files have train and test output for each epoch. For example:
```
Epoch: 151
----------TRAIN STATS----------

TRAIN CROSS ENTROPY: 3.1798332813051013
TRAIN ACCURACY: 0.42
TRAIN CONFUSION MATRIX:
[[199   8   1 ...   2   5   1]
 [  1 166   1 ...   5   4   1]
 [  0   3  79 ...  11   5   5]
 ...
 [  0   3   5 ...  91   2   3]
 [  1   4   7 ...   9 104   4]
 [  1   1   1 ...   6   2 129]]
TRAIN CONFIDENCE INTERVAL: [0.48326257 0.48326257],[0.67673755 0.67673755]

----------TEST STATS----------

TEST CROSS ENTROPY: 5.363289957046509
TEST ACCURACY: 0.12
TEST CONFUSION MATRIX:
[[12  1  0 ...  0  1  0]
 [ 1  8  1 ...  0  2  0]
 [ 0  0  1 ...  0  2  0]
 ...
 [ 0  1  3 ...  2  0  0]
 [ 2  3  1 ...  1  4  0]
 [ 0  0  0 ...  0  2  1]]
TEST CONFIDENCE INTERVAL: [0.81630754 0.81630754],[0.94369245 0.94369245]**
```

### Running
Clone the directory and locate to the directory.
**Run the program using**
```python
python ./main.py --file="file name" <flags>
```
**Get more information about the flags using**
```pytohn
python ./main.py -h
```

##### Flags Table
| Flag          | Type          | Description                                     | Default |
| ------------- |:-------------:| :----------------------------------------------:| -------:|
| --file_dir    | String        | Path to the directory where the file is located |     ./  |
| --skip        | centered      | Skip number of lines while reading the file     |     0   |
| --file        | String        | Name of the file that you want to read          |         |    
| --out_dir     | String        | Ouput directory where the graphs will be moved  |     ./  |

### Output
The program will output the graph as a **PNG** file to the out_dir specified. Example graph looks like below.

![alt text](https://github.com/aagrawal20/generate-model-graph/blob/master/graphs/train-test.png "Train Test Graph")
