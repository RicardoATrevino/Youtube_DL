you need yt-dlp, ffmpeg, ffmprobe, ffmplay(unsure about this one). put them all in a folder named 'resources'
          
           resources|         
                    |- ffmpeg.exe
                    |- ffmplay.exe
                    |- ffmprobe.exe
                    |- yt-dlp.exe

I originally made this app bc i dislike how online converters work. 
          
          to-do:
                    add progress bar

intall dependencies 

          pip install -r requirements.txt -e <your current environment>
--
  
          pyinstaller --onefile --add-data "resources;resources" main.py