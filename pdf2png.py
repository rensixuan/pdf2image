import fitz
import os, sys
from os import listdir
from PIL import Image
import argparse
import shutil

def pdf2image(filepath, image_path):
    tmp_path = "./tmp/"
    os.makedirs(tmp_path, exist_ok = True)
    doc = fitz.open(filepath)
    # 设置图像像素
    mat = fitz.Matrix(4, 4)
    for index in range(0, doc.pageCount):
        page = doc[index]
        pm = page.getPixmap(matrix=mat)
        pm.writePNG(tmp_path + str(index)+".jpg")
    return doc.pageCount

def mergeImage(filepath, output, page_num, page_count):
    tmp_path = "./tmp/"

    # 获取单幅图像尺寸
    t = Image.open(tmp_path + "0.jpg")
    width, height = t.size

    # pdf转出来的大小相同，不用重设尺寸
    # 创建空白画布
    result = Image.new(t.mode, (width, height * page_num))

    # 拼接图片
    (file_path,tmp_filename) = os.path.split(filepath)
    (filename,extension) = os.path.splitext(tmp_filename)
    for i in range(0, page_count):
        im = Image.open(tmp_path + str(i)+".jpg")
        result.paste(im, box=(0, i%page_num * height))
        if (i+1)%page_num == 0 and i >0:
            # 保存图片
            result.save(output + filename + str(int(i/page_num))+".jpg")
    if i<page_count:
        result = result.crop(box = (0,0,width,(page_count-i+1) * height))
        result.save(output + filename +str(int(i/page_num) + 1)+".jpg")

def main(filepath, output, page_num):
    page_count = pdf2image(filepath, output)
    mergeImage(filepath, output, page_num, page_count)

def argInit():
    parse = argparse.ArgumentParser()
    parse.add_argument("-f", "--filepath", help="pdf文件")
    parse.add_argument("-u", "--unit", help="每张图所包含的页数")
    args = parse.parse_args()
    page_num = 5
    filepath,output = "", "./output/"
    if args.filepath:
        filepath = args.filepath
    else:
        raise FError("filename empty")
    if args.unit:
        page_num = args.unit
    os.makedirs(output, exist_ok = True)
    return filepath, output, page_num

if __name__ == '__main__':
    filepath, output, page_num = argInit()
    main(filepath, output, page_num)
    shutil.rmtree("./tmp/")
