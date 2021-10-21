## 功能

pdf转长图，支持设置每张长图包含多少页pdf

环境：python3.6+

## 安装

### macos

1. 安装pymupdf，将每页pdf转为图片

   ```
   python3 -m pip install --upgrade pip --user
   python3 -m pip install --upgrade pymupdf --user
   ```

2. 安装Pillow，用于图像拼接

   ```
   python3 -m pip install --upgrade Pillow --user
   ```

## 使用

参数说明：

```
python3 pdf2png.py -h #查看帮助
usage: pdf2png.py [-h] [-f FILEPATH] [-u UNIT]
optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        pdf文件
  -u UNIT, --unit UNIT  每张图所包含的页数
```

脚本使用：

```
python3 pdf2png.py -f raft.pdf
```

输出结果在当前目录 output文件夹下

