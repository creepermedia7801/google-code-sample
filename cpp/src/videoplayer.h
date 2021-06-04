#ifndef VIDEOPLAYER_H
#define VIDEOPLAYER_H

#include <iostream>

/**
 * A class used to represent a Video Player.
 */
class VideoPlayer {
     public:
        VideoPlayer();
        void showAllVideos();
        void playVideo(std::string videoId);
        void playRandomVideo();
        void stopVideo();  
        void pauseVideo();
        void continueVideo();
        void showPlaying();
        void createPlaylist( std::string playlistName);
        void addVideoToPlaylist( std::string playlistName,  std::string videoId);
        void removeFromPlaylist( std::string playlistName,  std::string videoId);
        void clearPlaylist( std::string playlistName);
        void deletePlaylist( std::string playlistName);
        void showPlaylist( std::string playlistName);
        void showAllPlaylists();
        void searchVideos( std::string searchTerm);
        void searchVideosWithTag( std::string videoTag);
        void flagVideo( std::string videoId);
        void flagVideo( std::string videoId,  std::string reason);
        void allowVideo( std::string videoId);
};

#endif