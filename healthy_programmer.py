"""
Healthy Programmer: This is a Python program using pygame that reminds a programmer to drink water (every 35 mins),
do eye exercises (every 30 mins), and perform physical activity (every 45 mins) during work hours (9am-5pm).
The program should:
- Play audio reminders until the user confirms completion ("drank" for water, "eydone" for eyes, "exdone" for physical).
- Maintain log completion times in separate files for each activity.
- Manage overlapping reminders, so they don't play simultaneously.
"""

from pygame import mixer     # pygame module for loading and playing sounds
import datetime
from emoji import emojize
import time


# Function to play audio with user confirmation
def play_audio(audio_file, activity):
    mixer.init()  # Start the mixer
    mixer.music.load(audio_file)   # Load the song
    mixer.music.set_volume(0.5)   # Set the volume
    mixer.music.play()  # Start playing the song

    while True:
        a = input("Enter: ")
        if a == activity:
            mixer.music.stop()
            break


# Function to log completion time
def log_completion(file):
    with open(f"{file}_log.txt", "a") as f:
        f.write(f"{file.capitalize()} at\t{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


if __name__ == "__main__":
    water_start = time.time()
    eye_start = time.time()
    physical_start = time.time()
    water_interval = 35*60  # seconds
    eye_interval = 30*60   # seconds
    physical_interval = 45*60  # seconds

    while True:
        current_time = datetime.datetime.now()

        # Check if within work hours (9 am to 5 pm)
        # if current_time.hour == 12 and 28 <= current_time.minute < 30:
        if 9 <= current_time.hour < 17:
            if time.time() - water_start > water_interval:
                print(emojize("\nWater drinking time :pouring_liquid:! Enter 'drank' to stop the reminder music."))
                play_audio("water_time.mp3", "drank")
                water_start = time.time()
                log_completion("water_drank")

            if time.time() - eye_start > eye_interval:
                print(emojize("\nEye exercise time :eyes:! Enter 'eydone' to stop the reminder music."))
                play_audio("time_to_relax_your_eyes.mp3", "eydone")
                eye_start = time.time()
                log_completion("eye_exercise")

            if time.time() - physical_start > physical_interval:
                print(emojize("\nPhysical exercise time :woman_running::woman_lifting_weights:!"
                              "Enter 'exdone' to stop the reminder music."))
                play_audio("physical_exercise.mp3", "exdone")
                physical_start = time.time()
                log_completion("physical_exercise")

        else:
            print("\nWell Done! You successfully completed your activity tasks during your work hours today. "
                  "See you tomorrow!")
            break