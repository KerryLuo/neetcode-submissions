# iterature through indexes in reverse
# Add to stack, next item
# if less than stack, assign the value (diff of indices) and add i to stack
# each time, pop values in stack until top i is greater than element
# then calculate the value (diff) and add to stack
# the stack stores the indices of the temperatures, then you access it to get the actual temp
# if values are the same, pop() and calculate with next
# only greater temp counts

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # log of all temperatures you've iterated over
        tmps = []

        # num of days until a warmer day
        warmer = []

        for i in reversed(range(len(temperatures))):
            # add first value
            if i == len(temperatures) - 1:
                warmer.append(0)
                tmps.append(i)
                continue
            
            # less
            if temperatures[i] < temperatures[tmps[-1]]:
                warmer.append(tmps[-1] - i)
                tmps.append(i)

            # greater or equal
            else:
                reset = False
                
                while temperatures[i] >= temperatures[tmps[-1]]:
                    if len(tmps) == 1:
                        tmps.pop()
                        warmer.append(0)
                        tmps.append(i)

                        reset = True
                        break
                    
                    tmps.pop()
                
                if reset == False:
                    warmer.append(tmps[-1] - i)
                    tmps.append(i)
        
        return warmer[::-1]



            
            

        