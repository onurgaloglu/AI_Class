Python 3.7.1


First Task:

First, I created objects for each element of the grid to store each element's coordinate, symbol, h value, 
g value, f value and I also overrode some of the opeartors, as binary heaps (that I used as priority queue) 
can't compare class objects. Then, I wrote the heuristics for the a* search algorithm which I chose as the 
euclidian distance. In the search part, elements in the priority queue(frontier) are first checked if they are 
goal node, if not, each element with the symbol "_" are added to the priority queue (as long as they are not already 
in frontier or expored set). Search continues until either there is frontier is empyt or goal node is found. 


Second Task: 

Like the first task, I created objects for each element of the grid and stored their coordinates 
and symbols accordingly. Afterwards, I looked for the objects, which have symbol as "." and locate on 
the boundary, then pushed them into a queue. Later I implemented a search so that I can detect the all
neighbors of the elements in the queue which have symbol as "." and push them to the queue. The algorithm 
continues until there is no elment left in the queue (while checking for each new element whether they 
have already been checked nor already on the list to be checked). Now I have a list of elements which are 
connected with the "." elements on the boundaries which means that they won't be converted. Other "."
elements of the grid, however, converted into "*".