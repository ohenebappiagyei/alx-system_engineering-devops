#include <Python.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject pointer to the bytes object
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes_obj;
    Py_ssize_t size, i;
    unsigned char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_obj = (PyBytesObject *)p;
    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %d bytes:", (size > 10) ? 10 : (int)size);
    for (i = 0; i < ((size > 10) ? 10 : size); i++)
        printf(" %02x", str[i]);

    printf("\n");
}

/**
 * print_python_list - Print information about a Python list.
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyTuple_Check(item))
            printf("tuple\n");
        else if (PyList_Check(item))
            print_python_list(item);
        else if (PyLong_Check(item))
            printf("int\n");
        else if (PyUnicode_Check(item))
            printf("str\n");
        else
            printf("unknown\n");
    }
}

