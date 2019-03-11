from skimage import io
import pylab
import numpy as np

N1=256;
N2=256; 
n=0.2;
f=io.imread('hello.jpg',as_gray=True) 
b=np.ones((4,4))/4**2
F=np.fft.fft2(f)
B=np.fft.fft2(b,(N1,N2))
G=F*B
pylab.subplot(1,3,1)
pylab.title('Blur')
pylab.imshow(abs(np.fft.ifft2(G)), cmap='gray', interpolation='nearest')

BF = np.where(abs(B)<n)
B[BF]=n;
H= np.ones((N1,N2))/B;

I =G*H ;
im=abs(np.fft.ifft2(I));

pylab.subplot(1 , 3 , 2)
pylab.title('Restored')
pylab.imshow(im, cmap='gray', interpolation='nearest')
pylab.subplot(1,3,3)
pylab.title('Original')
pylab.imshow(f, cmap='gray', interpolation='nearest')

pylab.show()