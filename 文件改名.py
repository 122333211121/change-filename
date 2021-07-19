import os
import exifread
 
def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'# 拍摄日期的标识
    filedir = open(filename, 'rb')
    tags = exifread.process_file(filedir)
    filedir.close()        

    # 如果是原图，则会有拍摄日期，就提取拍摄日期并以此重命名
    if FIELD in tags:
        i = 1
        new_name = str(tags[FIELD]).split(' ')[0] + '_' + str(i) + os.path.splitext(filename)[1]
        new_name = new_name.replace(':', ' ')
        while os.path.exists(new_name):    
            i += 1
            new_name = str(tags[FIELD]).split(' ')[0] + '_' + str(i) + os.path.splitext(filename)[1]
            new_name = new_name.replace(':', ' ')
        os.rename(filename, new_name)
    # 如果不是原图，则找不到拍摄日期，则以特殊格式重命名
    else:
        x = 1
        y = '00000'
        newname = y[0:len(y)-len(str(x))] + str(x) + '.jpg'
        while os.path.exists(newname):
            x += 1
            newname = y[0:len(y)-len(str(x))] + str(x) + '.jpg'
        os.rename(filename, newname)

# 判断文件是否为图片        
def is_img(filename):
   ext = os.path.splitext(filename)[1]
   if ext in ['.jpg', '.png', '.jpeg', '.bmp']:
      return True
   else:
      return False

for filename in os.listdir('.'):
    if is_img(filename):
        getExif(filename)
