# -*- coding: utf-8 -*-
from TTS.api import TTS
ai_vc_cl_file = r"voice_clone_wav\input.wav"
tts = TTS("tts_models/en/vctk/vits",vocoder_name="vocoder_models/en/librispeech100/wavlm-hifigan_prematched")
tts.tts_to_file("",file_path="vc_op_wav.wav",split_sentences=True,speaker="p228")
tts2 = TTS("voice_conversion_models/multilingual/multi-dataset/openvoice_v2")
tts2.voice_conversion_to_file(source_wav ="vc_op_wav.wav" , target_wav=ai_vc_cl_file,file_path="finally.wav")