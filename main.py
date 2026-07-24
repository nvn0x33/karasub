from src import Handle


if __name__ == "__main__":
    new_handle = Handle()
    vid_files = new_handle.init_UI()
    
    new_handle.append_font_data(vid_files)
    
    new_handle.parallel_process_vids()
    