# 735. Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row
# The indices of the asteroid represent their relative position in space.
# For each asteroid, the absolute value represents its size, and the sign represents
# its direction. Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.

from typing import List

class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    stack = []
    
    for a in asteroids:
      # No collisions if stack is empty
      if len(stack) == 0:
        stack.append(a)
        continue

      # While asteroid is headed left and top of stack is headed right
      while stack and a < 0 < stack[-1]:
        if abs(a) > stack[-1]: # If the new asteroid is bigger
          stack.pop()
          continue
        elif abs(a) == stack[-1]: # If the new asteroid and top of stack have same size
          stack.pop() 
        break
      else:
        stack.append(a)

    return stack

test = Solution()
print(test.asteroidCollision([1,-2,-2,-2]))
