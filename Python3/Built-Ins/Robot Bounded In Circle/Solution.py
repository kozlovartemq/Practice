class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        point = [0, 0]
        # directions = ["North", "East", "South", "West"]
        index = 0
        # face = directions[index]
        for i in instructions:
            if i == "G":
                if index == 0:
                    point[1] = point[1] + 1
                elif index == 1:
                    point[0] = point[0] + 1
                elif index == 2:
                    point[1] = point[1] - 1
                elif index == 3:
                    point[0] = point[0] - 1
            elif i == "R":
                index = (index + 1) % 4
                # face = directions[index]
            elif i == "L":
                index = (index - 1) % 4
                # face = directions[index]
        if point == [0, 0] or index != 0:  # The condition of a robot staying in Circle: return to 0 point or change the direction.
            return True
        else:
            return False
