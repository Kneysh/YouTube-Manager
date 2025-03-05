import os
import json
from dotenv import load_dotenv

load_dotenv()  # This loads variables from the .env file in the current directory

file_name = os.getenv("file_name")  # Now file_name is available


def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("\n")
    print("#" * 50)
    if len(videos) > 0: 
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video["title"]} || {video["duration"]}")
    else:
        print("No Video Found!")
    print("\n")
    print("#" * 50)

def add_new_video(videos):
    title = input("\nEnter the title: ")
    duration = input("Enter the duration: ")
    videos.append({"title": title, "duration": duration})
    save_data(videos)
    print("\nNew video added!")

def update_video(videos):
    list_videos(videos)
    index = int(input("\nEnter the video number: "))
    if 1 <= index <= len(videos):
        new_title = input("\nEnter the title: ")
        new_duration = input("Enter the duration: ")
        videos[index-1] = {"title": new_title, "duration": new_duration}
        save_data(videos)
        print(f"\nVideo no.{index} is updated!")
    else:
        print("\nInvalid video number. Please try again!")

def delete_video(videos):
    list_videos(videos)
    index = int(input("\nEnter the video number: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
        print(f"\nVideo no.{index} is deleted!")
    else:
        print("\nInvalid Video number. Please try again!")



def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option\n")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video details")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos(videos)
            case "2":
                add_new_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("\nHave a nice day!\n")
                break
            case _:
                print("\nInvalid Choice! Please try again.\n")


if __name__ == "__main__":
    main()
