# manzil =  "https://www.tiktok.com/@nor10122/video/7037155617491913986"
async def tk(link):
    import requests
    import json

    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "7dc162a51bmshf078ddda23e0570p11090djsna83b84a87e09",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)

    return {"play":rest['video'][0], "music":rest['music'][0],"description":rest['description'], "author": rest['author']}
    # return rest

# print(tk("https://www.tiktok.com/@nor10122/video/7037155617491913986"))