"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_name):
        self._name = playlist_name
        self._videos = {}

    @property
    def name(self) -> str:
        """Returns the name of the playlist."""
        return self._name

    @property
    def videos(self) -> {}:
        """Returns the videos in the playlist."""
        return self._videos

    def get_videos(self):
        """Returns all available video information from the playlist."""
        return list(self._videos.values())

    def get_video(self, video_id):
        """Returns the video object (title, url, tags) from the playlist.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._videos.get(video_id, None)



