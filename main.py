from src import Handle


if __name__ == "__main__":
    new_handle = Handle()
    vid_files = new_handle.init_UI()
    
    new_handle.parallel_process_vids(vid_files)
        
# DATA:
# new_ui.config = configurations for colors, font style and font size
# vid_files = an array of dicts containing video name and its path
# videos_data = an array of dicts containing video name, its path, font_size and empty transcript dictionary to later append data into.

# TODO: calculate font size after obtaining video resolution            [Done]
#       clean and refactor the transcribed segments into usable form    [Done]

#       Write .ass file using the segments and config details and burn it into the video. [Done]

#       Refactor the main code where class is called.
#       Burn the subtitle file into the video file.
#       Allow user to adjust the percentage of the font size instead of actual font size.
#       Add threading feature to allow multiple video files at once.