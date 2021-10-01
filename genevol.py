#let's create a genetic engine

import random

#genesis, let there be a parent
def _parent_generator(parent_length, geneset):
    parent_genes = []
    while len(parent_genes) != parent_length:#fill up parent_genes until max length of parent length
        parent_genes.extend(random.choice(geneset))
        
    return ''.join(parent_genes)

#generate a child from the mother
def _child(parent_genes, geneset):
    index = random.randrange(0, len(parent))
    child_genes = list(parent_genes)
    new_gene, alternate = random.sample(geneset, 2)
    child_genes[index] == alternate if new_gene == child_genes[index] else new_gene
    return ''.join(child_genes)

#does the child live or die?
def _child_viability(child):
    return sum(1 for actual, guess in zip(child, parent) if actual == guess)

print(_child_viability('gggjn'))
