# Django Image Compression - Pillow

Storage is one of the essential pieces of web app development and needs to be paid special attention as it attracts server costs. If you have to pay for the storage costs of your web apps that involve images or any other non-text content it is better to focus on compression to reduce storage costs and scale at ease. This post discusses the image compression (lossy) in Django in detail and demonstrates an example of its implementation. You can find all the implementation details here.


### What is compression?

According to Wikipedia, data-compression involves encoding information using fewer bits than the original representation. To put it in simple words, compression is a method of making the file size smaller using a specific technique or algorithm.

Types and methods Data-compression is classified into two types.

**Lossy:** In this type of compression, the quality of data(in this case images and video) is reduced on compression. This is widely used to compress multimedia.

**Lossless:** In this type of compression, the quality of data(in this case image) is not lost. This is in wide use to compress sensitive data where data loss cannot be afforded.


### Installation and Configuration

Install the python image handling library [Pillow](https://pypi.org/project/Pillow/2.2.1/)

```
 pip install -r requirements.txt

```

We will set up a simple project to demonstrate the image upload and the file sizes of before and after upload. 

### Reference link 

* [Dev.to](https://dev.to/gajesh/compress-images-in-django-3la8) blog post.
* [BytesIO documentation](https://docs.python.org/3/library/io.html#io.BytesIO)



