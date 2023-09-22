import re
import pandas as pd
from node import Node
import numpy as np
from operators import Operator


def extract_words(path):
    file = open(path)
    labels = []
    dashCount = []
    while True:
        line = file.readline()
        if not line:
            break
        if line[0] != '-':
            continue
        numDash = 0
        for char in line:
            if char != '-':
                break
            numDash += 1
        line = line.strip('-')
        words = line.split()

        if words[0] == 'FUNCTION':
            labels.append(words[1])
            dashCount.append(numDash)
        else:
            labels.append(words[0])
            dashCount.append(numDash)

    return labels, dashCount



def adapt_node_label(labels, dashCount):
    while True:
        if labels[0] == "MAIN":
            break
        labels.pop(0);
        dashCount.pop(0);
    for label in labels:
        if ".builtinNS::" in label:
            index = labels.index(label)
            label = "func: " + label[12:]
            labels[index] = label
    n= 1
    for i in range(len(labels)):
        if 'MAIN' in labels[i] or 'func' in labels[i] or 'CP' in labels[i] or 'SPARK' in labels[i]:
            continue
        num = str(n)
        labels[i] = labels[i] + " " +num
        n +=1


def extract_tree_labels(words, dashCount):
    labels = []
    dashCountTree = []
    for i in range(len(words)):
        if 'CP' in words[i] or 'SPARK' in words[i]:
            continue
        labels.append(words[i])
        dashCountTree.append(dashCount[i])
    return labels, dashCountTree



def add_tree_nodes(labels, dashCount):

    names = []
    parents = []
    dashCountMain = dashCount[0]
    index = 1

    while index < len(labels):
        if dashCount[index] < dashCountMain:
            break
        index += 1
    names.append('MAIN')
    parents.append('')

    for i in range(1, index):
        names.append(labels[i])
        numDash = dashCount[i]
        x = i-1
        while x >= 0:
            if numDash - dashCount[x] == 2:
                parents.append(labels[x])
                break
            x -= 1

    for i in range(index,len(labels)):
        if 'MAIN' in labels[i] or 'func' in labels[i]:
            continue
        names.append(labels[i])
        numDash = dashCount[i]
        x= i-1
        while x >= index:
            if numDash - dashCount[x] == 2:
                parents.append((labels[x]))
                break
            x -= 1
    return names, parents


def sankey_index(words, dashCount, treeNode):
    i = words.index(treeNode)
    startIndex = i+1

    parentDash = dashCount[i]
    childDash = parentDash + 2
    index = startIndex
    while dashCount[index] == childDash:
        index += 1

    endingIndex = index-1
    return startIndex, endingIndex

def extract_sankey_lines(path, startIndex, endingIndex):
    file = open(path)
    lines = []
    sankeylines = []
    while True:
        line = file.readline()
        if not line:
            break
        if line[0] != '-':
            continue
        line = line.strip('-')
        line = line.split()
        lines.append(line)
    while True:
        line = lines[0]
        if line[0] == "MAIN":
            break
        lines.pop(0)
    for i in  range(startIndex, endingIndex+1):
        sankeylines.append(lines[i])

    length = len(sankeylines)
    x=0
    for i in range(length):
        if x > length:
            break
        line = sankeylines[x]
        if line[1] == 'createvar' or line[1] == 'rmvar':
            sankeylines.pop(x)
        else:
            x += 1

    return sankeylines

def sankey_versions(lines):
    cp = []
    spark = []
    for line in lines:
        if line[0] == "CP":
            cp.append(line)
        else:
            spark.append(line)
    return cp, spark

def create_operations(lines):
    operators = []
    for line in lines:
        name = line[1]
        input = []
        if name == 'seq':
            input.append(line[5])
            input.append(line[6])
            input.append(line[7])
            output = line[8]
        elif name == 'rand':
            input.append(line[2])
            input.append(line[3])
            i = len(line)-1
            output = line[i]
        else:
            input.append(line[2])
            output = line[3]
        operator = Operator(name, input, output)
        operators.append(operator)
    return operators

def create_sankey_nodes(operators):
    labels = []
    source = []
    target = []
    value = []
    for operator in operators:
        labels.append(operator.get_name())

    for x in range(len(operators)-1):
        operator1 = operators[x]
        name1 = operator1.get_name()
        output1 = operator1.get_output()
        for y in range(x+1, len(operators)):
            operator2 = operators[y]
            name2 = operator2.get_name()
            input2 = operator2.get_input()
            for input in input2:
                if output1 in input or input in output1:
                    source.append(x)
                    target.append(y)
    if len(source) == 0:
        source.append(0)
        target.append(1)
    for i in range(len(labels)):
        value.append(1)
    return labels, source, target, value















