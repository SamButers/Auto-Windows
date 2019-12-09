int main() {
	int x1;
	int x2;
	int y1;
	int y2;

	read(x1, x2, y1, y2);

	if x1 < MOUSE_X < x2 AND y1 < MOUSE_Y < y2 {
		int xMiddle = x1 + (x2 - x1)/2;
		int yMiddle = y1 + (y2 - y1)/2;
		int xOffset = 100;
		int yOffset = 100;
		
		if MOUSE_X < xMiddle {
			xOffset = xOffset * (-1);
		}
		
		if MOUSE_Y < yMiddle {
			yOffset = yOffset * (-1);
		}
		
		moveCursor(xOffset, yOffset, 1, 0);
	}

	return 0;
}