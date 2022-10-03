from collections import deque
from shutil import move

if __name__ == "__main__":
    movieStars = deque()
    movieStars.append("Tom Cruise")
    movieStars.append("Hugo Weaving")
    movieStars.append("Robert Downey Jr")
    movieStars.append("Aaron Paul")
    movieStars.append("Natalie Portman")
    movieStars.append("Anthony Hopkins")
    #Now we insert new names in the middle and both ends
    movieStars.append("Keanu Reeves")# Right
    movieStars.appendleft("Jack Nicholson")#Left
    movieStars.insert(len(movieStars)//2, "Luis Gerardo Mendez")#Middle
    print("After adding in the midddle and both ends")
    print(movieStars)
    #now, we remove two of the original names. In this case, we cant just use pop, as we would just
    #remove the new name. So we use remove
    movieStars.remove("Tom Cruise")
    movieStars.remove("Hugo Weaving")
    print("After removing two of the original names")
    print(movieStars)
    #Now we can remove the first and last entries, so we just use pop and popleft
    movieStars.popleft()
    movieStars.pop()
    print("After removing from the front and the rear")
    print(movieStars)