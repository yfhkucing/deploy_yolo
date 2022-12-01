import streamlit as st 
from yolo_deploy import customDetection


def main():
    detect = customDetection(capture_index=0,model_name='drone.pt')
    detect()

if __name__ == '__main__':
    main()