import wave
import math
import pylab as pl
import numpy as np
import Volume as vp

audio = '1.wav'

def main(wavName):
    fw = wave.open(wavName, 'r')
    params = fw.getparams()
    print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = fw.readframes(nframes)
    waveData = np.fromstring(strData, dtype=np.int16)
    waveData = waveData*1.0/max(abs(waveData))  # normalization

    factor = int(len(waveData)/nchannels)

    waveData_plot = waveData[0: factor]

    print(len(waveData_plot))

    fw.close()

    # calculate volume
    frameSize = 256
    overLap = 128
    volume11 = vp.calVolume(waveData_plot,frameSize,overLap)
    volume12 = vp.calVolumeDB(waveData_plot,frameSize,overLap)

    # plot the wave
    time = np.arange(0, nframes)*(1.0/framerate)
    time2 = np.arange(0, len(volume11))*(frameSize-overLap)*1.0/framerate

    pl.subplot(311)
    pl.plot(time, waveData_plot)
    pl.ylabel("Amplitude")
    pl.subplot(312)
    pl.plot(time2, volume11)
    pl.ylabel("absSum")
    pl.subplot(313)
    pl.plot(time2, volume12, c="g")
    pl.ylabel("Decibel(dB)")
    pl.xlabel("time (seconds)")
    pl.show()


if __name__ == "__main__":
    main(audio)
