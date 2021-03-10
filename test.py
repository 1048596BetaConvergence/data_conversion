import os
import urllib.request
import json
import subprocess
import sys

def run(cmd):
    proc = subprocess.Popen([sys.executable, cmd],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return stdout, stderr

def base_case_test():
    output, err = run("py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json")
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_base"] == output

def repo_case_test():
    output, err = run("py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --repo=github.com/myorg/c")
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_repo"] == output

def class_case_test():
    output, err = run("py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --class=injection")
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_class"] == output

def type_case_test():
    output, err = run("py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --type=weak-crypto-2")
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_type"] == output

def command_fail_test():
    output, err = run("py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --sourceUrl=https://raw.github.com --type=weak-crypto-2")
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_error"] == output