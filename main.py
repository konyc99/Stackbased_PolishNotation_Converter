#!/bin/python3

import numpy as np
from pythonds.basic import Stack

def ExpressionTypeDetection(expression):
    if expression[0] in "()+-*/^":
        print("Your expression is in Polish notation")
        return 0
    elif expression[len(expression)-1] in "+-*/^":
        print("Your expression is in Reverse Polish notation")
        return 1
    else:
        print("Your expression is in regular/infix notation")
        return 2

def revExpression(expression):
    revExp = []
    for c in expression[::-1]:
        if c == "(":
            revExp.append(')')
        elif c == ")":
            revExp.append('(')
        else:
            revExp.append(c)
    return revExp


def InfixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    infixexpr=infixexpr.lower().replace(" ", "")

    tokenList = list(infixexpr)
    #print(tokenList)

    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz":
            postfixList.append(token)
        elif token == '(':
            #pushing to operand stack
            opStack.push(token)
        elif token == ')':
            # removes top operand from operand stack
            topToken = opStack.pop()
            # until bracket is matched we append all other operators
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            # while there are operands left in the OpStack
            # and precedence of top >= precedence of current token
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                # append top of stack/peeked element to postfix expression
                  postfixList.append(opStack.pop())
            #then add the token to OpStack
            opStack.push(token)
    #once all tokens are cycled through append the rest
    #of the stack to the postfix expression by popping from the top
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def InfixToPrefix(infixexp):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    prefixList = []
    infixexp = infixexp.lower().replace(" ", "")

    tokenList = revExpression(infixexp)
    #print(tokenList)

    for token in tokenList:
       # print(prefixList,'###',token)
        if token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(' and not opStack.isEmpty():
                prefixList.append(opStack.pop())
            opStack.pop()
        elif token in "abcdefghijklmnopqrstuvwxyz":
            prefixList.append(token)
        else:
            while not opStack.isEmpty() and prec[token] < prec[opStack.peek()]:
                prefixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        prefixList.append(opStack.pop())

    finalExpression =  " ".join(prefixList)
    return finalExpression[::-1]

def PrefixToInfix(prefixExp):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    infixList = []
    prefixExp = prefixExp.lower().replace(" ", "")

    tokenList = revExpression(prefixExp)

    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "1234567890":
            infixList.append(token)
        elif token in prec.keys():
            top1 = infixList.pop()
            top2 = infixList.pop()
            full_operand = top2+token+top1
            infixList.append(full_operand)
    finalExpression = " ".join(infixList)
    return finalExpression[::-1]

def PostfixToInfix(postfixExp):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    infixList = []
    postfixExp = postfixExp.lower().replace(" ", "")

    tokenList = list(postfixExp)

    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "1234567890":
            infixList.append(token)
        elif token in prec.keys():
            top1 = infixList.pop()
            top2 = infixList.pop()
            full_operand = top2 + token + top1
            infixList.append(full_operand)
    finalExpression = " ".join(infixList)
    return finalExpression


if __name__ == '__main__':
    """
    print(InfixToPrefix("a + b"))
    print(InfixToPostfix ("A+B-C*(D-E)"))
    print(PrefixToInfix('- + a b * c - d e'))
    print(PostfixToInfix("a b + c d e - * -"))
    """
    Exp = input("Input your expression, please try to avoid unnecessary spaces\n")
    type = ExpressionTypeDetection(Exp)
    if type ==0:
        exp1 = PrefixToInfix(Exp)
        exp2 = InfixToPostfix(exp1)
        print(Exp+'\n',exp1+'\n',exp2)
    elif type ==1:
        exp1 = PostfixToInfix(Exp)
        exp2 = InfixToPrefix(exp1)
        print(exp2+'\n',exp1+'\n',Exp)
    elif type ==2:
        exp1 = InfixToPrefix(Exp)
        exp2 = InfixToPostfix(Exp)
        print(exp1+'\n',Exp+'\n',exp2)
