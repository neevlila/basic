# First step : pip install YouTube

from pytube import YouTube

YouTube('').streams.first().download()
