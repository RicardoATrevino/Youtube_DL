Delete MacOs-compatibility if downloading on windows for redundancy
or just drag it out and rename to main if on MacOs

you need yt-dlp, ffmpeg, ffmprobe, ffmplay(unsure about this one). put them all in a folder named 'resources'
          
           resources|         
                    |- ffmpeg.exe / ffmpeg
                    |- ffmplay.exe / ffmplay
                    |- ffmprobe.exe / ffmprobe
                    |- yt-dlp.exe / yt-dlp
                    
          note how in macOs theres no '.exe' for the files. 

I originally made this app bc i dislike how online converters work. 
          
          to-do:
                    add progress bar

intall dependencies 

          pip install -r requirements.txt -e <your current environment>
--
  
          pyinstaller --onefile --add-data "resources;resources" main.py
