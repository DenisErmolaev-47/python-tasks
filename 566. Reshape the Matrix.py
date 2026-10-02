class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        flat_list = [num for row in mat for num in row]
        reshaped_matrix = []
        for i in range(r):
            row_slice = flat_list[i * c : (i + 1) * c]
            reshaped_matrix.append(row_slice)
            
        return reshaped_matrix
