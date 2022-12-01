import streamlit as st 
from yolo_deploy import customDetection


def main():
    detect = customDetection(capture_index=0,model_name='drone.pt')
    #tracker = CentroidTracker(maxDisappeared=200,maxDistance=120)
    detect()

if __name__ == '__main__':
    main()