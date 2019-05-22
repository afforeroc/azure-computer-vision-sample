# Azure Computer Vision sample
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Get endpoint and key from environment variables
endpoint = "https://eastus.api.cognitive.microsoft.com/"
key = "<Your credentials>"

# Set credentials
credentials = CognitiveServicesCredentials(key)

# Create client
client = ComputerVisionClient(endpoint, credentials)

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Panoramica_Centro_De_Medellin.jpg/1024px-Panoramica_Centro_De_Medellin.jpg"

image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    print(tag.name)
