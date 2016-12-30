def matchParenthesis(str):

    counter = None

    for i in str:
        if counter == 0:
            return str[i]
        else:
            if i == "(":
                if counter==None:
                    counter = 1
                else:
                    counter +=1

def matchParenthesis1(str,i):

    for x in range (i+1, len(str)):
        if x == ")":
            return str[x]
        else:
            print("Parenthesis incomplete")


# using stack

def Evaluate(str):
  stack = []
  pushChars, popChars = "<({[", ">)}]"
  for c in str :
    if c in pushChars :
      stack.append(c)
    elif c in popChars :
      if not len(stack) :
        return False
      else :
        stackTop = stack.pop()
        balancingBracket = pushChars[popChars.index(c)]
        if stackTop != balancingBracket :
          return False
    else :
      return False
  return not len(stack)

