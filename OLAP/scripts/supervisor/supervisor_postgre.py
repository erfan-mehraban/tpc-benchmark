from subprocess import Popen, DEVNULL
from time import time
dstat_proc = None
query_proc = None
def run_dstat(log_path):
    global dstat_proc
    if dstat_proc is not None:
        dstat_proc.kill()
    dstat_proc = Popen([
            "dstat",
            "-lcmdrsyTt",
            "--full",
            "--output",
            log_path
        ],
        stdout=DEVNULL)

def run_query(file_path):
    global query_proc
    if query_proc is not None:
        query_proc.kill()
    with open(file_path) as query_handler:
        query_proc = Popen([
            "psql",
            "-d",
            "tpch",
        ],stdin=query_handler, stdout=DEVNULL)
        query_proc.wait()

begin_query_num = 4
end_query_num = 6
query_folder = "/root/q/"
report_folder = "/root/reports/"

for i in range(begin_query_num, end_query_num+1):
    print("query begin at:", time())
    print("run dstat for", i)
    report_path = report_folder + str(i) + ".dstat"
    run_dstat(report_path)

    print("run query", i)
    query_path = query_folder + str(i) + ".sql"
    run_query(query_path)
    print("query ends at:", time())

dstat_proc.kill()
query_proc.kill()