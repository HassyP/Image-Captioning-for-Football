from .base_model import GenericCaptioner

class FootballCaptioner(GenericCaptioner):
    def __init__(self):
        super().__init__("ybelkada/blip-image-captioning-base-football-finetuned")
