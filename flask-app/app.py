from flask import Flask, jsonify
from pyspark.sql import SparkSession

app = Flask(__name__)

# Create a Spark session that connects to the Spark master
def get_spark_session():
    return SparkSession.builder \
        .appName("FlaskSparkApp") \
        .master("spark://spark-master:7077") \
        .getOrCreate()

@app.route('/')
def home():
    return "Flask API connected to Spark cluster!"

@app.route('/submit-job')
def submit_job():
    # Get the Spark session
    spark = get_spark_session()

    # Example PySpark job (Pi calculation)
    pi_estimate = spark.sparkContext.parallelize(range(0, 1000000)) \
        .map(lambda x: 4.0 / (1 + ((x / 1000000.0) ** 2))) \
        .reduce(lambda x, y: x + y) / 1000000

    return jsonify({"Pi Estimate": pi_estimate})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
