# 小猿口算比大小图片识别
## Requirements:
### Blue Stacks 5:
1. 下载并安装[链接](https://www.bluestacks.com/bluestacks-5.html)
2. 绘制大于号小于号等号的脚本并绑定按键，大于号绑定`.`，小于号绑定`,`，等号绑定`/`
### Tesseract:
1. 下载Tesseract [链接](https://github.com/UB-Mannheim/tesseract/wiki)
2. 安装之后将`Tesseract-OCR`文件夹加入到path中
3. 打开cmd输入`tesseract -v`来检测是否安装成功

### Python:
1. Python版本>=3.9
2. `pip install opencv-python numpy pyautogui pytesseract keyboard`

## 运行之前:
修改`region1`和`region2`变量，`region1`代表左面的数字的区域,`region2`代表右面数字的区域。`region1/2`中四个值分别为起始点x轴坐标，起始点y轴坐标，取景范围宽度，取景范围高度。可以使用微信截图来测量
