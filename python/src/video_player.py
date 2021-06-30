"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""
    video_playing = None
    paused = False

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
                print(f"Currently playing: {self.video_playing.title} ({self.video_playing.video_id}) [{tags}] - PAUSED")
            else:
                print(f"Currently playing: {self.video_playing.title} ({self.video_playing.video_id}) [{tags}]")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

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
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

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
