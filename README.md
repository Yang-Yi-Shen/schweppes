# Schweppes

**Project description:** An image processing software that takes a video stream, and analyses it to determine information about people who may be in view. It also detects abnormal motion by people, and can be used to detect falls, running, etc. 

**Todo list:**
- [ ] Establish video feed from webcam
- [ ] Detect people in video feed
- - [ ] Use haar cascade to detect human presence
- - [ ] Draw yellow boxes around people
- [ ] Detect abnormal motion
- - [ ] Track change in center of drawn boxes
- - [ ] Create normal behavior model
- - [ ] Raise warning if behavior not conforming to model 