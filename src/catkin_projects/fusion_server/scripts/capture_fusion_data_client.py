#!/usr/bin/env python

import sys
import rospy
from fusion_server.srv import *

def capture_fusion_data_client(x):
    rospy.wait_for_service('capture_fusion_data')
    try:
        capture_fusion_data = rospy.ServiceProxy('capture_fusion_data', CaptureFusionData)
        resp1 = capture_fusion_data(x)
        return resp1.data_filepath
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(x)
    print "%s = %s"%(x, capture_fusion_data_client(x))