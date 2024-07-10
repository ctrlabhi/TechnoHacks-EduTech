import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.currently_playing = None

    def load_music(self, file_path):
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            self.currently_playing = file_path
            print(f"Loaded: {file_path}")
        else:
            print(f"File {file_path} does not exist.")

    def play_music(self):
        if self.currently_playing:
            pygame.mixer.music.play()
            print("Music is playing.")
        else:
            print("No music loaded to play.")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Music paused.")
        else:
            print("No music is playing to pause.")

    def unpause_music(self):
        if self.currently_playing and not pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            print("Music unpaused.")
        else:
            print("Music is already playing or nothing to unpause.")

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            print("Music stopped.")
        else:
            print("No music is playing to stop.")

    def main(self):
        while True:
            print("\nMusic Player")
            print("1. Load Music")
            print("2. Play Music")
            print("3. Pause Music")
            print("4. Unpause Music")
            print("5. Stop Music")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                file_path = input("Enter the path to the music file: ")
                self.load_music(file_path)
            elif choice == '2':
                self.play_music()
            elif choice == '3':
                self.pause_music()
            elif choice == '4':
                self.unpause_music()
            elif choice == '5':
                self.stop_music()
            elif choice == '6':
                print("Exiting the music player. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    player = MusicPlayer()
    player.main()
