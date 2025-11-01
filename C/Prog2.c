#include<stdio.h>

int main() {
	
	int num=42;
	float price = 99.95f;
	char grade = 'A';
	
	int *num_ptr;
	float *price_ptr;
	char *grade_ptr;
	
	printf("%d, %p, %zu\n", num, &num, sizeof(num));
	printf("%.2f, %p, %zu\n", price, &price, sizeof(price));
	printf("%c, %p, %zu", grade, &grade, sizeof(grade));
	
	// first value = value itself, second value = address, third value = bytes size
	
	return 0;
}


/*

POINTERS

Pointers vs Arrays
- The name of an array (eg. scores) is essentially a constant POINTER TO ITS FIRST ELEMENT
= scores & &scores have same value (address of 1st element)

Example:

int scores[5] = {1,2,3,4,5}
*(scores + 2) IS EQUAL TO scores[2]


BEST PRACTICES:

1. ALWAYS initialize pointers
2. Check for NULL before dereferencing

if(safe_ptr != NULL) {
	safe to dereference %d, *safe_ptr
} else {
	NULL, CANNOT DEREFERENCE SAFELY
}

3. Set pointers to NULL after freeing

Example:

int *dynamic_ptr = malloc(sizeof(int));
if(dynamic_ptr != NULL) {
	*dynamic_ptr = 42;
	printf
	free(dynamic_ptr);
	dynamic_ptr = NULL (PREVENTS ACCIDENTAL USE)
}

Otherwise, it will target a random memory/access (contain garbage)

*/

/*
int a = 10;  (B20)
int *b = NULL;  (A10)
int **c = NULL

QUESTION: How to target value of a?

INCORRECT: *b = &a   then b = 10;
Why? *b value is going to be changed to address of A (so it will be changed to B20)

CORRECT:



if **c = &b
then **c = a = 10;


if (*b != NULL) {
	printf("%d", *b);
	free(b)
	b = NULL
}
*/
