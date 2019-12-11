int main() {
	File b;
	string a;
	string c;
	open(b, "a.txt", 'r');
	
	read(b, a, c);
	print(a, '\n', c);
	
	close(b, 'r');
	
	return 0;
}