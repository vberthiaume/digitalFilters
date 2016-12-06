Nx = 1024;              # input signal length (nonzero portion)
Nh = 128;               # FIR filter length

# FIR "running sum" filter
A = 1; 
B = ones(1,Nh);  

n = 0:Nx-1;

x = sin(n*2*pi*7/Nx);   # input sinusoid - zero-pad it:

zp=zeros(1,Nx/2); xzp=[zp,x,zp]; nzp=[0:length(xzp)-1];
y = filter(B,A,xzp);    # filtered output signal