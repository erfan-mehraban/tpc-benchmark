#!/bin/bash
# first arg: report path

echo med/1
python3 analyse_oltpbench.py $1/med/1/ > $2/med/1_txn.tex
echo med/2
python3 analyse_oltpbench.py $1/med/2/ > $2/med/2_txn.tex
echo med/3
python3 analyse_oltpbench.py $1/med/3/ > $2/med/3_txn.tex
echo med/5
python3 analyse_oltpbench.py $1/med/5/ > $2/med/5_txn.tex
echo med/10
python3 analyse_oltpbench.py $1/med/10/ > $2/med/10_txn.tex
echo med/100
python3 analyse_oltpbench.py $1/med/100/ > $2/med/100_txn.tex
echo read/1
python3 analyse_oltpbench.py $1/read/1/ > $2/read/1_txn.tex
echo read/2
python3 analyse_oltpbench.py $1/read/2/ > $2/read/2_txn.tex
echo read/3
python3 analyse_oltpbench.py $1/read/3/ > $2/read/3_txn.tex
echo read/5
python3 analyse_oltpbench.py $1/read/5/ > $2/read/5_txn.tex
echo read/10
python3 analyse_oltpbench.py $1/read/10/ > $2/read/10_txn.tex
echo read/100
python3 analyse_oltpbench.py $1/read/100/ > $2/read/100_txn.tex
echo write/1
python3 analyse_oltpbench.py $1/write/1/ > $2/write/1_txn.tex
echo write/2
python3 analyse_oltpbench.py $1/write/2/ > $2/write/2_txn.tex
echo write/3
python3 analyse_oltpbench.py $1/write/3/ > $2/write/3_txn.tex
echo write/5
python3 analyse_oltpbench.py $1/write/5/ > $2/write/5_txn.tex
echo write/10
python3 analyse_oltpbench.py $1/write/10/ > $2/write/10_txn.tex
echo write/100
python3 analyse_oltpbench.py $1/write/100/ > $2/write/100_txn.tex