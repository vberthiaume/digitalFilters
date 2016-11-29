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
static PyObject *spam_system(PyObject *self, PyObject *args) {
    const char *command;

    if (!PyArg_ParseTuple(args, "s", &command)){
        return NULL;
	}
    int sts = system(command);
    return PyLong_FromLong(sts);
}