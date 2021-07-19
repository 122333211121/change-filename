import os
import exifread
 
def getExif(filename):
    FIELD = 'EXIF DateTimeOriginal'# 拍摄日期的标识
    filedir = open(filename, 'rb')
    tags = exifread.process_file(filedir)
    filedir.close()
    if FIELD in tags:
        i = 1
        new_name = str(tags[FIELD]).split(' ')[0] + '_' + str(i) + os.path.splitext(filename)[1]
        new_name = new_name.replace(':', ' ')
        while os.path.exists(new_name):    
            i += 1
            new_name = str(tags[FIELD]).split(' ')[0] + '_' + str(i) + os.path.splitext(filename)[1]
            new_name = new_name.replace(':', ' ')
        os.rename(filename, new_name)
    else:
        print('No {} found'.format(FIELD))
 
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        getExif(filename)
