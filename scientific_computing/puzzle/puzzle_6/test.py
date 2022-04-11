import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("notes.wav")
play_obj = wave_obj.play()
#play_obj.wait_done() #blocking call
while True:
    if(play_obj.is_playing()):
        print('Playing')
    else:
        print('Ended')
        break
