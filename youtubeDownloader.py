from pytube import YouTube

def Download(link):
                try:
                    youtubeObject=YouTube(link)
                    video_stream=youtubeObject.streams.get_highest_resolution()
                    
                    video_stream.download() 
                    print("download completed")
                except Exception as e:
                    print(f"an error occured : {e}")
                

link=input("Enter link of video you want to download: ")
Download(link)

             
                                   
             