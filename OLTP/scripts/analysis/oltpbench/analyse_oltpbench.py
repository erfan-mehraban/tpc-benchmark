from sys import argv, stderr
from re import match
from collections import defaultdict
import csv

# csv:
# 0 Transaction Type Index
    # 1,NewOrder
    # 2,Payment
    # 3,OrderStatus
    # 4,Delivery
    # 5,StockLevel
# 1 Transaction Name
# 2 Start Time (microseconds)
# 3 Latency (microseconds)
# 4 Worker Id (start number)
# 5 Phase Id (index in config file)

latency_scale = 30
throughput_scale = 15
time_scale = 10
def extract_csv_reports(path):
    with open(path) as fh:
        fh.readline()
        result = defaultdict(int)
        rt_txn = defaultdict(int)
        total_txn_count = 0
        latency_sum = 0
        latencies = []
        reader = csv.reader(fh)
        for record in reader:
            record_latency = int(record[3])
            total_txn_count += 1
            latency_sum += record_latency
            latencies.append(record_latency)
            if record_latency>100000:
                result["timeout_txn"] += 1
            else:
                # print(record_latency, file=stderr)
                rt_txn[record_latency//latency_scale*latency_scale] += 1
                if record[0]=='1':
                    result["new_order_total_txn"] += 1
                    result["new_order_tmp"] += record_latency
                elif record[0]=='2':
                    result["payment_total_txn"] += 1
                    result["payment_tmp"] += record_latency
                elif record[0]=='3':
                    result["order_status_total_txn"] += 1
                    result["order_status_tmp"] += record_latency
                elif record[0]=='4':
                    result["delivey_total_txn"] += 1
                    result["delivey_tmp"] += record_latency
                elif record[0]=='5':
                    result["stock_level_total_txn"] += 1
                    result["stock_level_tmp"] += record_latency

        result["latency_per_rt"] = list(rt_txn.items())
        result["latency_per_rt"].sort(key=lambda x:x[0])
        result["latency_avg"] = (latency_sum//total_txn_count)//latency_scale*latency_scale
        latencies.sort()
        result["latency_90th"] = latencies[int(0.9*total_txn_count)]//latency_scale*latency_scale
        result["new_order_tmp"] //= result["new_order_total_txn"]
        result["payment_tmp"] //= result["payment_total_txn"]
        result["order_status_tmp"] //= result["order_status_total_txn"]
        result["delivey_tmp"] //= result["delivey_total_txn"]
        result["stock_level_tmp"] //= result["stock_level_total_txn"]
        return result

def get_string(result):
    if not isinstance(result, list):
        return str(result)
    result_string = ""
    for record in result:
        result_string += str(record)+" "
    return result_string

def extract_times(path):
    with open(path) as f:
        for line in f:
            if line.startswith("start load"):
                start = float(line.split(":")[-1])
            if line.startswith("end load"):
                return {"load_time": int( (float(line.split(":")[-1]) - start)*1000 )}

# res:
# 0 time(sec)
# 1 throughput(req/sec)
# 2 avg_lat(ms)
# 3 min_lat(ms)
# 4 25th_lat(ms)
# 5 median_lat(ms)
# 6 75th_lat(ms)
# 7 90th_lat(ms)
# 8 95th_lat(ms)
# 9 99th_lat(ms)
# 10 max_lat(ms)
# 11 tp (req/s) scaled
        
def extract_res_reports(path):
    with open(path) as fh:
        fh.readline()
        reader = csv.reader(fh)
        result = defaultdict(list)
        th_rt = defaultdict(int)
        for record in reader:
            for _ in range(time_scale):
                fh.readline()
            throughput = float(record[1])*60 //throughput_scale*throughput_scale
            time = int(record[0])
            result["total_throughput"].append( (time, throughput) )
            result["avg_latency_per_time"].append( (time, int(float(record[5]))) )
            th_rt[throughput] = int(float(record[7]))
        result["resonsetime_per_throughput"] = list(th_rt.items())
        result["resonsetime_per_throughput"].sort(key=lambda x:x[0])
        result["throughput_50th"] = result["resonsetime_per_throughput"][len(th_rt)//2][0]
        result["throughput_80th"] = result["resonsetime_per_throughput"][int(len(th_rt)*0.8)][0]
        result["throughput_100th"] = result["resonsetime_per_throughput"][len(th_rt)-1][0]
        
        return result


report_file_dir = argv[1]
query_num = report_file_dir.split("/")[-1]
report = {}
report.update(extract_csv_reports(report_file_dir+"/oltpbench.csv"))
report.update(extract_res_reports(report_file_dir+"/oltpbench.res"))
report.update(extract_times(report_file_dir+"/time.out"))

# generate result tex from template by replacing placeholders
with open("oltpbench_report_template.tex") as fh:
    template = fh.read()
    for k, v in report.items():
        template = template.replace("{"+k+"}", get_string(v))
print(template.replace("{Q}", "Query"+str(query_num).zfill(2)))