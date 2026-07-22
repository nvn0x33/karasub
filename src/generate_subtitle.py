from fontTools.ttLib import TTFont

class ASS:
    def __init__(self, video_data, config):
        self.video_data = video_data
        self.config = config
        
        self.write_ass_script()
        

    def get_font_name(self):
        font = TTFont(self.config["font_style"])
        name_table = font["name"]
        
        for record in name_table.names:
            if record.nameId == 4:
                return record.toUnicode()
            
        return "Unknown"