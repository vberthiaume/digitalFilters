#include "include.h"


PyMethodDef VbCppMethods[] = {
	{0,0,0,0}
};

static struct PyModuleDef vbCpp = {
   PyModuleDef_HEAD_INIT,
   "vbCpp",				// name of module
   "this is my doc",	// module documentation, may be NULL
   -1,					// size of per-interpreter state of the module, or -1 if the module keeps state in global variables. 
   VbCppMethods
};


PyMODINIT_FUNC
PyInit_vbCpp(void)
{
    return PyModule_Create(&vbCpp);
}