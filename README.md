## DS-GA 1004 Big Data Term Project  

**Li Lin Qin (llq205)     :+1:        Yidi Zhang (yz3464)      :shipit:       Yurui Mu (ym1495)**


For the first part of the project, we will analyze the data and generate a descriptive summary of their contents as well as a list of data quality issues. 


For the second part, we will integrate our selected collection with one or more data sets and look for interesting relationships between the data sets.


The dataset we will be using is NYPD Complaint Historical Data, which includes all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) from 2006 to the end of 2015.



All components of our project are reproducible.

__________________________________________________________________________

For Part I, we wrote a mapper and reducer for each column of NYPD_Complaint_Data_Historic.csv to examine  data type, null values and invalid values for each column. 
You could find the mapper and reducer codes in column_summ folder. To submit a hadoop job on NYU Dumbo, please run as following:

hjs -numReduceTasks 1 -file /home/<your-net-id> -mapper <your-net-id>/map<column-index>.py -reducer <your-net-id>/reduce<column-index>.py -input /user/<your-csv-input> -output /user/<your-net-id>/result<column-index>.out

hjs -numReduceTasks 1 -file /home/<your-net-id> -mapper <your-net-id>/map<column-name>.py -reducer <your-net-id>/reduce_by_key.py -input /user/<your-csv-input> -output /user/<your-net-id>/result<column-name>.out

For Part II, we used PySpark to join tables and making queries on NYU Dumbo. 
To submit PySpark job, please run as following:

spark-submit <0>.py <csv1>.csv <csv2>.csv <output>.out  

For plotting in our project, please refer to jupyter notebooks in code_for_plots folder. And the plots are saved in image_new folder.  
