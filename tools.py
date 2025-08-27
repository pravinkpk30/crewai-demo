from crewai_tools import YoutubeChannelSearchTool
from embedchain import App
import os

class GeminiYoutubeChannelSearchTool(YoutubeChannelSearchTool):
    def __init__(self, **kwargs):
        # Initialize with Google's embedding model
        config = {
            "llm": {
                "provider": "google",
                "config": {
                    "model": "gemini/gemini-1.5-flash",
                    "api_key": os.getenv("GOOGLE_API_KEY")
                }
            }
        }
        super().__init__(**kwargs, config=config)

# Initialize the tool with a specific Youtube channel handle
yt_tool = GeminiYoutubeChannelSearchTool(youtube_channel_handle='@booleanbuffet-pr')