# The recursive function that jumbles all items in a string. 
def jumble(inList, first, last):
    
        # This is the base case of the recursive function, once last equals the first. 
	if first == last: 
		print(inList)
	else:
            
            # For loop parses through and uses each constituent as a pivot.
	    for x in range(first,last+1):

                    # First value in list is switched with the pivot value /
                    # Pivot value in list is switched with the first value in the list. 
		    inList[first], inList[x] = inList[x], inList[first]

		    # Recursive function that calls itself to jumble each constituent. /
		    # first index is incremented to select the next constituent. 
		    jumble(inList, first+1, last)

		    # First and pivot value are swapped again and used as a backtrack. /
		    # The backtrack makes sure there the original list is used for the next recursion. 
		    inList[first], inList[x] = inList[x], inList[first]

# The string is turned into a list where the letters can be given an index. 
def main():
	inString = "abcde"
	inList = list(inString)

	# The first call to jumble that starts the recursion. 
	jumble(inList, 0, len(inList)-1)
	
main()
