import yt_dlp
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from any origin (you can limit it to specific origins for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, can be restricted
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the request body
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
            ydl.download([video.url])  # Use the URL from the request body
        return {"status": "success", "message": "Download complete!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
