int main() {
	File b;
	open(b, "test.txt", 'w');
	
	print(b, "This is a wonderful test.");
	
	close(b, 'w');
	
	return 0;
}