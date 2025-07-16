Hello! this program is made for clustering a dataset automatically and avoid wasting time, because lots of clustering programs are alike. It gets main and X datasets and train k-means and DBSCAN with X dataset. It gets best n_clusters and best eps for each algorithm and compare the results (with silhoutte score) and uses the better algorithm to predict the clusters. It seperates main dataset by model output labels and save the new datasets in results/dfs folder (for example, it detects that there are 3 clusters, there will be 3 new datasets containing rows of each cluster). There probably will be a dataset specific for outliers. <br>
<h2>Tips:</h2>
  1. You should do preprocessing and transforming categorical data to binary (OneHotEncode) yourself.<br>
  2. You should make 2 datasets, 1- main dataset containing all data, 2- X dataset containing just columns that are used to train the model.<br>
  3. Each time that you run this program, it automatically deletes data of previous run, so, be careful and backup your data.<br>
  4. Make sure that you are on app folder in terminal when running code.


<h2>PCA:</h2>
  You can turn on PCA, it transform all columns to 2 columns. It sometimes causes model performs better, the other reason to use it is the program can make a 2d plot for visualization. Dont use PCA if your X dataset just has 2 columns (features).

<h2>Output:</h2>
  Results will be saved in results directory. If you use PCA or your X dataset just has 2 columns, the plot will be saved in results/images. Datasets of each cluster will be saved in results/dfs as df_{number of cluster}.csv.
