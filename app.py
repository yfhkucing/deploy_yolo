import streamlit as st 
from yolo_deploy import customDetection


def main():
    detect = customDetection
    #tracker = CentroidTracker(maxDisappeared=200,maxDistance=120)
    detect()


if __name__ == '__main__':
    main()