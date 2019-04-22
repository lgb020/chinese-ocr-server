#-*- coding:utf-8 -*-
# __auther__:wgshun

import os
import time
import shutil
import numpy as np
from PIL import Image
import ocr
import json

from flask import Flask,request
import os,sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/Rec_Interface/<string:task_id>',methods=['POST'])
def rec_img(task_id):
    if task_id == "file":
        img_file = request.form['image_path']
		if os.path.exists(img_file):
			image = np.array(Image.open(img_file).convert('RGB'))
			t = time.time()
			result, image_framed = ocr.model(image)
			print("Mission complete, it took {:.3f}s".format(time.time() - t))
			re_dict = {}
			for key in result:
				re_dict[result[key][1]] = list(result[key][0])
			return json.dumps(re_dict)
		else:
			return 'Image does not exist!'

    #elif task_id == "dir":
    #    for root, dirs, files in os.walk(request.form['image_path']):
    #        for fil in files:
    #            image = np.array(Image.open(os.path.join(root, fil)).convert('RGB'))
    #            t = time.time()
    #            result, image_framed = ocr.model(image)
    #            print("Mission complete, it took {:.3f}s".format(time.time() - t))
    #            for key in result:
    #                pass
    #     return "over"
    else:
        return 'warn'

    
if __name__ == "__main__":
    app.run(
        host = '127.0.0.1',
        port = 5000,
        debug = True
        )

