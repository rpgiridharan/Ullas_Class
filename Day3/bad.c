#include <stdio.h>
#include <string.h>

int main()
{
	char input[6];
	char password[] = "Hello";
	//printf("Please enter the password: ");
	gets(input);
	if (strncmp(input, password, 5) == 0)
	{
		printf("Welcome\n");
		printf("%s", password);
	}
	else
	{
		printf("invalid password");
	}
}
