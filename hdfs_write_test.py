from pyspark import *
from pyspark import Row



from random import randrange,randint,choice
import uuid
import datetime





tableName = "CUSTOMER_INFO10"

#----------------------------
sc = SparkContext(appName = "WriteRDD_10m")
sc.addPyFiles("simple_hdfs_writer-0.1-py2.7.egg")


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
print(rddRows.toDebugString())


#df.printSchema()
print("----------- \n\n\n\n")


#hc.sql("CREATE TABLE CUSTOMER_INFO3 (transGroup int,customerId STRING, CompanyName String,contactName String, EMAIL string,Address string,CustomerSince INT, AnnualSales FLOAT,LastOrderDate DATE);")

#df.show()
print("----------------------")

#print (df.count())
startTime = datetime.datetime.now()
#a = df.collect()
endTime = datetime.datetime.now()
print("Elapsed Time = {0}".format(endTime-startTime))
df.write.format("csv").mode("overwrite").saveAsTable(tableName)
