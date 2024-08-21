import instaloader
import os

L = instaloader.Instaloader(
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern=''
)

username = 'cristiano'

profile = instaloader.Profile.from_username(L.context, username)


target_dir = os.path.join(os.getcwd(), username)
os.makedirs(target_dir, exist_ok=True)

with open(os.path.join(target_dir, 'photo_info.txt'), 'w') as file:

    photo_count = 0

    for post in profile.get_posts():
        if post.typename == 'GraphImage':

            L.download_post(post, target=profile.username)

            file.write(f"Photo {photo_count + 1}:\n")
            file.write(f"Likes: {post.likes}\n")
            file.write(f"Description: {post.caption}\n\n")

            photo_count += 1
            if photo_count >= 6:
                break

print(f"Скачана первые 6 фотографий из аккаунта {username} с кол-во лайков и описанием в txt файле.")
