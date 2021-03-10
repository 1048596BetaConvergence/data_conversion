import os
import urllib.request
import json
import subprocess
import sys

def run(cmd):
    proc = subprocess.Popen([sys.executable] + cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    return stdout, stderr

def test_base_case():
    input_dir = "cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json".split()
    output, err = run(input_dir)
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.dumps(json.load(result)["result_base"]) == output.decode("UTF-8").replace("'", "\"").replace("\n", "").replace("\r", "")

def test_repo_case():
    input_dir = "cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --repo=github.com/myorg/c".split()
    output, err = run(input_dir)
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.dumps(json.load(result)["result_repo"]) == output.decode("UTF-8").replace("'", "\"").replace("\n", "").replace("\r", "")

def test_class_case():
    input_dir = "cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --class=injection".split()
    output, err = run(input_dir)
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.dumps(json.load(result)["result_class"]) == output.decode("UTF-8").replace("'", "\"").replace("\n", "").replace("\r", "")

def test_type_case():
    input_dir = "cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --type=weak-crypto-2".split()
    output, err = run(input_dir)
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.dumps(json.load(result)["result_type"]) == output.decode("UTF-8").replace("'", "\"").replace("\n", "").replace("\r", "")

def test_command_fail():
    input_dir = "cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --type=weak-crypto-2".split()
    output, err = run(input_dir)
    with urllib.request.urlopen("https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample_result.json") as result:
        assert json.load(result)["result_error"] == err.decode("UTF-8")