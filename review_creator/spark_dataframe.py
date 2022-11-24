from pyspark.sql.functions import col
from pyspark.sql.functions import when
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf

data_bunsik = spark.read.csv("hdfs://hadoop-name:9000/input/bunsik.csv")
data_cafe_dessert = spark.read.csv("hdfs://hadoop-name:9000/input/cafe_dessert.csv")
data_chicken = spark.read.csv("hdfs://hadoop-name:9000/input/chicken.csv")
data_hansik = spark.read.csv("hdfs://hadoop-name:9000/input/hansik.csv")
data_ilsik = spark.read.csv("hdfs://hadoop-name:9000/input/ilsik.csv")
data_joongsik = spark.read.csv("hdfs://hadoop-name:9000/input/joongsik.csv")
data_pizza = spark.read.csv("hdfs://hadoop-name:9000/input/pizza.csv")
data_jokbo = spark.read.csv("hdfs://hadoop-name:9000/input/jokbo.csv")


df_bunsik = data_bunsik.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_cafe_dessert = data_cafe_dessert.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_chicken = data_chicken.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_hansik = data_hansik.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_ilsik = data_ilsik.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_joongsik = data_joongsik.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_pizza = data_pizza.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_jokbo = data_jokbo.select(col('_c3').alias('taste'),
                        col('_c4').alias('amount'),
                        col('_c5').alias('delivery'),
                        col('_c6').alias('review'))

df_bunsik_filter = df_bunsik[~((df_bunsik['taste']=='-') | (df_bunsik['amount']=='-') | (df_bunsik['delivery']=='-'))].drop()
df_cafe_dessert_filter = df_cafe_dessert[~((df_cafe_dessert['taste']=='-') | (df_cafe_dessert['amount']=='-') | (df_cafe_dessert['delivery']=='-'))].drop()
df_chicken_filter = df_chicken[~((df_chicken['taste']=='-') | (df_chicken['amount']=='-') | (df_chicken['delivery']=='-'))].drop()
df_hansik_filter = df_hansik[~((df_hansik['taste']=='-') | (df_hansik['amount']=='-') | (df_hansik['delivery']=='-'))].drop()
df_ilsik_filter = df_ilsik[~((df_ilsik['taste']=='-') | (df_ilsik['amount']=='-') | (df_ilsik['delivery']=='-'))].drop()
df_joongsik_filter = df_joongsik[~((df_joongsik['taste']=='-') | (df_joongsik['amount']=='-') | (df_joongsik['delivery']=='-'))].drop()
df_pizza_filter = df_pizza[~((df_pizza['taste']=='-') | (df_pizza['amount']=='-') | (df_pizza['delivery']=='-'))].drop()
df_jokbo_filter = df_jokbo[~((df_jokbo['taste']=='-') | (df_jokbo['amount']=='-') | (df_jokbo['delivery']=='-'))].drop()


### 분식
df_bunsik_Twhen=df_bunsik_filter.select(col("*"), when(df_bunsik_filter.taste == "5","맛2")

    .when(df_bunsik_filter.taste == "4","맛1")
    
    .when(df_bunsik_filter.taste == "3","맛0")

    .when(df_bunsik_filter.taste == "2","맛0")

    .when(df_bunsik_filter.taste == "1","맛0")

    .when(df_bunsik_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_bunsik_Awhen=df_bunsik_Twhen.select(col("*"), when(df_bunsik_filter.amount == "5","양2")

    .when(df_bunsik_filter.amount == "4","양1")
    
    .when(df_bunsik_filter.amount == "3","양0")

    .when(df_bunsik_filter.amount == "2","양0")

    .when(df_bunsik_filter.amount == "1","양0")

    .when(df_bunsik_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_bunsik_final_when=df_bunsik_Awhen.select(col("*"), when(df_bunsik_filter.delivery == "5","배달2")

    .when(df_bunsik_filter.delivery == "4","배달1")
    
    .when(df_bunsik_filter.delivery == "3","배달0")

    .when(df_bunsik_filter.delivery == "2","배달0")

    .when(df_bunsik_filter.delivery == "1","배달0")

    .when(df_bunsik_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 카페/디저트
df_cafe_dessert_Twhen=df_cafe_dessert_filter.select(col("*"), when(df_cafe_dessert_filter.taste == "5","맛2")

    .when(df_cafe_dessert_filter.taste == "4","맛1")
    
    .when(df_cafe_dessert_filter.taste == "3","맛0")

    .when(df_cafe_dessert_filter.taste == "2","맛0")

    .when(df_cafe_dessert_filter.taste == "1","맛0")

    .when(df_cafe_dessert_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_cafe_dessert_Awhen=df_cafe_dessert_Twhen.select(col("*"), when(df_cafe_dessert_filter.amount == "5","양2")

    .when(df_cafe_dessert_filter.amount == "4","양1")
    
    .when(df_cafe_dessert_filter.amount == "3","양0")

    .when(df_cafe_dessert_filter.amount == "2","양0")

    .when(df_cafe_dessert_filter.amount == "1","양0")

    .when(df_cafe_dessert_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_cafe_dessert_final_when=df_cafe_dessert_Awhen.select(col("*"), when(df_cafe_dessert_filter.delivery == "5","배달2")

    .when(df_cafe_dessert_filter.delivery == "4","배달1")
    
    .when(df_cafe_dessert_filter.delivery == "3","배달0")

    .when(df_cafe_dessert_filter.delivery == "2","배달0")

    .when(df_cafe_dessert_filter.delivery == "1","배달0")

    .when(df_cafe_dessert_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 치킨
df_chicken_Twhen=df_chicken_filter.select(col("*"), when(df_chicken_filter.taste == "5","맛2")

    .when(df_chicken_filter.taste == "4","맛1")
    
    .when(df_chicken_filter.taste == "3","맛0")

    .when(df_chicken_filter.taste == "2","맛0")

    .when(df_chicken_filter.taste == "1","맛0")

    .when(df_chicken_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_chicken_Awhen=df_chicken_Twhen.select(col("*"), when(df_chicken_filter.amount == "5","양2")

    .when(df_chicken_filter.amount == "4","양1")
    
    .when(df_chicken_filter.amount == "3","양0")

    .when(df_chicken_filter.amount == "2","양0")

    .when(df_chicken_filter.amount == "1","양0")

    .when(df_chicken_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_chicken_final_when=df_chicken_Awhen.select(col("*"), when(df_chicken_filter.delivery == "5","배달2")

    .when(df_chicken_filter.delivery == "4","배달1")
    
    .when(df_chicken_filter.delivery == "3","배달0")

    .when(df_chicken_filter.delivery == "2","배달0")

    .when(df_chicken_filter.delivery == "1","배달0")

    .when(df_chicken_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 한식
df_hansik_Twhen=df_hansik_filter.select(col("*"), when(df_hansik_filter.taste == "5","맛2")

    .when(df_hansik_filter.taste == "4","맛1")
    
    .when(df_hansik_filter.taste == "3","맛0")

    .when(df_hansik_filter.taste == "2","맛0")

    .when(df_hansik_filter.taste == "1","맛0")

    .when(df_hansik_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_hansik_Awhen=df_hansik_Twhen.select(col("*"), when(df_hansik_filter.amount == "5","양2")

    .when(df_hansik_filter.amount == "4","양1")
    
    .when(df_hansik_filter.amount == "3","양0")

    .when(df_hansik_filter.amount == "2","양0")

    .when(df_hansik_filter.amount == "1","양0")

    .when(df_hansik_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_hansik_final_when=df_hansik_Awhen.select(col("*"), when(df_hansik_filter.delivery == "5","배달2")

    .when(df_hansik_filter.delivery == "4","배달1")
    
    .when(df_hansik_filter.delivery == "3","배달0")

    .when(df_hansik_filter.delivery == "2","배달0")

    .when(df_hansik_filter.delivery == "1","배달0")

    .when(df_hansik_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 일식
df_ilsik_Twhen=df_ilsik_filter.select(col("*"), when(df_ilsik_filter.taste == "5","맛2")

    .when(df_ilsik_filter.taste == "4","맛1")
    
    .when(df_ilsik_filter.taste == "3","맛0")

    .when(df_ilsik_filter.taste == "2","맛0")

    .when(df_ilsik_filter.taste == "1","맛0")

    .when(df_ilsik_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_ilsik_Awhen=df_ilsik_Twhen.select(col("*"), when(df_ilsik_filter.amount == "5","양2")

    .when(df_ilsik_filter.amount == "4","양1")
    
    .when(df_ilsik_filter.amount == "3","양0")

    .when(df_ilsik_filter.amount == "2","양0")

    .when(df_ilsik_filter.amount == "1","양0")

    .when(df_ilsik_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_ilsik_final_when=df_ilsik_Awhen.select(col("*"), when(df_ilsik_filter.delivery == "5","배달2")

    .when(df_ilsik_filter.delivery == "4","배달1")
    
    .when(df_ilsik_filter.delivery == "3","배달0")

    .when(df_ilsik_filter.delivery == "2","배달0")

    .when(df_ilsik_filter.delivery == "1","배달0")

    .when(df_ilsik_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 중식
df_joongsik_Twhen=df_joongsik_filter.select(col("*"), when(df_joongsik_filter.taste == "5","맛2")

    .when(df_joongsik_filter.taste == "4","맛1")
    
    .when(df_joongsik_filter.taste == "3","맛0")

    .when(df_joongsik_filter.taste == "2","맛0")

    .when(df_joongsik_filter.taste == "1","맛0")

    .when(df_joongsik_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_joongsik_Awhen=df_joongsik_Twhen.select(col("*"), when(df_joongsik_filter.amount == "5","양2")

    .when(df_joongsik_filter.amount == "4","양1")
    
    .when(df_joongsik_filter.amount == "3","양0")

    .when(df_joongsik_filter.amount == "2","양0")

    .when(df_joongsik_filter.amount == "1","양0")

    .when(df_joongsik_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_joongsik_final_when=df_joongsik_Awhen.select(col("*"), when(df_joongsik_filter.delivery == "5","배달2")

    .when(df_joongsik_filter.delivery == "4","배달1")
    
    .when(df_joongsik_filter.delivery == "3","배달0")

    .when(df_joongsik_filter.delivery == "2","배달0")

    .when(df_joongsik_filter.delivery == "1","배달0")

    .when(df_joongsik_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 피자
df_pizza_Twhen=df_pizza_filter.select(col("*"), when(df_pizza_filter.taste == "5","맛2")

    .when(df_pizza_filter.taste == "4","맛1")
    
    .when(df_pizza_filter.taste == "3","맛0")

    .when(df_pizza_filter.taste == "2","맛0")

    .when(df_pizza_filter.taste == "1","맛0")

    .when(df_pizza_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_pizza_Awhen=df_pizza_Twhen.select(col("*"), when(df_pizza_filter.amount == "5","양2")

    .when(df_pizza_filter.amount == "4","양1")
    
    .when(df_pizza_filter.amount == "3","양0")

    .when(df_pizza_filter.amount == "2","양0")

    .when(df_pizza_filter.amount == "1","양0")

    .when(df_pizza_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_pizza_final_when=df_pizza_Awhen.select(col("*"), when(df_pizza_filter.delivery == "5","배달2")

    .when(df_pizza_filter.delivery == "4","배달1")
    
    .when(df_pizza_filter.delivery == "3","배달0")

    .when(df_pizza_filter.delivery == "2","배달0")

    .when(df_pizza_filter.delivery == "1","배달0")

    .when(df_pizza_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


### 족발보쌈
df_jokbo_Twhen=df_jokbo_filter.select(col("*"), when(df_jokbo_filter.taste == "5","맛2")

    .when(df_jokbo_filter.taste == "4","맛1")
    
    .when(df_jokbo_filter.taste == "3","맛0")

    .when(df_jokbo_filter.taste == "2","맛0")

    .when(df_jokbo_filter.taste == "1","맛0")

    .when(df_jokbo_filter.taste.isNull() ,"")

    .alias("taste_review"))


df_jokbo_Awhen=df_jokbo_Twhen.select(col("*"), when(df_jokbo_filter.amount == "5","양2")

    .when(df_jokbo_filter.amount == "4","양1")
    
    .when(df_jokbo_filter.amount == "3","양0")

    .when(df_jokbo_filter.amount == "2","양0")

    .when(df_jokbo_filter.amount == "1","양0")

    .when(df_jokbo_filter.amount.isNull() ,"")

    .alias("amount_review"))

df_jokbo_final_when=df_jokbo_Awhen.select(col("*"), when(df_jokbo_filter.delivery == "5","배달2")

    .when(df_jokbo_filter.delivery == "4","배달1")
    
    .when(df_jokbo_filter.delivery == "3","배달0")

    .when(df_jokbo_filter.delivery == "2","배달0")

    .when(df_jokbo_filter.delivery == "1","배달0")

    .when(df_jokbo_filter.delivery.isNull() ,"")

    .alias("delivery_review"))


df_bunsik_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_cafe_dessert_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_chicken_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_hansik_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_ilsik_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_joongsik_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_pizza_final_when.na.replace(['"', '\n'], ['', ''], 'review')
df_jokbo_final_when.na.replace(['"', '\n'], ['', ''], 'review')


### 분식
df_bunsik_final_when.createOrReplaceTempView("review")

df_bunsik_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM review")
df_bunsik_review.show(10,truncate=False)

### 카페/디저트
df_cafe_dessert_final_when.createOrReplaceTempView("cafe_dessert_review")

df_cafe_dessert_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM cafe_dessert_review")
df_cafe_dessert_review.show(10,truncate=False)

### 치킨
df_chicken_final_when.createOrReplaceTempView("chicken_review")

df_chicken_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM chicken_review")
df_chicken_review.show(10,truncate=False)


### 한식
df_hansik_final_when.createOrReplaceTempView("hansik_review")

df_hansik_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM hansik_review")
df_hansik_review.show(10,truncate=False)


### 일식
df_ilsik_final_when.createOrReplaceTempView("ilsik_review")

df_ilsik_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM ilsik_review")
df_ilsik_review.show(10,truncate=False)


### 중식
df_joongsik_final_when.createOrReplaceTempView("joongsik_review")

df_joongsik_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM joongsik_review")
df_joongsik_review.show(10,truncate=False)


### 피자
df_pizza_final_when.createOrReplaceTempView("pizza_review")

df_pizza_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM pizza_review")
df_pizza_review.show(10,truncate=False)


### 족발보쌈
df_jokbo_final_when.createOrReplaceTempView("jokbo_review")

df_jokbo_review = spark.sql("SELECT  \
    CONCAT(taste_review, ' / ', amount_review, ' / ', delivery_review, ' / ', review) \
    AS new_review \
FROM jokbo_review")
df_jokbo_review.show(10,truncate=False)


df_bunsik = df_bunsik_review.na.drop('all')
df_cafe_dessert = df_cafe_dessert_review.na.drop('all')
df_chicken = df_chicken_review.na.drop('all')
df_hansik = df_hansik_review.na.drop('all')
df_ilsik = df_ilsik_review.na.drop('all')
df_joongsik = df_joongsik_review.na.drop('all')
df_pizza = df_pizza_review.na.drop('all')
df_jokbo = df_jokbo_review.na.drop('all')

df_bunsik = df_bunsik.distinct()
df_cafe_dessert = df_bunsik.distinct()
df_chicken = df_bunsik.distinct()
df_hansik = df_bunsik.distinct()
df_ilsik = df_bunsik.distinct()
df_joongsik = df_bunsik.distinct()
df_pizza = df_bunsik.distinct()
df_jokbo = df_bunsik.distinct()


df_bunsik.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_bunsik_new.csv")
df_cafe_dessert.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_cafe_dessert_new.csv")
df_chicken.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_chicken_new.csv")
df_hansik.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_hansik_new.csv")
df_ilsik.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_ilsik_new.csv")
df_joongsik.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_joongsik_new.csv")
df_pizza.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_pizza_new.csv")
df_jokbo.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("hdfs://hadoop-name:9000/input/df_jokbo_new.csv")
