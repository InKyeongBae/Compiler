# Lexical Analyzer & Sysntax Analyzer : Team Project for Compiler Class
>__* All screen capture and detail of lexical&syntax_analyzer and more detail in__ *" Team2_lexical(syntax)_analyzer_report.pdf "*

>2021-1 Compiler class in CAU Team2


## Team Member
|Name|
|---|
|배인경|
|좌민주|

## Brief project description
1) Lexical analyzer
- directory name : mid
- lexical analyzer for a simplified Java programming language
- Based on specification(by class note), define tokens (e.g., token names) for a simplified Java language, make regular expressions which describe the patterns of the tokens, construct a NFA for the regular expressions, translate the NFA into a DFA, especially in the form of a table, 
and implement a program which does a lexical analysis (recognizing tokens).

2) Syntax analyzer
- directory name : final
- a bottom-up syntax analyzer (a.k.a., parser) for a simplified Java programming language
- Implement a SLR parsing program for the simplified Java programming language by using the constructed table.

## How to Compile
### 1 Lexical Analyzer(Run on Linux or Unix-like OS)__

1. Open the Project directory(mid) that you want to execute.
2. On a command line, your analyzer must run with the following command.
```
$ python3 lexical_analyzer.py <input_file_name>.java
```
3. __Input__: A program written in a simplified Java programming language
4. __Output__: <input_file_name>.out

### 2 Syntax Analyzer(Run on Linux or Unix-like OS)__

1. Open the Project directory(final) that you want to execute.
2. On a command line, your analyzer must run with the following command.
```
$ python3 lexical_analyzer.py <input_file_name>.java
```
```
$ python3 syntax_analyzer.py <input_file_name>.out
```
3. __Input__: An output of your lexical analyzer program
4. __Output__: just an acceptance message;(If an output is “reject”) please make an error report which explains why and where the error occurred (e.g., line number) 

