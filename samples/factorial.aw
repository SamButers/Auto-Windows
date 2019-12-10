int factorial(int x) {
	if x <= 1 {
	return 1;
	}

	return x * factorial(x - 1);
}

int main() {
	int x;
	read(x);

	x = factorial(x);
	print(x);

	return 0;
}