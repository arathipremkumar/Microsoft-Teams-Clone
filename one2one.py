import os


os.environ['QT_MAC_WANTS_LAYER'] = '1'    #shows the main window
import sys
import MainWindow
import agorartc
from PyQt5 import QtOpenGL
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

localWinId = -1
remoteWinId = -1

#The SDK uses the MyRtcEngineEventHandler interface class to send callbacks to the application,
#the application inherits the methods of this interface class to retrieve these callbacks.
class MyRtcEngineEventHandler(agorartc.RtcEngineEventHandlerBase):

    def __init__(self, rtc):
        super().__init__()
        self.rtc = rtc

    #reports a warning during SDK runtime
    def onWarning(self, warn, msg):
        print("warn: ")
        print(warn)

    #reports an error during SDK runtime
    def onError(self, err, msg):
        print("err: ")
        print(err)

    #Occurs when the local user joins a specified channel
    def onJoinChannelSuccess(self, channel, uid, elapsed):
        print("onJoinChannelSuccess")

    #Occurs when a user rejoins the channel after being disconnected due to network problems
    def onRejoinChannelSuccess(self, channel, uid, elapsed):
        print("onRejoinChannelSuccess")

    #Occurs when a user leaves the channel
    def onLeaveChannel(self, stats):
        print("onLeaveChannel")

    #Occurs when the user role switches in a live streaming. For example, from a host to an audience or vice versa
    def onClientRoleChanged(self, oldRole, newRole):
        print("onClientRoleChanged")

    #Occurs when a remote user (COMMUNICATION)/host (LIVE_BROADCASTING) joins the channel
    def onUserJoined(self, uid, elapsed):
        global remoteWinId
        if remoteWinId != -1:
            remoteVideoCanvas = agorartc.createVideoCanvas(remoteWinId)
            remoteVideoCanvas.uid = uid
            self.rtc.setupRemoteVideo(remoteVideoCanvas)

    #Occurs when a remote user (COMMUNICATION)/host (LIVE_BROADCASTING) leaves the channel
    def onUserOffline(self, uid, reason):
        print("onUserOffline")

    # Last mile refers to the connection between the local device and Agora edge server
    # this callback reports once every two seconds the uplink and downlink last mile
    # network conditions of the local user before the user joins the channel
    def onLastmileQuality(self, quality):
        print("onLastmileQuality")

    #Reports the last-mile network probe result
    def onLastmileProbeResult(self, res):
        print("onLastmileProbeResult")

    #Occurs when the connection between the SDK and the server is interrupted
    def onConnectionInterrupted(self):
        print("onConnectionInterrupted")

    #Occurs when the SDK cannot reconnect to Agora edge server 10 seconds after
    # its connection to the server is interrupted
    def onConnectionLost(self):
        print("onConnectionLost")

    #Occurs when your connection is banned by the Agora Server
    def onConnectionBanned(self):
        print("onConnectionBanned")

    #Occurs when an API method is executed
    def onApiCallExecuted(self, err, api, res):
        print("onApiCallExecuted" + str(api))

    #Occurs when the token has expired
    #Once you receive this callback, generate a new token on your app server,
    #call renewToken to pass the new token to the SDK
    def onRequestToken(self):
        print("onRequestToken")

    #Occurs when the token expires in 30 seconds
    def onTokenPrivilegeWillExpire(self, token):
        print("onTokenPrivilegeWillExpire")

    #Reports the statistics of the audio stream from each remote user/host
    def onAudioQuality(self, uid, quality, delay, lost):
        print("onAudioQuality")

    #Reports the statistics of the RtcEngine once every two seconds
    def onRtcStats(self, stats):
        print("onRtcStats")

    #Reports the last mile network quality of each user in the channel once every two seconds
    def onNetworkQuality(self, uid, txQuality, rxQuality):
        print("onNetworkQuality")

    #Reports the statistics of the local video streams
    def onLocalVideoStats(self, stats):
        print("onLocalVideoStats")

    #Reports the statistics of the video stream from each remote user/host
    def onRemoteVideoStats(self, stats):
        print("onRemoteVideoStats")

    #Reports the statistics of the local audio stream
    def onLocalAudioStats(self, stats):
        print("onLocalAudioStats")

    #Reports the statistics of the audio stream from each remote user/host
    def onRemoteAudioStats(self, stats):
        print("onRemoteAudioStats")

    #Occurs when the local audio stream state changes
    def onLocalAudioStateChanged(self, state, error):
        print("onLocalAudioStateChanged")

    #Occurs when the remote audio state changes
    def onRemoteAudioStateChanged(self, uid, state, reason, elapsed):
        print("onRemoteAudioStateChanged")

    #Reports the volume information of users
    def onAudioVolumeIndication(self, speakers, speakerNumber, totalVolume):
        print("onAudioVolumeIndication")

    #Occurs when the most active remote speaker is detected
    def onActiveSpeaker(self, uid):
        print("onActiveSpeaker")

    #Occurs when the video stops playing
    def onVideoStopped(self):
        print("onVideoStopped")

    #Occurs when the first local video frame is rendered
    def onFirstLocalVideoFrame(self, width, height, elapsed):
        print("onFirstLocalVideoFrame")

    #Occurs when the first remote video frame is received and decoded
    def onFirstRemoteVideoDecoded(self, uid, width, height, elapsed):
        print("onFirstRemoteVideoDecoded")

    #Occurs when the first remote video frame is rendered
    def onFirstRemoteVideoFrame(self, uid, width, height, elapsed):
        print("onFirstRemoteVideoFrame")

    #Occurs when a remote user stops/resumes sending the audio stream
    def onUserMuteAudio(self, uid, muted):
        print("onUserMuteAudio")

    #Occurs when a remote user stops/resumes sending the video stream
    def onUserMuteVideo(self, uid, muted):
        print("onUserMuteVideo")

    #Occurs when a remote user enables/disables the video module
    def onUserEnableVideo(self, uid, enabled):
        print("onUserEnableVideo")

    #Occurs when the audio device state changes
    def onAudioDeviceStateChanged(self, deviceId, deviceType, deviceState):
        print("onAudioDeviceStateChanged")

    #Occurs when the volume of the playback device, microphone, or application changes
    def onAudioDeviceVolumeChanged(self, deviceType, volume, muted):
        print("onAudioDeviceVolumeChanged")

    #Occurs when the camera is turned on and ready to capture video
    def onCameraReady(self):
        print("onCameraReady")

    #Occurs when the camera focus area is changed
    def onCameraFocusAreaChanged(self, x, y, width, height):
        print("onCameraFocusAreaChanged")

    #The camera exposure area has changed
    def onCameraExposureAreaChanged(self, x, y, width, height):
        print("onCameraExposureAreaChanged")

    #Occurs when the audio mixing file playback finishes
    def onAudioMixingFinished(self):
        print("onAudioMixingFinished")

    #Occurs when the playback state of the local user's music file changes.
    def onAudioMixingStateChanged(self, state, errorCode):
        print("onAudioMixingStateChanged")

    #Occurs when a remote user starts audio mixing
    def onRemoteAudioMixingBegin(self):
        print("onRemoteAudioMixingBegin")

    #Occurs when a remote user finishes audio mixing
    def onRemoteAudioMixingEnd(self):
        print("onRemoteAudioMixingEnd")

    #Occurs when the local audio effect playback finishes
    def onAudioEffectFinished(self, soundId):
        print("onAudioEffectFinished")

    #Occurs when the SDK decodes the first remote audio frame for playback
    def onFirstRemoteAudioDecoded(self, uid, elapsed):
        print("onFirstRemoteAudioDecoded")

    #Occurs when the video device state changes
    def onVideoDeviceStateChanged(self, deviceId, deviceType, deviceState):
        print("onVideoDeviceStateChanged")

    #Occurs when the local video stream state changes
    def onLocalVideoStateChanged(self, localVideoState, error):
        print("onLocalVideoStateChanged")

    #Occurs when the video size or rotation of a specified user changes
    def onVideoSizeChanged(self, uid, width, height, rotation):
        print("onVideoSizeChanged")

    #Occurs when the remote video state changes
    def onRemoteVideoStateChanged(self, uid, state, reason, elapsed):
        print("onRemoteVideoStateChanged")

    #Occurs when a specified remote user enables/disables the local video capturing function
    def onUserEnableLocalVideo(self, uid, enabled):
        print("onUserEnableLocalVideo")

    #Occurs when the local user receives the data stream from the remote user within five seconds
    def onStreamMessage(self, uid, streamId, data, length):
        print("onStreamMessage")

    #Occurs when the local user does not receive the data stream from the remote user within five seconds
    def onStreamMessageError(self, uid, streamId, code, missed, cached):
        print("onStreamMessageError")

    #Occurs when the media engine loads
    def onMediaEngineLoadSuccess(self):
        print("onMediaEngineLoadSuccess")

    #Occurs when the media engine call starts
    def onMediaEngineStartCallSuccess(self):
        print("onMediaEngineStartCallSuccess")

    #Occurs when the state of the media stream relay changes
    def onChannelMediaRelayStateChanged(self, state, code):
        print("onChannelMediaRelayStateChanged")

    #Reports events during the media stream relay
    def onChannelMediaRelayEvent(self, code):
        print("onChannelMediaRelayEvent")

    #Occurs when the engine sends the first local audio frame
    def onFirstLocalAudioFrame(self, elapsed):
        print("onFirstLocalAudioFrame")

    #Occurs when the engine receives the first audio frame from a specific remote user
    def onFirstRemoteAudioFrame(self, uid, elapsed):
        print("onFirstRemoteAudioFrame")

    #Occurs when the state of the RTMP or RTMPS streaming changes
    def onRtmpStreamingStateChanged(self, url, state, errCode):
        print("onRtmpStreamingStateChanged")

    #Reports the result of calling the addPublishStreamUrl method
    def onStreamPublished(self, url, error):
        print("onStreamPublished")

    #Reports the result of calling the removePublishStreamUrl method
    def onStreamUnpublished(self, url):
        print("onStreamUnpublished")

    #Occurs when the publisher's transcoding is updated
    def onTranscodingUpdated(self):
        print("onTranscodingUpdated")

    #Occurs when a voice or video stream URL address is added to the interactive live streaming
    def onStreamInjectedStatus(self, url, uid, status):
        print("onStreamInjectedStatus")

    #Occurs when the local audio route changes
    def onAudioRouteChanged(self, routing):
        print("onAudioRouteChanged")

    #Occurs when the published media stream falls back to an audio-only stream due to poor
    # network conditions or switches back to video stream after the network conditions improve
    def onLocalPublishFallbackToAudioOnly(self, isFallbackOrRecover):
        print("onLocalPublishFallbackToAudioOnly")

    #Occurs when the remote media stream falls back to audio-only stream due to poor network conditions
    # or switches back to video stream after the network conditions improve
    def onRemoteSubscribeFallbackToAudioOnly(self, uid, isFallbackOrRecover):
        print("onRemoteSubscribeFallbackToAudioOnly")

    #Reports the transport-layer statistics of each remote audio stream
    def onRemoteAudioTransportStats(self, uid, delay, lost, rxKBitRate):
        print("onRemoteAudioTransportStats")

    #Reports the transport-layer statistics of each remote video stream
    def onRemoteVideoTransportStats(self, uid, delay, lost, rxKBitRate):
        print("onRemoteVideoTransportStats")

    #Occurs when the microphone is enabled/disabled
    def onMicrophoneEnabled(self, enabled):
        print("onMicrophoneEnabled")

    #Occurs when the connection state between the SDK and the server changes
    def onConnectionStateChanged(self, state, reason):
        print("onConnectionStateChanged")

    #Occurs when the network type changes
    def onNetworkTypeChanged(self, type):
        print("onNetworkTypeChanged")

    #Occurs when the local user registers a user account
    def onLocalUserRegistered(self, uid, userAccount):
        print("onLocalUserRegistered")

    #Occurs when the SDK gets the user ID and user account of the remote user
    def onUserInfoUpdated(self, uid, info):
        print("onUserInfoUpdated")


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainWindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.window1 = GLwindow()
        self.window2 = GLwindow()
        self.gridLayout.addWidget(self.window1)
        self.gridLayout_2.addWidget(self.window2)
        self.joinButton.clicked.connect(self.joinChannel)
        self.leaveButton.clicked.connect(self.leaveChannel)
        self.videoButton.clicked.connect(self.disableLocalVideo)
        self.AudioButton.clicked.connect(self.disableLocalAudio)
        self.screenrecButton.clicked.connect(self.screen_recording)
        #self.stop_screenrecButton.clicked.connect(self.stop_screen_recording)



        self.rtc = agorartc.createRtcEngineBridge()
        self.eventHandler = MyRtcEngineEventHandler(self.rtc)
        self.rtc.initEventHandler(self.eventHandler)

    #This event handler is called with the given event when Qt receives
    # a window close request for a calendar from the window system
    def closeEvent(self, event):
        self.rtc.release(True)
        event.accept()

    #Joins a channel with the user ID, and configures whether to publish or
    # automatically subscribe to the audio or video streams
    def joinChannel(self):
        global localWinId, remoteWinId
        localWinId = self.window1.effectiveWinId().__int__()
        remoteWinId = self.window2.effectiveWinId().__int__()

        if self.checkAppId() == False:
            QMessageBox.information(self, "Message",
                                    "Please input your App ID of your project.",
                                    QMessageBox.Yes)
            return
        if self.checkChannelName() == False:
            QMessageBox.information(self, "Message",
                                    "The channel name contains illegal character.",
                                    QMessageBox.Yes)
            return
        if len(self.channelEdit.text()) == 0:
            QMessageBox.information(self, "Message",
                                    "Please input the channel name.",
                                    QMessageBox.Yes)
            return
        if len(self.channelEdit.text()) > 64:
            QMessageBox.information(self, "Message",
                                    "The length of the channel name must be less than 64.",
                                    QMessageBox.Yes)
            return

        # self.rtc.initialize(self.appIdEdit.text()) to take appid as input
        #reads appid taken from Agora's official site and is stored in 'appid.txt'
        f = open('appid.txt')
        lines = f.read()
        self.rtc.initialize(lines, None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)

        self.rtc.enableVideo()
        localVideoCanvas = agorartc.createVideoCanvas(localWinId)
        ret = self.rtc.setupLocalVideo(localVideoCanvas)
        channelName = self.channelEdit.text()
        self.rtc.joinChannel("", channelName, "", 0)
        self.rtc.startPreview()

    #Occurs when a user leaves the channel
    def leaveChannel(self):
        self.rtc.leaveChannel()

    #Enables/Disables the local video capture
    def disableLocalVideo(self):
        if self.videoButton.isChecked():
            self.videoButton.setStyleSheet("border-image : url('video.png');")
            self.rtc.enableLocalVideo(False)
        else:
            self.videoButton.setStyleSheet("border-image : url('videoon.png');")
            self.rtc.enableLocalVideo(True)


    def disableLocalAudio(self):
        if self.AudioButton.isChecked():
            self.AudioButton.setStyleSheet("border-image : url('nomic.png');background-color : 'white';")
            self.rtc.enableLocalAudio(False)
        else:
            self.AudioButton.setStyleSheet("border-image : url('mic.png');")
            self.rtc.enableLocalAudio(True)

    def screen_recording(self):
        os.system('python screen_recording.py')

    #def stop_screen_recording(self):
        #print("Stop Screen Recording Triggered!")
        #screen_recording.manualStop()


    def checkAppId(self):
        #if len(self.appIdEdit.text()) == 0:
         #   return False
        return True

    def checkChannelName(self):
        channelName = self.channelEdit.text()
        for char in channelName:
            if ord(char) >= ord('a') and ord(char) <= ord('z'):
                continue
            elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
                continue
            elif ord(char) >= ord('0') and ord(char) <= ord('9'):
                continue
            elif char in ["!", "#", "$", "%", "&", "(", ")", "+", "-", ":",
                          ";", "<", "=", ".", ">", "?", "@", "[", "]", "^",
                          "_", "{", "}", "|", "~", ","] or ord(char) == 32:
                continue
            else:
                return False
        return True

# QOpenGLWidget provides functionality for displaying OpenGL graphics integrated into a Qt application
class GLwindow(QtOpenGL.QGLWidget):
    def __init__(self):
        QtOpenGL.QGLWidget.__init__(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)    ##create a new instance of QApplication
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())           #makes you immediately close the program after the Qt Event loop is over,
                                    # which is in most cases when you close the GUI
