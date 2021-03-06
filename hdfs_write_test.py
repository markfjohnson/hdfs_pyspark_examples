from pyspark import *
from pyspark import Row



from random import randrange,randint,choice
import uuid
import datetime




#----------------------------
sc = SparkContext(appName = "WriteRDD_10m")



#----------------------------

rowDef = Row("transGroup","CustomerId","companyGroup","CompanyName","Name","EMAIL","Address","CustomerSince","AnnualSales","LastOrderDate")




#----------------------------
def random_date(start, end):
    secRange = randrange(0, (end - start).total_seconds(),1)
    d = start + datetime.timedelta(secRange)
    return(unicode(d))

#here

def buildCustomerRDD(i) :
    d1 = datetime.date(randrange(2008,2016,1),randrange(1,12,1),1)
    d2 = datetime.date(2016,12,31)
    row = rowDef(i, str(uuid.uuid4()), choice(["GroupA","GroupB","GroupC"]),"ACME Widget", "John Doe", "abc@abc.com", "ABC",randrange(1990,2016,1), randrange(1000,10000,1000),d1)
    return(row);

#---------------- Begin Main Processing
a = sc.parallelize(range(1,100))
rddRows = a.map(lambda i: buildCustomerRDD(i) )
print("----------------------")

rddRows.saveAsTextFile('hdfs://10.0.2.149:9000/tmp/TEST_DATA.csv')
#df.write.format("csv").mode("overwrite").saveAsTable(tableName)
