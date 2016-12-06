#include "include.h"


PyObject* fir3(PyObject* self, PyObject* args){
	__int64 input_value;
	if(!PyArg_ParseTuple(args, "L", &input_value)){
		return 0;
	}
	//we need to construct a new object to return, because python integers are immutable
	return PyLong_FromLongLong(input_value +1);
}

PyMethodDef VbCppMethods[] = {
	{"fir_3", (PyCFunction)fir3, METH_VARARGS, 0},
	//{0,0,0,0}
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