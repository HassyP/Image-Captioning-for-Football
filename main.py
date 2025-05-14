from models.base_model import GenericCaptioner
from models.football_model import FootballCaptioner
from utils.image_loader import load_image
from utils.name_extractor import extract_entity_name
from utils.caption_merger import replace_placeholder
from config import IMAGE_PATH

def main():
    image = load_image(IMAGE_PATH)

    # FuseCap
    fusecap = GenericCaptioner("noamrot/FuseCap")
    fuse_caption = fusecap.generate_caption(image, prompt="a picture of ")
    print("FuseCap:", fuse_caption)

    # Football Model
    football_model = FootballCaptioner()
    football_caption = football_model.generate_caption(image)
    print("Football Caption:", football_caption)

    # Extract player name
    player = extract_entity_name(football_caption.capitalize())
    print("Extracted Name:", player)

    # Merge
    final_caption = replace_placeholder(fuse_caption, player)
    print("Final Caption:", final_caption)

if __name__ == "__main__":
    main()
