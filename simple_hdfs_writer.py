path = new Path("hdfs://namenode:8020/some/folder/myfile.txt")
conf = new Configuration(spark.sparkContext.hadoopConfiguration)
conf.setInt("dfs.blocksize", 16 * 1024 * 1024) // 16MB HDFS Block Size
fs = path.getFileSystem(conf)
if (fs.exists(path))
    fs.delete(path, true)
out = new BufferedOutputStream(fs.create(path)))
txt = "Some text to output"
out.write(txt.getBytes("UTF-8"))
out.flush()
out.close()
fs.close()