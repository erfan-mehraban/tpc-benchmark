import sys
from subprocess import Popen, DEVNULL, STDOUT
from time import time

dstat_proc = None
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

def run_test(dir_path):
    with open(dir_path+"/test.out", "w") as out_file_handler:
        test_proc = Popen([
            "bash",
            "oltpbenchmark",
            "-c", dir_path+"/config.xml",
            "-b","tpcc",
            "-d", dir_path,
            "--execute", "true", "-s", "1"
        ],stdout=out_file_handler, stderr=STDOUT)
        test_proc.wait()

def report_time(desc, fh):
    fh.write(desc+str(time())+"\n")

def drop(dir_path):
    with open(dir_path+"/drop.out", "w") as out_file_handler:
        test_proc = Popen([
            "bash",
            "oltpbenchmark",
            "-c", dir_path+"/config.xml",
            "-b","tpcc",
            "-d", dir_path,
            "--runscript", "drop.sql"
        ],stdout=out_file_handler, stderr=STDOUT)
        test_proc.wait()

def load(dir_path):
    with open(dir_path+"/load.out", "w") as out_file_handler:
        test_proc = Popen([
            "bash",
            "oltpbenchmark",
            "-c", dir_path+"/config.xml",
            "-b","tpcc",
            "-d", dir_path,
            "--create", "true", "--load", "true"
        ],stdout=out_file_handler, stderr=STDOUT)
        test_proc.wait()

report_folder = sys.argv[1]
for sf in ["1", "2", "3", "5", "10", "100"]:
    with open(report_folder+"/time.out", "w") as time_file_handler:
        print("sf:",sf)
        folder_path = report_folder+"/"+sf
        sys.stdout.flush()
        drop(folder_path)
        report_time("start load",time_file_handler)
        load(folder_path)
        report_time("end load",time_file_handler)
        run_dstat(folder_path+"/dstat.out")
        report_time("start test",time_file_handler)
        run_test(folder_path)
        report_time("end test",time_file_handler)
        dstat_proc.kill()