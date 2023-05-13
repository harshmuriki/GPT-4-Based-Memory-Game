import openai
from dotenv import load_dotenv
import os


def prompt(size=3, prompt="color"):

    # openai.api_key = "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"
    load_dotenv("variables.env")
    # openai.api_key_path = "variables.env"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = "Give me image that only has " + prompt + "which is an icon"

    response = openai.Image.create(
        prompt=prompt,
        n=size,
        size="256x256"
    )

    # print(response)
    # "url":

    links = [link["url"] for link in response["data"]]
    # print(links)
    # "https://oaidalleapiprodscus.blob.core.windows.net/private/org-dZcEmqV4WTGc8KyvoaKKdtso/user-3xDZBl4STWUXMYfZRINHE7Cn/img-9LOJUT4Cvn3Ye3mSBWkXFOcl.png?st=2023-05-10T05%3A07%3A21Z&se=2023-05-10T07%3A07%3A21Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-
    return links

# data = prompt()

# print(arr)
