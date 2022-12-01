import streamlit as st 
from yolo_deploy import customDetection


def main():
    detect = customDetection
    #tracker = CentroidTracker(maxDisappeared=200,maxDistance=120)
    detect(capture_index=0,model_name='drone.pt')


if __name__ == '__main__':
    main()