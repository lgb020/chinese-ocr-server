#-*- coding:utf-8 -*-
import os
import ocr
import time
import shutil
import numpy as np
from PIL import Image
image_files = './test_result'
import sys

reload(sys)

sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    result_files = './result'

    for root, dirs, files in os.walk(image_files):
	for fil in files:
	    output_dir = os.path.join(result_files, root.split('/')[-1])
	    if os.path.exists(output_dir):
		pass
	    else:
		os.makedirs(output_dir)
            image = np.array(Image.open(os.path.join(root, fil)).convert('RGB'))
            t = time.time()
            result, image_framed = ocr.model(image)
	    new_img = fil.split('.')[0] + '_o.jpg'
            output_file = os.path.join(output_dir, new_img)
            Image.fromarray(image_framed).save(output_file)
            print("Mission complete, it took {:.3f}s".format(time.time() - t))
            print("\nRecognition Result:\n")
	    with open(os.path.join(output_dir, fil.split('.')[0] + '_o.txt'), 'w') as fi:
                for key in result:
		    #print(result[key][1]+'\n')
                    #fi.write(str(result[key][0])+'\n')
		    fi.write(str(result[key][1])+'\n')
	    fi.close()

