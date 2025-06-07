# Initial Attempt
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Take car add to a stack. If car will be caught up to by stack behind it,
        # before target, pop that car in the stack. As you can only go the speed of
        # the top car, that limits all other cars so it will never get popped.
        stack = []
        # To find if a car will reach the car in front of it, we need to take the
        # distance at which they will meet, and see if that distance is less than
        # the target?
        # distance = speed x time
        # so we need to have a timer t, that ticks and checks the distance from position
        # i after t seconds. If that distance > the car in front of it, then we pop that 
        # car from stack and it becomes part of the convoy. I think I'll do this one car
        # at a time so I need to take index i as i represents a car.
        # So i need to take a car and then iterate it through time so I need two loops.
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars:
            distance = 0
            time = 0
            if not stack:
                stack.append((target-pos)/spd)
            else:
                time = (target - pos)/spd
                if time > stack[-1]:
                    stack.append(time)
                else:
                    continue

        return len(stack)
        
# Better, simpler solution where you just append to stack then compare:
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



        