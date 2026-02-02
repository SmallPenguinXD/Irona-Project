# -*- coding: utf-8 -*-
import pyautogui
import os
import keyboard as kb
import torch
import time
import ollama
import asyncio
import tkinter as tk
import whisper
from TTS.api import TTS
import wave
import time as tm
import pyaudio
import pygame
import threading
from fsm import forget_sm
import locate_gui
import main
os.getcwd()
print(torch.cuda.is_available())
print(torch.__version__)
print(torch.version.cuda)
ml = ["tts_models/multilingual/multi-dataset/xtts_v2","tts_models/zh-CN/baker/tacotron2-DDC-GST","tts_models/en/vctk/vits","tts_models/ja/kokoro/tacotron2-DDC"]
class judge():
    @staticmethod
    def judgemar(tts_no_model,atext):
        if tts_no_model == "英文":
            print(tts_no_model)
            tts = TTS(ml[2],vocoder_name="vocoder_models/en/librispeech100/wavlm-hifigan_prematched")
            tts.tts_to_file(atext,file_path="vc_op_wav.wav",speaker="p225")
            print(tts_no_model)
        if tts_no_model == "中文":
            print(tts_no_model)
            tts = TTS(ml[1])
            tts.tts_to_file(atext,file_path="vc_op_wav.wav")
            print(tts_no_model)
        if tts_no_model == "日文":
            print(tts_no_model)
            tts = TTS(ml[3],vocoder_name="vocoder_models/ja/kokoro/hifigan_v1")
            tts.tts_to_file(atext,file_path="vc_op_wav.wav")
            print(tts_no_model)

