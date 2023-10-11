#include <Python.h>

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject representing a Python list
*/
void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	printf("[*] SIze of the Python LIst = %ld\n", PyList_Size(p));

	PyObject *item;
	Py_ssize_t i;

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 * print_python_bytes - Print basic info about Python bytes objects
 * @p: PyObject representing a Python bytes object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, length;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("	[ERROR] Invalid Bytes Object\n");
		return;
	}

	length = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("	size: %ld\n", length);
	printf("	trying string: %s\n", str);

	printf("	first 10 bytes: ");

	for (i = 0; i < length && i < 10; i++)
		printf("%02x%c", (unsigned char)str[i], i < 9 ? ' ': '\n');

