#include "include.h"


//CODE FROM 2.7 TUTORIAL
//PyMethodDef SpamMethods[] = {
//	{0,0,0,0}
//};
//
//PyMODINIT_FUNC
//initspam(void)
//{
//    PyObject *m;
//
//    m = Py_InitModule("spam", SpamMethods);
//    if (m == NULL)
//        return;
//
//    //SpamError = PyErr_NewException("spam.error", NULL, NULL);
//    //Py_INCREF(SpamError);
//    //PyModule_AddObject(m, "error", SpamError);
//}

//CODE FROM 3.5 TUTORIAL
//static PyObject *spam_system(PyObject *self, PyObject *args) {
//    const char *command;
//
//    if (!PyArg_ParseTuple(args, "s", &command)){
//        return NULL;
//	}
//    int sts = system(command);
//    return PyLong_FromLong(sts);
//}

PyMethodDef VbCppMethods[] = {
	{0,0,0,0}
};

static struct PyModuleDef vbCpp = {
   PyModuleDef_HEAD_INIT,
   "vbCpp",   /* name of module */
   "this is my doc", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   VbCppMethods
};


PyMODINIT_FUNC
PyInit_vbCpp(void)
{
    return PyModule_Create(&vbCpp);
}