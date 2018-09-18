clear all
clc 

%% JPEG 
figure;
subplot(221);
imshow('jpg3.jpg');
I1=imread('jpg3.jpg');
subplot(222);
imhist(I1);
title('histogram of jpg')

%% PNG
subplot(223);
imshow('png3.png')
I2=imread('png3.png');
subplot(224);
imhist(I2);
title('histogram of png')

%% BMP
figure;
subplot(221);
imshow('bmp3.bmp')
I3=imread('bmp3.bmp');
subplot(222);
imhist(I3);
title('histogram of bmp')

%% GIF
subplot(223);
imshow('gif3.gif')
I4=imread('gif3.gif');
subplot(224);
imhist(I4);
title('histogram of gif')
%% Tiff
figure;
subplot(211);
imshow('tiff3.tiff')
I5=imread('tiff3.tiff');
subplot(212);
imhist(I5);
title('histogram of tiff')


%% Cumulative and Equalization
figure;
subplot(231);
imshow('jpg3.jpg');
I1=imread('jpg3.jpg');
h1=imhist(I1);
subplot(232);imhist(I1); % histogram of jpeg before
c1=cumsum(h1); %cumulative before
subplot(233); plot(c1);
q1=histeq(I1); %histogram equalization(picture high quality)
subplot(234);imshow(q1);
subplot(235);imhist(q1);% histogram of jpeg after
h2=imhist(q1);
c2=cumsum(h2); %cumulative after
subplot(236); plot(c2);





