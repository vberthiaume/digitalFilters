#include "include.h"


static int NTICK = 256;

static PyObject* fir3(PyObject* self, PyObject* args){
	double input;
	double* outputAout;
	double* inputAinp;
	double b0;
	double b1;
	double b2;
	double s1;
	double s2;
	if(!PyArg_ParseTuple(args, "dd*d*", &input, &outputAout)){
		return 0;
	}

	for(int i = 0; i < NTICK; i++){
		input = inputAinp[i];
		outputAout[i] = b0 * input + b1 * s1 + b2 * s2;
		s2 = s1;
		s1 = input;
	}
}


static PyObject* func(PyObject* self, PyObject* args) {
  PyObject *list2_obj;
  PyObject *list3_obj;
  if (!PyArg_ParseTuple(args, "OO", &list2_obj, &list3_obj))
    return NULL;

  double **list2;
  double ***list3;

  //Create C arrays from numpy objects:
  int typenum = NPY_DOUBLE;
  PyArray_Descr *descr;
  descr = PyArray_DescrFromType(typenum);
  npy_intp dims[3];
  if (PyArray_AsCArray(&list2_obj, (void **)&list2, dims, 2, descr) < 0 || PyArray_AsCArray(&list3_obj, (void ***)&list3, dims, 3, descr) < 0) {
    PyErr_SetString(PyExc_TypeError, "error converting to c array");
    return NULL;
  }
  printf("2D: %f, 3D: %f.\n", list2[3][1], list3[1][0][2]);
}

//static PyObject* fir3(PyObject* self, PyObject* args){
//	double input_value;
//	if(!PyArg_ParseTuple(args, "L", &input_value)){
//		return 0;
//	}
//	//we need to construct a new object to return, because python integers are immutable
//	return PyLong_FromLongLong(input_value +1);
//}



//static PyObject* fir3(PyObject* self, PyObject* args){
//	__int64 input_value;
//	if(!PyArg_ParseTuple(args, "L", &input_value)){
//		return 0;
//	}
//	//we need to construct a new object to return, because python integers are immutable
//	return PyLong_FromLongLong(input_value +1);
//}

static PyMethodDef VbCppMethods[] = {
	{"fir_3", (PyCFunction)fir3, METH_VARARGS, 0},
	{0,0,0,0}
};

static struct PyModuleDef vbCpp = {
   PyModuleDef_HEAD_INIT,
   "vbCpp",				// name of module
   "this is my doc",	// module documentation, may be NULL
   -1,					// size of per-interpreter state of the module, or -1 if the module keeps state in global variables. 
   VbCppMethods
};


PyMODINIT_FUNC PyInit_vbCpp(void) {
    return PyModule_Create(&vbCpp);
}



