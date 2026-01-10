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
import main
class gui_class():
    def __init__(self):
        self.window1 = tk.Tk()
        weight_w1 ,height_w1 = pyautogui.size()
        weight_w2 ,height_w2 = weight_w1//2 ,height_w1//2 
        print(weight_w2,height_w2)
        self.window1.geometry(f'{weight_w2}x{height_w2}')
    def gui_interfre(self):
        s_btn_aiasr = tk.Button(self.window1,text="語音識別",command=lambda: main.ai_chating().ai_model_asr(default_model = b2.get()))
        s_btn_aiasr.pack()
        s_btn_aiasr = tk.Button(self.window1,text="AI語音聊天",command=lambda: main.ai_chating().ai_chat(asr_model = b2.get(),ipg="",b1g=b1.get()))
        s_btn_aiasr.pack()
        s_btn_aiasr = tk.Button(self.window1,text="錄音",command=main.ai_chating().record_vc)
        s_btn_aiasr.pack()
        tk.Label(self.window1,text="請輸入文本來輸入聊天內容").pack()
        input_word = tk.Entry(self.window1)
        input_word.pack()
        s_btn_getin = tk.Button(self.window1,text="使用文字聊天(請記得在上面的欄位輸入內容)",command=lambda: main.ai_chating().ai_chat(ipg = input_word.get(),b1g = b1.get()))
        s_btn_getin.pack()
        v1l = ["qwen3:30b","qwen3:8b","qwen3:4b"]
        v2l = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo']
        tk.Label(self.window1,text="選擇聊天用AI模型").pack(side="left")
        b1 = tk.ttk.Combobox(self.window1,values=v1l,state="readonly")
        b1.pack(side="left")
        tk.Label(self.window1,text="選擇語音轉文字用AI模型").pack(side="left")
        b2 = tk.ttk.Combobox(self.window1,values=v2l,state="readonly")
        b2.pack(side="left")
        self.window1.config(bg="aqua")
        self.window1.mainloop()
if __name__ == "__main__":
    gui = gui_class()
    gui.gui_interfre()
