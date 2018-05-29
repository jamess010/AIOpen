# -*- coding: UTF-8 -*-
###spark streaming&&kafka
# 安装hadoop-2.7.6, kafka_2.10-0.8.2.0, spark-2.0.1-bin-hadoop2.7, zookeeper-3.4.12
# start-dfs.sh, zookeeper-server-start.sh ../config/zookeeper.properties
# bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
# spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.2.jar KafkaWordCount.py 2> error.txt


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc=SparkContext("local[2]","KafkaWordCount")
#处理时间间隔为1s
ssc=StreamingContext(sc,2)
zookeeper="192.168.31.86:2181,192.168.31.86:2182,192.168.31.86:2183"
#打开一个TCP socket 地址 和 端口号
topic={"test5":0,"test5":1,"test5":2}
groupid="test-consumer-group"
lines = KafkaUtils.createStream(ssc, zookeeper,groupid,topic)
lines1=lines.map(lambda x:x[1])

#对1s内收到的字符串进行分割
words=lines1.flatMap(lambda line:line.split(" "))

#映射为（word，1）元祖
pairs=words.map(lambda word:(word,1))

wordcounts=pairs.reduceByKey(lambda x,y:x+y)

#输出文件，前缀+自动加日期
wordcounts.saveAsTextFiles("/tmp/fkafka")

wordcounts.pprint()

#启动spark streaming应用
ssc.start()
#等待计算终止
ssc.awaitTermination()

