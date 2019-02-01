from sys import argv
from re import match
from collections import defaultdict
import csv

# time: 0
# total_txn: 1
# total_tps: 2
# avg_latency: 7
# total_stock_level_txn: 8
# total_delivery_txn: 9
# total_order_status_txn: 10
# total_payment_txn: 11
# total_new_order_txn: 12

def load_csv_reader(file_handler):
    for line in file_handler:
        if line.startswith("complete"):
            break
    return csv.reader(fh)

def extract_time(record):
    return int(record[0])//1000

def extract_total_throughput(record):
    return (
        extract_time(record),
        float(record[2])*60
        )

def extract_avg_latency(record):
    return (
        extract_time(record),
        float(record[7])
        )

def extract_stock_level_throughput(record, prev_record):
    return (
        extract_time(record),
        (int(record[8]) - int(prev_record[8]))*6
        )

def extract_delivery_throughput(record, prev_record):
    return (
        extract_time(record),
        (int(record[9]) - int(prev_record[9]))*6
        )

def extract_order_status_throughput(record, prev_record):
    return (
        extract_time(record),
        (int(record[10]) - int(prev_record[10]))*6
        )

def extract_payment_throughput(record, prev_record):
    return (
        extract_time(record),
        (int(record[11]) - int(prev_record[11]))*6
        )

def extract_new_order_throughput(record, prev_record):
    return (
        extract_time(record),
        (int(record[12]) - int(prev_record[12]))*6
        )

def extract_csv_reports(reader):
    """
    return dict which contain all reports from inout csv reader
    """
    result = defaultdict(list)
    # prev_row = [0]*14
    prev_row = reader.__next__()
    for row in reader:
        if row[0].startswith("=="):
            break
        result["total_throughput"].append(extract_total_throughput(row))
        result["avg_latency_per_time"].append(extract_avg_latency(row))
        result["stock_level_throughput"].append(extract_stock_level_throughput(row, prev_row))
        result["delivery_throughput"].append(extract_delivery_throughput(row, prev_row))
        result["order_status_throughput"].append(extract_order_status_throughput(row, prev_row))
        result["payment_throughput"].append(extract_payment_throughput(row, prev_row))
        result["new_order_throughput"].append(extract_new_order_throughput(row, prev_row))
        prev_row = row
    return result

def extract_loading_time(file_handler):
    start = 0
    for line in file_handler:
        if line.startswith("start Loading"):
            start = int(line.split(":")[-1])
        if line.startswith("load ends"):
            return {"load_time": str(int(line.split(":")[-1]) - start)}


def extract_rersponse_time_report(fh):
    latency_avg = ""
    for line in fh:
        if line.startswith(" - Average"):
            latency_avg = line.split()[-2]
            break
    latency_results = []
    for line in fh:
        latency_data = match(" -   Latency   (\d*)ms -  (\d*)ms = (\d*)", line)
        if latency_data is None:
            break
        latency_results.append((
            (int(latency_data.group(1)) + int(latency_data.group(2)))/2,
            int(latency_data.group(3))
        ))
    return {"latency_per_rt": latency_results,
            "latency_avg": latency_avg,
            "timeout_txn": line.split()[-1]}

def transaction_time_report(fh):
    for _ in range(3):
        fh.readline()
    stock_level_splited = fh.readline().split()
    delivey_splited = fh.readline().split()
    order_status_splited = fh.readline().split()
    payment_splited = fh.readline().split()
    new_order_splited = fh.readline().split()
    return {
        "stock_level_total_txn": stock_level_splited[2], "stock_level_tmp": stock_level_splited[6],
        "delivey_total_txn": delivey_splited[1], "delivey_tmp": delivey_splited[5],
        "order_status_total_txn": order_status_splited[2], "order_status_tmp": order_status_splited[6],
        "payment_total_txn": payment_splited[1], "payment_tmp": payment_splited[5],
        "new_order_total_txn": new_order_splited[2], "new_order_tmp": new_order_splited[6],
    }

def get_string_throughput_result(result):
    """
    summerize result (getting avg from second datum)
    """
    if isinstance(result, str):
        return result
    result_string = ""
    for record in result:
        # result_string += " ("+str(record[0])+" , "+str(record[1])+")"
        result_string += str(record)+" "
    return result_string

report_file_path = argv[1]
report = {}
with open(report_file_path) as fh:
    report.update(extract_loading_time(fh))
    reader = load_csv_reader(fh)
    report.update(extract_csv_reports(reader))
    report.update(transaction_time_report(fh))
    report.update(extract_rersponse_time_report(fh))

# generate result tex from template by replacing placeholders
with open("tpcc_report_template.tex") as fh:
    template = fh.read()
    for k, v in report.items():
        template = template.replace("{"+k+"}", get_string_throughput_result(v))
print(template)