int main() {
	bool a = TRUE;
	bool b = FALSE;
	int c = 1;
	int d = 2;
	
	if(a == b) {
		print("-1");
	}
	
	else {
		print("1");
	}
	
	if(NOT c > d) {
		print("-1");
	}
	
	else {
		print("2");
	}
	
	if(d > c AND a) {
		print("3");
	}
	
	else {
		print("-1");
	}
	
	if(c > d AND a) {
		print("-1");
	}
	
	else {
		print("4");
	}
	
	return 0;
}