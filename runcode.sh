hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map8.py -reducer column_summ/reduce8.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results8.out

hfs -get results8.out

hfs -rm -r results8.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map9.py -reducer column_summ/reduce9.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results9.out
hfs -get results9.out results/
hfs -rm -r results9.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map10.py -reducer column_summ/reduce10.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results10.out
hfs -get results10.out results/
hfs -rm -r results10.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map11.py -reducer column_summ/reduce11.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results11.out
hfs -get results11.out results/
hfs -rm -r results11.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map12.py -reducer column_summ/reduce12.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results12.out
hfs -get results12.out results/
hfs -rm -r results12.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map13.py -reducer column_summ/reduce13.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results13.out
hfs -get results13.out results/
hfs -rm -r results13.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map14.py -reducer column_summ/reduce14.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results14.out
hfs -get results14.out results/
hfs -rm -r results14.out

hjs -D mapreduce.job.reduces=1 -files /home/yz3464/project/ds1004-project/column_summ -mapper column_summ/map15.py -reducer column_summ/reduce15.py -input /user/yz3464/NYPD.csv -output /user/yz3464/results15.out
hfs -get results15.out results/
hfs -rm -r results15.out

