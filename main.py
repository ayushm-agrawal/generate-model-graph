# Import the required libraries
import matplotlib.pyplot as plt
import numpy as np

import argparse
import os
import sys
import shutil
import time

# the main function
def main(file, skip_lines, file_dir, out_dir):

    # store some variables
    epochs = 0
    train_accuracy = []
    test_accuracy = []

    start = time.time()
    # open the file in read only mode
    try:
        print("Reading the file...")
        f = open(file_dir + file, "r")

    except FileNotFoundError as error:

        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('{} in {} at line {}\n'.format(error, fname, exc_tb.tb_lineno))
        print('Use flags to specify the file and directory. HELP -> python ./main.py -h')
        sys.exit()


    # skip unnecessary lines
    print("Skipping lines...")
    for _ in range(skip_lines):
        next(f)

    # loop through line by line
    
    print("Fetching train and test accuracies from the file...\n")
    while True:
        line = f.readline()
        if 'Epochs' == line[:6]:
            num = line[8:]
            epochs = parse(num)
        elif 'TRAIN ACCURACY' == line[:14]:
            num = line[16:]
            train_accuracy.append(parse(num))
        elif 'TEST ACCURACY' == line[:13]:
            num = line[15:]
            test_accuracy.append(parse(num))
        if not line:
            break

        print('Number of train accuracies {} and test accuracies {}'.format(len(train_accuracy), len(test_accuracy)), end='\r')
    
    # close the file: IMPORTANT
    f.close()

    end = time.time()
    print('\n')
    print("Total time taken: {} seconds.".format(round((end - start),2)))

    train_np = np.asarray(train_accuracy)
    test_np = np.asarray(test_accuracy)

    # plot graph
    both_img = 'train-test.png'
    plt.plot(np.arange(1, epochs+1), train_np, 'r')
    plt.plot(np.arange(1, epochs+1), test_np, 'g')
    plt.xlabel('Epochs')
    plt.ylabel('Train Accuracy')
    plt.savefig(both_img)

    # move the graph to the output directory mentioned in the flags
    try:
        shutil.move("./"+both_img, out_dir+both_img)
    except Exception as error:
        print(error)
        exit()

    print("Output graphs are stored at {} in the {} directory.".format(both_img, out_dir))

# convert the num to integer or float
def parse(num):
    try:
        return int(num)
    except ValueError:
        return float(num)

if __name__ == "__main__":

    # Setup parser
    parser = argparse.ArgumentParser(description='Generate Graphs for the model')
    parser.add_argument(
        '--file_dir',
        type=str,
        default='./',
        help='Directory where the file is located')
    parser.add_argument('--skip', type=int, default=25, help='Skip the number of lines when reading the file')
    parser.add_argument('--file', type=str, help='path to the file')
    parser.add_argument('--out_dir', type=str, default='./',help='path to the output directory. It should already exist')

    # Setup parser arguments
    args = parser.parse_args()
    #args = vars(args_namespace)['file']
    main(args.file, args.skip, args.file_dir, args.out_dir)