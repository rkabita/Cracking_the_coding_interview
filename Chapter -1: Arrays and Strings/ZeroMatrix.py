'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


'''

void setMatrixZeros(int A[][], int M, int N)
{
    bool row[M], col[N]
    
    for(i = 0 to M-1)
        row[i] = false
    for(j = 0 to N-1)
        col[j] = false
    
    for(i = 0 to M-1)
    {
        for(j = 0 to N-1)
        {
            if(A[i][j] == 0) 
            {
                row[i] = true
                col[j] = true
            }
        }
    }
    
    for(i = 0 to M-1)
    {
        for(j = 0 to N-1)
        {
            if(row[i] == true or col[j] == true)
                A[i][j] = 0
        }
    }
}