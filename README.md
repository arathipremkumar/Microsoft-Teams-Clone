# Microsoft Teams Clone
Microsoft Teams Clone is a simple one-to-one video call app  built in python using Agora SDK. 
Two people can connect in a channel using the App-id from agora.io. Live chat is incorporated using PubNub. An additional screen recording feature is also availabe.

Python is very convenient to work with. It is High level, Interpreted, Object-oriented, Interactive, Modular, Dynamic, Portable and Extensible in C++ & C.
It's advantages are that it is easy to read and write, low maintainance cost, no harms for the software bugs  and it also allows integration with other languages.
It's slow execution speed and large memory consumption makes it weak in mobile computing. But, as my task is to create an application that works on the desktop, python is a good option.

## Agile Project Management Methodology

### Sprint Calendar

#### Sprint 1
* Did Research on requirements and resources.
* Decided to build a Desktop Teams Clone in Python

#### Sprint 2
* Mentors helped with information on SDK s like Agora and Web rtc.
* Built the minimum required feature - One-to-One Video Call using Agora
  <img width="500" alt="first ss" src="https://user-images.githubusercontent.com/57580997/125207968-67957600-e2ad-11eb-855e-b7810b47c328.png">

#### Sprint 3
* Added Screen Recording feature.
* Faced bugs on incorporating the new feature to the existing.
* As per the instruction of mentors, started documentation of the project in GitHub.
  <img width="500" alt="sec ss" src="https://user-images.githubusercontent.com/57580997/125208039-ca870d00-e2ad-11eb-95d9-fc30587e1f52.png">

#### Sprint 4
* Worked on User Interface.
* Faced bugs in designing UI with PyQt5.
* Incorporated Live chat application to teams clone.
* Fixed the bugs faced in sprint 3 and 4.
* Completed final documentation
* Made necessary changes as suggested by mentors and created final video for submission.

### Output of project in action
![image](https://user-images.githubusercontent.com/57580997/125112749-337f5100-e105-11eb-8b68-4dfe68bf12fe.png)


### References
* https://github.com/AgoraIO-Community/Agora-Python-QuickStart/tree/master/basic_one_to_one_video
* https://github.com/ajb413/python-desktop-chat-application

### Installation

#### Requirements
* Python 3.6+

* Xcode (macOS)

* Visual Studio 2017+ with C++ (Windows)

#### Dependencies
* Agora Python SDK

* PyQt5

* PubNub

### How to get Agora App-id
* Create a developer account at agora.io.
* Navigate in the dashboard tree on the left to Projects > Project List.
* Copy the app ID that you obtained from the dashboard into  line 447 of one2one.py line 447. 
* self.rtc.initialize('............ENTER YOUR AGORA APP ID HERE............', None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)

### How to get PubNub publish key and subscription key
* First make a free PubNub account to instantly get API keys. It's free up to 1 million messages per month, forever.
* Copy and paste your free PubNub API keys onto line 340 of one2one.py.
* pnconfig.publish_key = '............ENTER YOUR PUBNUB PUBLISH KEY HERE............'
* pnconfig.subscribe_key = '............ENTER YOUR PUBNUB SUBSCRIBE KEY HERE............'

### Author

Arathi Premkumar
