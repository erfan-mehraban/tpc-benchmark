#!/bin/bash
# first arg: report path
# second arg: tex path

# for voltdb
# python3 analyse_dstat.py $1/med/1.dstat medium > $2/med/1_dstat.tex
# python3 analyse_dstat.py $1/med/2.dstat medium > $2/med/2_dstat.tex
# python3 analyse_dstat.py $1/med/3.dstat medium > $2/med/3_dstat.tex
# python3 analyse_dstat.py $1/med/5.dstat medium > $2/med/5_dstat.tex
# python3 analyse_dstat.py $1/med/10.dstat medium > $2/med/10_dstat.tex
# python3 analyse_dstat.py $1/med/100.dstat medium > $2/med/100_dstat.tex

# python3 analyse_dstat.py $1/read/1.dstat high\\_read > $2/read/1_dstat.tex
# python3 analyse_dstat.py $1/read/2.dstat high\\_read > $2/read/2_dstat.tex
# python3 analyse_dstat.py $1/read/3.dstat high\\_read > $2/read/3_dstat.tex
# python3 analyse_dstat.py $1/read/5.dstat high\\_read > $2/read/5_dstat.tex
# python3 analyse_dstat.py $1/read/10.dstat high\\_read > $2/read/10_dstat.tex
# python3 analyse_dstat.py $1/read/100.dstat high\\_read > $2/read/100_dstat.tex

# python3 analyse_dstat.py $1/write/1.dstat high\\_write > $2/write/1_dstat.tex
# python3 analyse_dstat.py $1/write/2.dstat high\\_write > $2/write/2_dstat.tex
# python3 analyse_dstat.py $1/write/3.dstat high\\_write > $2/write/3_dstat.tex
# python3 analyse_dstat.py $1/write/5.dstat high\\_write > $2/write/5_dstat.tex
# python3 analyse_dstat.py $1/write/10.dstat high\\_write > $2/write/10_dstat.tex
# python3 analyse_dstat.py $1/write/100.dstat high\\_write > $2/write/100_dstat.tex

# for postgres
# python3 analyse_dstat.py $1/med/1/dstat.out medium > $2/med/1_dstat.tex
# python3 analyse_dstat.py $1/med/2/dstat.out medium > $2/med/2_dstat.tex
# python3 analyse_dstat.py $1/med/3/dstat.out medium > $2/med/3_dstat.tex
# python3 analyse_dstat.py $1/med/5/dstat.out medium > $2/med/5_dstat.tex
# python3 analyse_dstat.py $1/med/10/dstat.out medium > $2/med/10_dstat.tex
# python3 analyse_dstat.py $1/med/100/dstat.out medium > $2/med/100_dstat.tex

# python3 analyse_dstat.py $1/read/1/dstat.out high\\_read > $2/read/1_dstat.tex
# python3 analyse_dstat.py $1/read/2/dstat.out high\\_read > $2/read/2_dstat.tex
# python3 analyse_dstat.py $1/read/3/dstat.out high\\_read > $2/read/3_dstat.tex
# python3 analyse_dstat.py $1/read/5/dstat.out high\\_read > $2/read/5_dstat.tex
# python3 analyse_dstat.py $1/read/10/dstat.out high\\_read > $2/read/10_dstat.tex
# python3 analyse_dstat.py $1/read/100/dstat.out high\\_read > $2/read/100_dstat.tex

# python3 analyse_dstat.py $1/write/1/dstat.out high\\_write > $2/write/1_dstat.tex
# python3 analyse_dstat.py $1/write/2/dstat.out high\\_write > $2/write/2_dstat.tex
# python3 analyse_dstat.py $1/write/3/dstat.out high\\_write > $2/write/3_dstat.tex
# python3 analyse_dstat.py $1/write/5/dstat.out high\\_write > $2/write/5_dstat.tex
# python3 analyse_dstat.py $1/write/10/dstat.out high\\_write > $2/write/10_dstat.tex
# python3 analyse_dstat.py $1/write/100/dstat.out high\\_write > $2/write/100_dstat.tex