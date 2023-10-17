def recurse_down(number):
        if number == 0:
            print(number)
            return number
        print(number)
        return recurse_down(number - 1)
recurse_down(10)

def recurse_up(start, end): # notice when you increment in a recursive loop, you'll need an additional parameter for the upper limit
      if start <= end:
            print(start)
            recurse_up(start + 1, end)  
recurse_up(0, 10)