#include <iostream>
#include <vector>

using namespace std;

vector<int> binarySearch(vector<vector<int>> &mat, int target) {
    vector<int> v;
    int row = 0;
    int col = mat[0].size() - 1;

    while(row < mat.size() && col >= 0) {
        if(mat[row][col] == target) {
            return v = {row, col};
        }
        else if(target > mat[row][col]) {
            row++;
        }
        else if(target < mat[row][col]) {
            col--;
        }
    }
    return {-1, -1};
}

int main() {
    vector<vector<int>> matrix = {{10, 20, 30, 40},
                                  {15, 25, 35, 45},
                                  {28, 29, 37, 49},
                                  {33, 34, 38, 50}};
    // vector<vector<int>> matrix = {{1, 3}};
    // std::cout << matrix[0].size();
                                                    
    vector<int> v = binarySearch(matrix, 34);
    std::cout << v[0] << ", " << v[1] << "\n";
}