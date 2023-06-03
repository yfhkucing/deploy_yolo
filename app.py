#import streamlit as st 
from yolo_deploy import customDetection


def main():
    model = 'models\drone_survivor.pt'
    detect = customDetection(capture_index=0,model_name=model)
    detect()

if __name__ == '__main__':
    main()