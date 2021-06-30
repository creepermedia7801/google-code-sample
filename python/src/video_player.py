"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""
    video_playing = None
    paused = False
    playlists = {}

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda x: x.title)

        print("Here's a list of all available videos:")
        for j in range(len(video_list)):
            tags = (" ".join(video_list[j].tags))
            print(f"{video_list[j].title} ({video_list[j].video_id}) [{tags}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        self.paused = False
        new_video = self._video_library.get_video(video_id)

        if new_video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self.video_playing is not None:
                self.stop_video()

            self.video_playing = new_video
            print(f"Playing video: {self.video_playing.title}")

    def stop_video(self):
        """Stops the current video."""
        if self.video_playing is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self.video_playing.title}")
            self.video_playing = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        if len(video_list) == 0:
            print("No videos available")
        self.play_video(video_list[random.randint(0, len(video_list) - 1)].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self.video_playing is None:
            print("Cannot pause video: No video is currently playing")
        else:
            if self.paused:
                print(f"Video already paused: {self.video_playing.title}")
            else:
                self.paused = True
                print(f"Pausing video: {self.video_playing.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.video_playing is None:
            print("Cannot continue video: No video is currently playing")
        else:
            if not self.paused:
                print("Cannot continue video: Video is not paused")
            else:
                self.paused = False
                print(f"Continuing video: {self.video_playing.title}")

    def show_playing(self):
        """Displays video currently playing."""
        if self.video_playing is None:
            print("No video is currently playing")
        else:
            tags = (" ".join(self.video_playing.tags))
            if self.paused:
                print(
                    f"Currently playing: {self.video_playing.title} ({self.video_playing.video_id}) [{tags}] - PAUSED")
            else:
                print(f"Currently playing: {self.video_playing.title} ({self.video_playing.video_id}) [{tags}]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for name in self.playlists.keys():
            if playlist_name.upper() == name.upper():
                print("Cannot create playlist: A playlist with the same name already exists")
                return

        new_playlist = Playlist(playlist_name)
        self.playlists[playlist_name] = new_playlist
        print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        found = False
        for name in self.playlists.keys():
            if playlist_name.upper() == name.upper():
                found = True
        if found:
            new_video = self._video_library.get_video(video_id)
            if new_video is None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
                return
            else:
                if self.playlists[name].get_video(video_id) is not None:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                    return
                else:
                    self.playlists[name].videos[video_id] = new_video
                    print(f"Added video to {playlist_name}: {new_video.title}")
                    return
        else:
            print(f"Cannot add video to another {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        all_playlists = list(self.playlists.values())
        if not all_playlists:
            print("No playlists exist yet")
        else:
            all_playlists.sort(key=lambda x: x.name)

            print("Showing all playlists:")
            for z in range(len(all_playlists)):
                print(all_playlists[z].name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.playlists[playlist_name] is None:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        self.playlists[playlist_name].videos = {}

        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda x: x.title)
        results = 0

        for i in range(len(video_list)):
            tags = (" ".join(video_list[i].tags))
            if search_term.upper() in video_list[i].title.upper():
                results += 1
                if results == 1:
                    print(f"Here are the results for {search_term}:")
                print(f"{i + 1}) {video_list[i].title} ({video_list[i].video_id}) [{tags}]")
        if results > 0:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            try:
                choice = int(inp)
                if 0 < choice <= results:
                    self.play_video(video_list[choice - 1].video_id)
            except:
                pass
        else:
            print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        video_list = self._video_library.get_all_videos()
        video_list.sort(key=lambda x: x.title)
        results = 0

        for i in range(len(video_list)):
            tags = (" ".join(video_list[i].tags))
            for tag in video_list[i].tags:
                if video_tag.upper() == tag.upper():
                    results += 1
                    if results == 1:
                        print(f"Here are the results for {video_tag}:")
                    print(f"{i + 1}) {video_list[i].title} ({video_list[i].video_id}) [{tags}]")
        if results > 0:
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            try:
                choice = int(inp)
                if 0 < choice <= results:
                    self.play_video(video_list[choice - 1].video_id)
            except:
                pass
        else:
            print(f"No search results for {video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
