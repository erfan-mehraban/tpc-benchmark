#!/bin/bash
# first arg: report path
# second arg: tex path
for i in `seq 1 22`; do
python3 analyse_dstat.py $1/postgre-reports/$i.dstat > $2/postgres/$i.tex
python3 analyse_dstat.py $1/spark-parquet-reports/$i.dstat > $2/spark_parquet/$i.tex
python3 analyse_dstat.py $1/spark-orc-reports/$i.dstat > $2/spark_orc/$i.tex
python3 analyse_dstat.py $1/spark-avro-reports/$i.dstat > $2/spark_avro/$i.tex
done
