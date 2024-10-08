class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Initialize the stack with the nested list and index
        self.stack = [(nestedList, 0)]

    def next(self) -> int:
        # We assume hasNext() is called before next(), so the stack should be pointing to an integer
        nestedList, idx = self.stack[-1]
        self.stack[-1] = (nestedList, idx + 1)  # Move the index forward after getting the integer
        return nestedList[idx].getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            nestedList, idx = self.stack[-1]

            # If we've reached the end of the current list, pop from the stack
            if idx == len(nestedList):
                self.stack.pop()
            else:
                element = nestedList[idx]
                
                if element.isInteger():
                    # The current element is an integer, we're ready to return it
                    return True
                else:
                    # The current element is a list, so we replace the current index and drill down
                    self.stack[-1] = (nestedList, idx + 1)  # Move index forward for the current list
                    self.stack.append((element.getList(), 0))  # Push the nested list onto the stack
        
        return False  # If the stack is empty, there are no more integers
