#include "python.h" 

static PyObject*



main_t_count(PyObject *self, PyObject* args1)
{
    const char* total=NULL;
             
    if (!PyArg_ParseTuple(args1, "s", &total) )
         return NULL;

    int n = *total + 0;
  
    if (n > 10)
        n = 5;
    return Py_BuildValue("i", n);
}

static PyMethodDef mainMethods[] = {
    {"t_count", main_t_count, METH_VARARGS,
    "count."},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef mainmodule = {
    PyModuleDef_HEAD_INIT,
    "main",
    "It is test module.",
    -1,mainMethods
};

PyMODINIT_FUNC
PyInit_main(void)
{
    return PyModule_Create(&mainmodule);
}
