#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: A PythonObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, allocate, j;
	PyObject *obj;

	size = py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%S\n", Py_TYPE(obj)->tp_name)
	}
}
