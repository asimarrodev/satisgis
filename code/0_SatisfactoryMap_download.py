import requests
import os

def download_map_tiles(base_url, c, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    x, y, v = 0, 0, 1726055654
    while True:
        image_url = f"{base_url}/{c}/{x}/{y}.png?v={v}"
        response = requests.get(image_url)
        print(f"Trying: {image_url}")

        if response.status_code == 200:
            file_name = f"{save_path}/{x}_{y}.png"
            with open(file_name,"wb") as file:
                file.write(response.content)
            print(f"Downloaded: {file_name}")
            x += 1
        else:
            if x == 0:
                print(f"No more tiles found at y={y}, stopping.")
                break 
            else:
                x = 0
                y += 1
                print(f"Moving to next row: y={y}")


# c = 5 Game Map // c = 3 Realistic Map
c = 3
save_path = 'img/realistic_map'

download_map_tiles(base_url='https://static.satisfactory-calculator.com/imgMap/gameLayer/EarlyAccess',c=c,save_path=save_path)