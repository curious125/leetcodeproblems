class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>T(numRows);
        for(int i = 0;i < numRows;i++){
            T[i].resize(i+1,1);//changing rowvalues to 1s
            for(int j = 1;j < i;j++){
                T[i][j] = T[i-1][j-1] + T[i-1][j];
            }
        }
        return T;
    }
};