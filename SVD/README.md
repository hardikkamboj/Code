In Singular Vector Decomposition, we are expressing a matrix X of shape (n,m), where we are assuming that n >> m. For example, X is a matrix where each col are
representing an image converted to a col. n would be the size of that col matrix, and m would be the number of images we have. 

Through SVD, we represent this X, as a prodcut of three other matrices, each having unique properties, these can be furthur written as a sum of m rank 1 matrices. 

Out of these m rank one matrices, we can select some arbitrary r rank matrix, which gives us the best approximation of X. 
