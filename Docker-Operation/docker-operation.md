---
marp: true
size: 4:3
theme: default
#backgroundColor: purple

---
# Docker Common Operation
# 容器，开箱即学 
# “老师再也不担心 我的学习了”
by Jibo HE
hejibolaboratory@pku.org.cn
清华大学社会科学学院心理学系

---
# Lecture Goal/学习目标
- 制作一个可以用OpenCV, dlib的Python开发环境
- 此开发环境可以用于开发疲劳检测，平均脸，情绪识别等心理学重要议题
- 做到开箱即用

---
# 如何获得此强大容器，开箱即学？
- Step 1. 下载并安装 https://www.docker.com
- Step 2. 在cmd或者terminal运行
    docker pull hejibo1984/facemorperbyhejibo:withFaceLandmark

---
# Relationship between docker image/镜像 and docker container/容器
![width:800px](docker-image-container.png)

---
# run a docker image
docker run -it hejibo1984/facemorperbyhejibo:latest

---
# add a local file to a docker container
docker cp wifi.txt vigorous_aryabhata:/tmp/hejiboStuff/wifi.txt

docker cp shape_predictor_68_face_landmarks.dat vigorous_aryabhata:/tmp/hejibo/shape_predictor_68_face_landmarks.dat

## References:
https://takacsmark.com/copying-files-from-host-to-docker-container/

---
# 如何获得container ID
通过运行 docker ps 命令获取刚从其退出的容器的容器 ID：

docker ps -a

---
# Save container changes into an image 
创建新的“HelloWorld”映像，其中包含已运行的第一个容器中的更改。 为此，请运行 docker commit 命令，将 <containerid> 替换为容器的 ID：

docker commit <containerid> helloworld

## 例如：
C:\Users\hejibo\Downloads>docker commit 6be186b672f5 hejibo1984/facemorperbyhejibo:withFaceLandmark

sha256:cc22d9ce4cc71b89ef35413fe3512656005f944c1650bdc05bcb68d408a815c2

---
# 查看docker 镜像列表
完成后，现在你就具有一个包含“hello world”脚本的自定义映像了。 执行 docker images 命令即可看到该映像。

docker images

--- 
# 推送docker image到网上的docker hub

docker push hejibo1984/facemorperbyhejibo:withFaceLandmark