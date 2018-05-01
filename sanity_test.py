from __future__ import print_function
import sys
from base64 import b64decode

try:
    import gluoncv as gcv
    net = gcv.model_zoo.get_model('ssd_512_resnet50_v1_voc', pretrained_base=False)
    print('Test succeeded')
except:
    import traceback
    print('Test failed')
    traceback.print_exc()
    sys.exit(1)
