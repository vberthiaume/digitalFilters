import sys
sys.path.append("C:\\Users\\barth\\Documents\\git\\digitalFilters\\CppExtension\\vbCpp\\Release")
import vbCpp

print ("\n====================\n welcome to VBCPP!!!\n====================\n")

print ("attributes for the object are: ",  dir(vbCpp), "\n")

print ("__doc__ is:\t",      vbCpp.__doc__)

print ("vbCpp.fir_3(1) is:", vbCpp.fir_3(1))
