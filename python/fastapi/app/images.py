from dotenv import load_dotenv
from imagekitio import ImageKit
import os
load_dotenv()
imagekit = ImageKit(
    private_key=os.getenv('imagekit_private_key'), # arg is the variable in the .envvv file in which the private keyis stored
    public_key = os.getenv('imagekit_public_key'),
    url_endpoint = os.getenv('imagekit_url')
)