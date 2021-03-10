# Test Running
The test that was designed for this program is using Pytest.

First run the following command to install pytest:
```pip install pytest```

Then simply run the following command to execute test cases:
```pytest test.py```


# Manually running the program
The program can be ran manually by directly calling the program:
```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json```

This will produce a complete list of all data converted:
```
[
 {"repository": "github.com/myorg/a", "file": "file.py", "startLineNumber": "1", "endLineNumber": "2", "type": "sql-injection", "class": "injection"}, 
 {"repository": "githu.com/myorg/a", "file": "file.py", "startLineNumber": "5", "endLineNumber": "10", "type": "command-injection", "class": "injection"}, 
 {"repository": "github.com/myorg/a", "file": "file.py", "startLineNumber": "1", "endLineNumber": "2", "type": "weak-crypto", "class": "bad-crypto"}, 
 {"repository": "github.com/myorg/c", "file": "file.py", "startLineNumber": "1", "endLineNumber": "5", "type": "weak-crypto-2", "class": "bad-crypto"}
]
```

A couple of case is handle directly at the input level where the program will directly exit with error:
```python cli.py```
error: "sourceUrl not found from command"

```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json```
error: "duplicate command --sourceUrl"

The above error applies for other command --class, --type --repo as well.

```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --magic=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json```
error: "Unrecognized command: magic"

```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json=```
error: "Unrecognized command format --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json=" (since there is multiple equal signs)


# Multiple commands
The program also accept multiple command such as:
```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --repo=github.com/myorg/c --class=injection```

which will produce result A where A belong both to the commands:
```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --repo=github.com/myorg/c```
AND
```python cli.py --sourceUrl=https://raw.githubusercontent.com/1048596BetaConvergence/data_conversion/master/test/sample.json --class=injection```
