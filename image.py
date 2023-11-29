from PIL import Image, ImageDraw, ImageEnhance, ImageOps


class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def save(self, filename):
        self.image.save(filename)

    def erase_area(self, left_percent, top_percent, right_percent, bottom_percent):
        # 获取图像的实际宽度和高度
        img_width, img_height = self.image.size
        # 将百分比转换为像素值
        left = int(left_percent * img_width)
        top = int(top_percent * img_height)
        right = int(right_percent * img_width)
        bottom = int(bottom_percent * img_height)
        # 创建一个绘图对象
        draw = ImageDraw.Draw(self.image)
        # 定义涂抹区域的坐标 (左, 上, 右, 下)
        erase_coords = (left, top, right, bottom)
        # 绘制一个矩形来覆盖该区域
        draw.rectangle(erase_coords, fill='black')

    def preprocess_for_ocr(self, left_percent, top_percent, right_percent, bottom_percent):
        img_width, img_height = self.image.size
        left = int(left_percent * img_width)
        top = int(top_percent * img_height)
        right = int(right_percent * img_width)
        bottom = int(bottom_percent * img_height)
        self.image = self.image.crop((left, top, right, bottom))
