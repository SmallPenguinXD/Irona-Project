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
        self.window2 = tk.Tk()
        self.window1 = tk.Toplevel(self.window2)
        weight_w1 ,height_w1 = pyautogui.size()
        weight_w2 ,height_w2 = weight_w1//2 ,height_w1//2 
        print(weight_w2,height_w2)
        self.window1.geometry(f'{weight_w2}x{height_w2}')
        self.window2.geometry(f'{weight_w2}x{height_w2}')
    def gui_setting_page(self):
        v1l = ["qwen3:30b","qwen3:8b","qwen3:4b"]
        v2l = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large', 'large-v3-turbo', 'turbo']
        v3l = ["中文","英文","日文"]
        tk.Label(self.window1,text="選擇聊天用AI模型").pack()
        self.b1gg = tk.ttk.Combobox(self.window1,values=v1l,state="readonly")
        self.b1gg.pack()
        tk.Label(self.window1,text="選擇語音轉文字用AI模型").pack()
        self.b2gg = tk.ttk.Combobox(self.window1,values=v2l,state="readonly")
        self.b2gg.pack()
        tk.Label(self.window1,text="選擇AI回覆使用的語言").pack()
        self.b3gg = tk.ttk.Combobox(self.window1,values=v3l,state="readonly")
        self.b3gg.pack()
        btn_ss = tk.Button(self.window1,text="保存設定",command=self.save_setting)
        btn_ss.pack()
        self.window1.config(bg="aqua")
    def save_setting(self):
        self.b1 = self.b1gg.get()
        self.b2 = self.b2gg.get()
        self.b3 = self.b3gg.get()
        print(f"{self.b1} + {self.b2} + {self.b3}")
    def gui_interfre(self):
        s_btn_aiasr = tk.Button(self.window2,text="語音識別",command=lambda: main.ai_chating().ai_model_asr(default_model = self.b2))
        s_btn_aiasr.pack()
        s_btn_aiasr = tk.Button(self.window2,text="使用語音聊天",command=lambda: main.ai_chating().ai_chat(asr_model = self.b2,ipg="",b1g=self.b1,tts_no_model=str(self.b3)))
        s_btn_aiasr.pack()
        s_btn_aiasr = tk.Button(self.window2,text="錄音",command=main.ai_chating().record_vc)
        s_btn_aiasr.pack()
        tk.Label(self.window2,text="請輸入文本來輸入聊天內容").pack()
        input_word = tk.Entry(self.window2)
        input_word.pack()
        s_btn_getin = tk.Button(self.window2,text="使用文字聊天(請記得在上面的欄位輸入內容)",command=lambda: main.ai_chating().ai_chat(ipg = input_word.get(),b1g = self.b1,asr_model = self.b2,tts_no_model=str(self.b3)))
        s_btn_getin.pack()
        self.window2.config(bg="aqua")
        self.window2.mainloop()
if __name__ == "__main__":
    gui = gui_class()
    gui.gui_setting_page()
    gui.gui_interfre()
    