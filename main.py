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
os.getcwd()
print(torch.cuda.is_available())
print(torch.__version__)
print(torch.version.cuda)
os.getcwd()
print(torch.cuda.is_available())
print(torch.__version__)
print(torch.version.cuda)
import random
t_prompt = ""

#AI-Chating Class
class ai_chating():
    #Reocrding
    def record_vc(self):
        p = pyaudio.PyAudio()
        print("start recording")
        stream = p.open(format=pyaudio.paInt32, channels=1, rate=16000, frames_per_buffer=1024, input=True)
        frames = []
        while True:
            data = stream.read(1024)
            frames.append(data)
            if kb.is_pressed('q'):
                break
        print("stop recording")
        stream.stop_stream()             
        stream.close()                  
        p.terminate()
        awav = wave.open("input_audio.wav","wb")
        awav.setnchannels(1)
        awav.setsampwidth(p.get_sample_size(pyaudio.paFloat32))
        awav.setframerate(24000) 
        awav.writeframes(b"".join(frames))
        awav.close()
    #AI-ASR
    def ai_model_asr(self,default_model):        
        default_model = default_model
        st_asr_time = tm.time()
        if(torch.cuda.is_available() == True):
            devide_to_run_asr = "cuda"
            print(f"your pc is able to run it with {torch.cuda.get_device_name(0)}")
        else:
            devide_to_run_asr = "cpu"
            print("bro your pc is not able to run it with cuda(GPU) or update your cuda")
        ai_model_asr_model_load = whisper.load_model(default_model,device=devide_to_run_asr)
        ai_model_asr_result = ai_model_asr_model_load.transcribe("input_audio.wav",temperature=0.15)
        print(ai_model_asr_result['text'])
        avc = ai_model_asr_result['text']
        total_time = tm.time() - st_asr_time
        print(f"Total use {total_time}sec to run")
        return avc
    #Read Docs :>
    def read_docs(self,file_name):
        if(os.path.exists(rf"brain\\{file_name}")):
            print("File exists")
            with open(rf"brain\\{file_name}","r") as files_need_deal:
                content1 = files_need_deal.read()
                lens1 = len(content1)
                print(lens1)
                if(lens1 == 0):
                    print("prompt is too short")
                else:
                    print("prompt is enough")
                    return content1
    #use voice input or text input
    def vc_or_text(self,ipg,asr_model):
        qe = str(ipg)
        if(len(qe) > 0):
            print(len(qe))
            prompt = str(qe)
        else:
            print(len(qe))
            prompt = str(self.ai_model_asr(default_model = asr_model))
        return prompt
    #ai reply and write memory
    def ai_chat(self,ipg,b1g,asr_model):
        prompt = self.vc_or_text(ipg = ipg,asr_model = asr_model)
        b1r = b1g
        ai_vc_cl_file = r"voice_clone_wav\input.wav"
        st_asr_time = tm.time()
        if(torch.cuda.is_available() == True):
            devide_to_run_aichat = "cuda"
            print(f"your pc is able to run it with {torch.cuda.get_device_name(0)}")
        else:
            devide_to_run_aichat = "cpu"
            print("bro your pc is not able to run it with cuda(GPU) or update your cuda")
        cr_prompt = self.read_docs(file_name="character_prompt.txt")
        brain_memory = self.read_docs(file_name="brain_basic.txt")
        brain_basic_memory = self.read_docs(file_name="long_memory.txt")
        print("start...")
        print(f"{cr_prompt}\n{brain_memory}\n{brain_basic_memory}")
        rr_reply = ""
        reply = ollama.generate(model=f"{b1r}",system=f"""{cr_prompt}\n{brain_memory}\nHistory:{brain_basic_memory}""",prompt=prompt,options={"temperature":0.8,"num_ctx":4096})
        rr_reply = reply["response"]
        rrr_reply = str(rr_reply)
        if(len(rrr_reply) <= 0):
            rrr_reply = "Dude!What can I say?"
        total_time = tm.time() - st_asr_time
        print(f"Total use {total_time}sec to run")
        ask_ddmmyy = time.asctime(time.localtime(time.time()))
        ask_ddmmyy = ask_ddmmyy.replace(":", "_")
        ask_ddmmyy = ask_ddmmyy.replace(" ", "_")
        print(ask_ddmmyy, prompt,"|", rr_reply)
        tts = TTS("tts_models/en/vctk/vits",vocoder_name="vocoder_models/en/librispeech100/wavlm-hifigan_prematched")
        tts.tts_to_file(rrr_reply,file_path="vc_op_wav.wav",speaker="p225")
        tts2 = TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2")
        tts2.voice_conversion_to_file(source_wav ="vc_op_wav.wav", target_wav=ai_vc_cl_file,file_path=f"{ask_ddmmyy}.wav")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(f"{ask_ddmmyy}.wav")
        pygame.mixer.music.play()
        time.sleep(5)
        sb = self.read_docs(file_name="short_bb.txt")
        q1 = rrr_reply
        q2 = "Please evaluate whether this content is worthy of long-term memory,Score 0–1 on the following scale:Task relevance,Novelty,Emotional intensity,Generalizability,Total highest is 4.0,and just reply total score(like 2.0 2.5 1.0 3.7)"
        los = ollama.generate(model="qwen3:4b",system=f"""Background Information:{sb}""",prompt=f"""{q2} question(only answer it):{q1}""")
        print(los["response"])
        ts = float(los["response"])
        if(ts >= 3.0):
            with open(r"brain\long_memory.txt","a",encoding="utf-8") as lmf:
                lmf.write(rf"Penguin(Questioner):{prompt};Yourself:{rrr_reply}\n")
                lmf.close()
        if(ts < 3.0):
            with open(rf"brain\short_memory\{ask_ddmmyy}_short_memory.txt","w",encoding="utf-8") as smf:
                smf.write(f"Penguin(Questioner):{prompt};Yourself:{rrr_reply}\n")
                smf.close()
                forget_sm(ask_ddmmyy=f"{ask_ddmmyy}")
