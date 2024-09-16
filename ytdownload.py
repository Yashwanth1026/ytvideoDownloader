import yt_dlp
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class VideoURL(BaseModel):
    url: str

@app.post("/download")
def download_youtube_video(video: VideoURL):
    ydl_opts = {
        'format': 'best',  
        'outtmpl': '%(title)s.%(ext)s',
    }

   
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video.url])  
        return {"status": "success", "message": "Download complete!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
