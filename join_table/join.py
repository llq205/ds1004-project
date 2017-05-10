from __future__ import print_function

import sys

from pyspark import SparkContext

def create_crime_pair(crime):
    features = crime.strip().split(',')
    key = (features[19],features[20])
    values = ",".join(features)
    return (key, values)

def create_graffiti_pair(graffiti):
    features = graffiti.strip().split(",", 1)
    key = (features[-2],features[-1])
    values =",".join(features)
    return (key,values)

if __name__ == "__main__":

    # Create SparkContext
    sc = SparkContext(appName="DatasetJoin")

    # Read first file: trips data
    crimeData = sc.textFile(sys.argv[1])

    # Read second file: demographic data
    graffiti = sc.textFile(sys.argv[2])

    # Split by comma (take the datetime as key and all the line as value)
    crime_values = crimeData.map(create_crime_pair)
    #print(crime_values.take())
    graffiti_values = graffiti.map(create_graffiti_pair)

    # Left Join
    joined = crime_values.join(graffiti_values)
    joined_csv = joined.map(lambda res: str(res[1][0]) + ',' + str(res[1][1]))
    output = joined_csv.saveAsTextFile(sys.argv[3])
    sc.stop()
