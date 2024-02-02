import argparse
from shingles_retake import shingles

def argparser():

    parser1 = argparse.ArgumentParser(description='Generate and print shingles')
    parser1.add_argument('-n', type=int,required=True,default=1,help='Number of most common k-shingles')
    parser1.add_argument('-k',type=int,required=True,default=1,help='Length of k-shingles')
    args1 = parser1.parse_args()
    n,k = args1.n, args1.k
    return n,k

def input_data():
