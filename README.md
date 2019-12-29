# Introduction to Machine Learning 

Respitory này được tạo ra nhằm tạo ra cách tiếp cận dễ dàng cho những người mới tìm hiểu Machine Learning. Bài giảng được lấy từ khoá học Introduction to Machine Learning for Coders của fast.ai. \
[Intro to Machine Learning for Coders](http://course18.fast.ai/ml) \
[Ghi chép về khoá học](https://medium.com/@hiromi_suenaga/machine-learning-1-lesson-1-84a1dc2b5236) \
[Wiki](https://forums.fast.ai/t/wiki-thread-lesson-1/6825) 

## Installation 
Hướng dẫn cài đặt môi trường lập trình cho khoá học. \
**Anaconda:** một platform cung cấp các góp thư viện để lập trình Python. Anaconda có thể chạy trên nhiều hệ điều hành. Một công cụ mạnh dùng cùng Command Line. \
  [Windows](https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/) \
  [Mac](https://problemsolvingwithpython.com/01-Orientation/01.04-Installing-Anaconda-on-MacOS/) \
  [Linux](https://problemsolvingwithpython.com/01-Orientation/01.05-Installing-Anaconda-on-Linux/) 
  ``` bash 
  # Clone respitory fastai which contains library for courses (needed install Github)
  git clone https://github.com/fastai/fastai 
  cd fastai  
  conda create -n fastai python=3.6 anaconda
  # If we don't have GPU 
  conda env update --file environment-cpu.yml 
  source active fastai 
  ```
  

