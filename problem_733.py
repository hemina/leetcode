"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

https://leetcode.com/problems/flood-fill/

@author Mina HE
"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        nb_row = len(image)
        nb_col = len(image[0])
        old_color = image[sr][sc]
        delta_x = [0, 0, 1, -1]
        delta_y = [1, -1, 0, 0]
        self.old_image = self.new_image = image
        self.visited = set()

        def fill_pixel(x, y):
            if (x, y) not in self.visited:
                self.visited.add((x, y))
                if self.old_image[x][y] == old_color:
                    self.new_image[x][y] = newColor
                    for i in range(4):
                        new_x = x + delta_x[i]
                        new_y = y + delta_y[i]
                        if new_x >= 0 and new_x < nb_row and new_y >= 0 and new_y < nb_col:
                            fill_pixel(new_x, new_y)

        fill_pixel(sr, sc)
        return self.new_image


"""
Runtime: 56 ms, faster than 93.54% of Python online submissions.
Memory Usage: 12 MB, less than 54.55% of Python online submissions.
Complexity: O(m*n)
"""
