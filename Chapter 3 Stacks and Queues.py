# 3.1
# pass
# 3.2
# pass
# 3.3
# pass
# 3.4
class Tower:
    def __init__(self, index):
        self.stack = []
        self.index = index

    def moveTopTo(self, tower):
        disk = self.stack.pop()
        tower.stack.append(disk)
        print "Move Disk", disk, "from Stack", self.index, "to Stack", tower.index 

    def moveDisks(self, n, destination, buffer):
        if n<=0: return
        self.moveDisks(n-1, buffer, destination)
        self.moveTopTo(destination)
        buffer.moveDisks(n-1, destination, self)

    def add(self, disk):
        self.stack.append(disk)

# 3.5 
# 3.6
# 3.7

if __name__ == "__main__":
    # 3.1
    #.3.2
    # 3.3
    # 3.4
    print "# 3.4"
    n = 4
    tower1 = Tower(1); tower2 = Tower(2); tower3 = Tower(3)
    for i in reversed(range(n)): tower1.add(i+1)
    tower1.moveDisks(n, tower3, tower2)
    # 3.5 
    # 3.6
    # 3.7
    