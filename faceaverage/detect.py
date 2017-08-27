# -*- coding:utf-8 -*-
import  requests
import os
import json
import mimetypes
from model import FemaleFace, Session
key = ''
secret = ''

api =r'https://api-cn.faceplusplus.com/facepp/v3'

url = '{}/detect?api_key={}&api_secret={}&return_landmark=1'.format(api, key, secret)

class Point(object):
    """二维平面点"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_dect(filepath):

    files = {'image_file': (os.path.basename(filepath),
                            open(filepath, 'rb'),
                            mimetypes.guess_type(filepath)[0]),}
    response = requests.post(url, files=files)
    info = response.json()
    print info

def detect_face(record_id, filepath):
    """
    调用face++ API检测人脸并写入数据库
    :param record_id: (int) 数据库记录
    :param file_path: (string) 图像路径
    :return: (int) 是否检测到人脸（默认选第一个）
    """
    files = {'image_file': (os.path.basename(filepath),
                            open(filepath, 'rb'),
                            mimetypes.guess_type(filepath)[0]),}
    response = requests.post(url, files=files)
    info = response.json()
    FemaleFace.update(record_id, info=json.dumps(info))

    faces = info.get('faces', [])
    print faces
    if not faces:
        return 0
    landmark = faces[0].get('landmark',[])
    print landmark
    if not landmark:
        return 0

    FemaleFace.update(record_id, landmark=json.dumps(landmark))
    return 1

if __name__ == '__main__':
    session = Session()
    pretty_faces = session.query(FemaleFace).filter(FemaleFace.label == 2)
    for face in pretty_faces:
        file_path = r'e:\face\{}'.format(face.filename)
        print file_path
        detect_face(face.id, file_path)
