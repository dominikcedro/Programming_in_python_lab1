'''
@author Dominik Cedro

disclaimer! For find_genes function I used stackoverflow site and answer of ddzialak
on topic of iterating by threes. I implemented his answer in my code and changed it
to suit my needs for this task. Link below:
https://stackoverflow.com/questions/10988036/iterating-through-list-by-3s
'''

from list1 import dna_complement

def find_genes(strand):
    '''Finds potential genes in a strand.

    This function takes a strand of DNA as a argument. Then it will find genes
    in this strand and put them in a list. It's not a solution to the whole task.

    Parameters:
    strand: string, a strand of DNA depicted by series of letters

    Returns:
    list_genes: list , that shows which genes were found in the strand
    '''
    if not isinstance(strand, str):
        raise TypeError('Aargument must be a string type.')
    list_genes = []
    fresh_strand = ""

    for i in range(len(strand)):
       if (i+2) == len(strand):
           break
       if (strand[i]=="A" and strand[i+1]=="T" and strand[i+2]=="G"):
           for k in range(i+3,len(strand)+1,3):
                fresh_strand = fresh_strand + strand[k - 3:k]
                if strand[k - 3:k] == "TAA" or strand[k - 3:k] == "TGA" or strand[k - 3:k] == "TAG" :
                    list_genes.append(fresh_strand)
                    fresh_strand = ""
                    break
    return list_genes

print(find_genes('CCATGCGCGCGTAACGCGATGGGGTGAAATGCGCGCGTAGA'))

def test_find_genes():
    '''Testing function for find_genes

    Raises: Assertion error when test fails.
    '''
    # test for normal instance
    assert find_genes("AATGGGATAG") == ['ATGGGATAG']
    #how to test type errors?
    assert not isinstance(1, str), "Test failed: Argument is a string."




def fin(strand):
    ''' Final function, provides answer.

    This is final function for this task. It will use find_genes function to
    find genes in given strand. Then it will use dna_complement function from
    list1 (it's important to have it at hand) to translate those found genes.

    Parameters:
    strand: string, a strand of dna that will be put into function find_genes

    Returns:
    printed feedback of found dna strands and their complements
    '''
    for j in find_genes(strand):
        print(f"{j} is the first gene in strand, and {dna_complement(j)} is it's complement")


