from transformers import BlipProcessor, BlipForConditionalGeneration
from config import DEVICE

class GenericCaptioner:
    def __init__(self, model_id: str):
        self.processor = BlipProcessor.from_pretrained(model_id)
        self.model = BlipForConditionalGeneration.from_pretrained(model_id).to(DEVICE)

    def generate_caption(self, image, prompt=None, max_tokens=30):
        inputs = self.processor(image, prompt if prompt else "", return_tensors="pt").to(DEVICE)
        output = self.model.generate(**inputs, num_beams=3, max_new_tokens=max_tokens)
        return self.processor.decode(output[0], skip_special_tokens=True)
