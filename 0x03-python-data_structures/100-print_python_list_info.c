#include <Python.h>

/**
 * print_python_list_info - Print basic inf of Python list
 * @p: pyObject list
 */

void print_python_list_info(pyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((pyListObject *)p)->allocated;

	printf("[*] size of python list = %d\n", size);
	printf("[*] allocate = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
