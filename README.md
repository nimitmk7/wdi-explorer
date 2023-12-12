# WDI Explorer

This repo contains the code and dataset for the research paper "World Development Indicators Data: Evaluating Data Deprivation Across Country Income Levels".

## Setup

To clone the repository, use the following command: 
```
git clone git@github.com:nimitmk7/wdi-explorer.git
```

To install the required dependencies, please run the following command: 

```
pip install -r requirements.txt
```

To upload all the dataset files to Hadoop, please follow the following steps:

```
Note: Make sure your system can access the hadoop cluster.

1. Using CLI, navigate to the Data folder and use the following Hadoop command to upload CSV files to the Hadoop Distributed File System. Replace '<path_to_cloned_repository>' with the location of the cloned repository on your system. Please ensure that the '<filename>' should be the same as present in Data folder.

2. hdfs dfs -put <path_to_cloned_repository>/Data/<filename>.csv <filename>.csv

```

To merge the dataset, please follow the following steps :

```
1. Delete the file 'final_merge_data.csv' if it exists from the hadoop cluster. Please run the following command from the CLI.
hdfs dfs -rm -r final_merge_data.csv

2. Using CLI, navigate to the location where 'merge_data.py' is present

3. Run spark-submit merge_data.py

Note: After the spark job is successfully executed, a file called 'final_merge_data.csv' will be created.
```

To run the analysis run the file Final_Analysis_Big_Data.ipynb in a Jupyter Notebook.


