# Ransomware written in Python

> Disclaimer: This tool is for education purpose only. I made this just for experimenting and testing and learning purpose. I am not responsible for any misuse of this tool. Be careful what you do.

<hr>

### Instructions

You need [Python3](http://python.org/) (ofcourse!)

#### Installing

```sh
$ pip install cryptography pyinstaller
```

once this is done! you can change in `__main__` for `sys_root` or `local_root`

- <b>sys_root</b>: this config uses `expanduser("~")` means it will get the user's root eg. `/home/username` in Linux or `C:\Users\MyName` in Windows. It will start encrypting given extensions in `file_ext_target` (referenced in Ransomware Class `__init__` method)

- <b>local_root</b>: this config uses `"."` (Referenced as current directory). This means wherever the file is placed, It will start encrypting from that directory into its sub directories. (eg. if file is executed from `E:\Games` then it will start encrypting files and folders inside `Games` dir)  
    
    - <b>file_ext_target</b>: A list targetting the given extension files will be encrypted. (eg. you can pass as `[ "txt", "pdf", "mp3", ...]`)

## Usage

There are several arguments to be used for execution.

|  Argument  | Priority | Description | 
|:------------:|:--------:|-----------|
| `--action` | Required | Action takes one parameter either `encrypt` or `decrypt` |
| `--keyfile` | Optional | It is optional with `encrypt` action if you don't have your own key. It will generate by itself and save as `mykey.key` file. <br> With `decrypt` it is **Required** without key your data won't be decrypted.

- Here is simple example for `encryption` and `decryption`

#### Encrypting
```sh
$ python main.py --action encrypt
```
OR

```sh
$ python main.py --action encrypt --keyfile "./secret.key"
```

#### Decrypting

```sh
$ python main.py --action decrypt --keyfile "./secret.key"
```
**NOTE**: Make sure you use correct key file for its belonging encrypted files. Otherwise if they secret key wont match then your data won't be decrypted correctly.

## Keyfile

- **NOTE:** Make sure you save your key file at safe place after you encrypt your data. Take a note that the keyfile will be generated as `mykey.key` where the program is executed.

## Compiling

- You can use `pyinstaller` or any other favourite bundler/compiler to convert it in executable.

```sh
$ pyinstaller --onefile main.py -w
```

- <h3>This will create an executable in <b>dist/</b> folder from there it will work on any machine without python installed just by running from commandline.</h3>
> **NOTE**: all the execution method will remain same just `main.exe` will be replaced instead `python main.py`. Rest of the methods will follow same as above mentioned.

### License
- No licnese. Feel free to use by taking care of **Disclaimer**.

Initiated and made by &copy; Swapnil Soni.

